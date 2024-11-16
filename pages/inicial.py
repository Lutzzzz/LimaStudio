import streamlit as st
import pandas as pd
from utils.db import conectar_banco
from datetime import datetime, timedelta
from css.styles import apply_custom_styles

def pagina_inicial():
    apply_custom_styles()  # Aplicando estilos customizados
    st.title("Bem-vindo ao LimaStudio!")
    
    # Exibir a data atual
    st.write(f"**Data de hoje:** {datetime.now().strftime('%d/%m/%Y')}")
    
    # Exibir os próximos agendamentos do dia
    st.subheader("Agendamentos Futuros - Hoje")
    exibir_tabela_agendamentos(datetime.now())
    
    # Exibir os agendamentos do próximo dia
    proximo_dia = datetime.now() + timedelta(days=1)
    st.subheader("Agendamentos Futuros - Próximo Dia")
    exibir_tabela_agendamentos(proximo_dia)

def exibir_tabela_agendamentos(data):
    connection = conectar_banco()
    cursor = connection.cursor()

    # Definir o horário de início (7:00) e o horário final (22:00) para o dia especificado
    horario_inicial = data.replace(hour=7, minute=0, second=0, microsecond=0)
    horario_final = data.replace(hour=22, minute=0, second=0, microsecond=0)

    # Gerar a lista de horários de 30 em 30 minutos entre 7:00 e 22:00
    horarios = []
    while horario_inicial <= horario_final:
        horarios.append(horario_inicial.strftime('%H:%M'))
        horario_inicial += timedelta(minutes=30)

    # Ajuste: Usar o formato correto 'DD/MM/YYYY' para compatibilidade com o banco de dados Oracle
    data_str = data.strftime('%d/%m/%Y')

    # Imprimir a data usada na consulta para depuração
    st.write(f"Consultando a data: {data_str}")

    # Consulta SQL ajustada para usar TRUNC() e garantir que a comparação seja feita apenas com a data (sem o horário)
    cursor.execute("""
        SELECT p.nome AS profissional, s.nome_servico, a.data_hora, c.nome AS cliente
        FROM agendamentos a
        JOIN servicos s ON a.id_servico = s.id_servico
        JOIN profissionais p ON a.id_profissional = p.id_profissional
        JOIN clientes c ON a.id_cliente = c.id_cliente
        WHERE TRUNC(a.data_hora) = TO_DATE(:data_dia, 'DD/MM/YYYY')  -- Usar TRUNC para comparar apenas a data
        ORDER BY a.data_hora
    """, {'data_dia': data_str})

    agendamentos = cursor.fetchall()

    # Verificar se a consulta retornou dados
    if not agendamentos:
        st.write("Nenhum agendamento encontrado para este dia.")
        return

    # Criar um dicionário para armazenar os agendamentos por horário e profissional
    tabela_agendamentos = {}

    # Preencher a tabela com os dados dos agendamentos
    for agendamento in agendamentos:
        nome_profissional = agendamento[0]
        nome_servico = agendamento[1]
        data_hora = agendamento[2].strftime('%H:%M')  # Formatando a hora
        nome_cliente = agendamento[3]

        if data_hora not in tabela_agendamentos:
            tabela_agendamentos[data_hora] = {}

        tabela_agendamentos[data_hora][nome_profissional] = f"{nome_cliente} - {nome_servico}"

    # Criar a tabela com os dados
    tabela = []

    # Cabeçalho: profissionais
    profissionais = list(set([nome_profissional for horarios_agendamentos in tabela_agendamentos.values() for nome_profissional in horarios_agendamentos.keys()]))

    # Garantir que todos os horários (7:00 - 22:00) estejam presentes, mesmo que sem agendamento
    for horario in horarios:
        if horario not in tabela_agendamentos:
            tabela_agendamentos[horario] = {}

    # Adicionar os profissionais no cabeçalho
    tabela.append(["Horário"] + profissionais)

    # Mapeamento de cores para os serviços
    cores_servicos = {
        'Corte de Cabelo': '#FFDDC1',
        'Manicure': '#D1FFDC',
        'Pedicure': '#D1D1FF',
        'Massagem': '#F2D1FF',
        'Escova': '#FFFCF2',
        'Maquiagem': '#F2F0F0'
    }

    # Adicionar os agendamentos nas células correspondentes
    for horario in horarios:
        linha = [horario]  # Hora na primeira coluna
        for profissional in profissionais:
            if horario in tabela_agendamentos and profissional in tabela_agendamentos[horario]:
                servico_nome = tabela_agendamentos[horario][profissional].split(' - ')[1]
                cor_servico = cores_servicos.get(servico_nome, '#FFFFFF')  # Cor padrão caso o serviço não esteja no mapeamento
                agendamento_info = tabela_agendamentos[horario][profissional]

                linha.append(f'<div style="background-color:{cor_servico}; color:black; padding: 5px; word-wrap: break-word; white-space: pre-wrap;">{agendamento_info}</div>')
            else:
                linha.append("")  # Se não houver agendamento, célula vazia
        tabela.append(linha)

    # Criar o DataFrame com pandas
    df = pd.DataFrame(tabela[1:], columns=tabela[0])

    # Exibir a tabela com Streamlit ajustando automaticamente
    st.markdown(df.to_html(escape=False), unsafe_allow_html=True)

    connection.close()

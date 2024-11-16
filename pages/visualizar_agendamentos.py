import streamlit as st
import pandas as pd
from utils.db import conectar_banco
from css.styles import apply_custom_styles

def visualizar_agendamentos():
    st.title("Visualizar Agendamentos Atuais")

    connection = conectar_banco()
    cursor = connection.cursor()

    # Ajuste na consulta SQL para incluir o nome do cliente
    cursor.execute("""
        SELECT p.nome AS profissional, s.nome_servico, a.data_hora, c.nome AS cliente
        FROM agendamentos a
        JOIN servicos s ON a.id_servico = s.id_servico
        JOIN profissionais p ON a.id_profissional = p.id_profissional
        JOIN clientes c ON a.id_cliente = c.id_cliente
        WHERE TRUNC(a.data_hora) >= TRUNC(SYSDATE)
        ORDER BY a.data_hora
    """)
    agendamentos = cursor.fetchall()

    if agendamentos:
        apply_custom_styles()

        # Criar DataFrame com os agendamentos
        tabela_dados = []
        cores_servicos = {
            'Corte de Cabelo': '#FFDDC1',
            'Manicure': '#D1FFDC',
            'Pedicure': '#D1D1FF',
            'Massagem': '#F2D1FF',
            'Escova': '#FFFCF2',
            'Maquiagem': '#F2F0F0'
        }

        for agendamento in agendamentos:
            profissional = agendamento[0]
            servico = agendamento[1]
            data_hora = agendamento[2].strftime('%d/%m/%Y %H:%M')
            cliente = agendamento[3]
            cor_fundo = cores_servicos.get(servico, '#FFFFFF')

            # Ajuste para garantir que a cor da fonte seja visível (preto)
            estilo_fonte = "color: black;"

            tabela_dados.append({
                'Profissional': profissional,
                'Serviço': f'<div style="background-color:{cor_fundo}; padding: 5px; word-wrap: break-word; white-space: pre-wrap; {estilo_fonte}">{servico}</div>',
                'Cliente': cliente,
                'Data e Hora': data_hora
            })

        # Criar DataFrame
        df = pd.DataFrame(tabela_dados)

        # Exibir tabela com Streamlit
        st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)
    else:
        st.write("Não há agendamentos futuros.")

    connection.close()

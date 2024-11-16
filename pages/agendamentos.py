import streamlit as st
from datetime import datetime
from utils.db import conectar_banco

def pagina_agendamentos():
    st.title("Agendamentos")

    st.subheader("Realizar Agendamento")

    connection = conectar_banco()
    cursor = connection.cursor()

    # Obter lista de profissionais
    cursor.execute("SELECT id_profissional, nome FROM profissionais")
    profissionais = cursor.fetchall()

    # Obter lista de serviços
    cursor.execute("SELECT id_servico, nome_servico FROM servicos")
    servicos = cursor.fetchall()

    if profissionais and servicos:
        # Selecionar profissional
        lista_profissionais = [profissional[1] for profissional in profissionais]
        profissional_selecionado = st.selectbox("Escolha o Profissional", lista_profissionais)
        id_profissional_selecionado = next(
            (profissional[0] for profissional in profissionais if profissional[1] == profissional_selecionado), None
        )

        # Selecionar serviço
        lista_servicos = [servico[1] for servico in servicos]
        servico_selecionado = st.selectbox("Escolha o Serviço", lista_servicos)
        id_servico_selecionado = next(
            (servico[0] for servico in servicos if servico[1] == servico_selecionado), None
        )

        # Autocompletar cliente
        cursor.execute("SELECT nome FROM clientes")
        clientes = cursor.fetchall()
        lista_clientes = [cliente[0] for cliente in clientes]
        nome_cliente = st.selectbox("Nome do Cliente (Digite ou Selecione)", lista_clientes)
        telefone_cliente = st.text_input("Telefone do Cliente")

        data = st.date_input("Data do Agendamento")
        hora = st.time_input("Hora do Agendamento")
        data_hora = datetime.combine(data, hora) if data and hora else None

        status = st.selectbox("Status do Agendamento", ['pendente', 'concluido', 'cancelado'])

        submit_button = st.button("Agendar")

        if submit_button:
            if nome_cliente and telefone_cliente and id_profissional_selecionado and id_servico_selecionado and data_hora:
                try:
                    cursor.execute("SELECT id_cliente FROM clientes WHERE nome = :nome_cliente", {"nome_cliente": nome_cliente})
                    cliente = cursor.fetchone()

                    if cliente:
                        id_cliente = cliente[0]
                    else:
                        cursor.execute("""
                            INSERT INTO clientes (id_cliente, nome, telefone)
                            VALUES (seq_clientes.NEXTVAL, :nome_cliente, :telefone_cliente)
                            RETURNING id_cliente INTO :id_cliente
                        """, {
                            "nome_cliente": nome_cliente,
                            "telefone_cliente": telefone_cliente,
                            "id_cliente": cursor.var(int)
                        })
                        id_cliente = cursor.var(int).getvalue()

                    cursor.execute("""
                        INSERT INTO agendamentos (id_agendamento, id_cliente, id_profissional, id_servico, data_hora, status)
                        VALUES (seq_agendamentos.NEXTVAL, :id_cliente, :id_profissional, :id_servico, :data_hora, :status)
                    """, {
                        "id_cliente": id_cliente,
                        "id_profissional": id_profissional_selecionado,
                        "id_servico": id_servico_selecionado,
                        "data_hora": data_hora,
                        "status": status
                    })
                    connection.commit()
                    st.success("Agendamento realizado com sucesso!")
                except Exception as e:
                    connection.rollback()
                    st.error(f"Erro ao realizar agendamento: {e}")
            else:
                st.error("Todos os campos são obrigatórios.")
    else:
        st.write("Não há profissionais ou serviços cadastrados.")
    connection.close()

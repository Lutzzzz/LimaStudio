import streamlit as st
from utils.db import conectar_banco

# Função para exibir a lista de profissionais
def pagina_profissionais():
    st.title("Profissionais")
    
    # Exibir os profissionais cadastrados no banco de dados
    st.subheader("Lista de Profissionais")
    
    # Conectar ao banco de dados
    connection = conectar_banco()
    cursor = connection.cursor()
    
    # Consultar profissionais
    cursor.execute("SELECT id_profissional, nome, especialidade, numero_atendimentos FROM profissionais")
    profissionais = cursor.fetchall()
    
    connection.close()
    
    if profissionais:
        for profissional in profissionais:
            st.write(f"**Nome:** {profissional[1]}")
            st.write(f"**Especialidade:** {profissional[2]}")
            st.write(f"**Número de Atendimentos:** {profissional[3]}")
            st.write("---")
    else:
        st.write("Nenhum profissional cadastrado.")
    
    # Formulário para cadastrar um novo profissional
    st.subheader("Cadastrar Novo Profissional")
    
    with st.form(key="form_profissional"):
        nome = st.text_input("Nome do Profissional")
        especialidade = st.text_input("Especialidade")
        
        # Botão de envio do formulário
        submit_button = st.form_submit_button("Cadastrar Profissional")
        
        if submit_button:
            if nome and especialidade:
                try:
                    # Conectar ao banco de dados para inserir o novo profissional
                    connection = conectar_banco()
                    cursor = connection.cursor()
                    
                    cursor.execute("""
                        INSERT INTO profissionais (id_profissional, nome, especialidade, numero_atendimentos)
                        VALUES (seq_profissionais.NEXTVAL, :nome, :especialidade, 0)
                    """, {
                        "nome": nome,
                        "especialidade": especialidade,
                    })
                    connection.commit()
                    connection.close()
                    
                    st.success("Profissional cadastrado com sucesso!")
                except Exception as e:
                    st.error(f"Erro ao cadastrar profissional: {e}")
            else:
                st.error("Todos os campos são obrigatórios!")

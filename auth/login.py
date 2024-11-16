import streamlit as st
from utils.db import conectar_banco

# Função para autenticar o usuário
def autenticar_usuario(usuario, senha):
    connection = conectar_banco()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM usuarios WHERE nome = '{usuario}' AND senha = '{senha}'")
    result = cursor.fetchone()
    connection.close()
    return result is not None

# Tela de login
def tela_login():
    st.title("Login")
    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")
    
    if st.button("Entrar"):
        if autenticar_usuario(usuario, senha):
            st.session_state.autenticado = True
            st.session_state.usuario_atual = usuario
            st.rerun()  # Redefine a aplicação e vai para a tela principal
        else:
            st.error("Usuário ou senha inválidos")

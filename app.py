import streamlit as st
from pages.inicial import pagina_inicial
from pages.agendamentos import pagina_agendamentos
from pages.visualizar_agendamentos import visualizar_agendamentos
from pages.estoque import pagina_estoque
from pages.profissionais import pagina_profissionais
from auth.login import tela_login  # Importando a tela de login
from css.styles import apply_custom_styles  # Aplicação de estilos customizados

# Função principal
def main():
    apply_custom_styles()

    # Inicializa a sessão de autenticação
    if "autenticado" not in st.session_state:
        st.session_state.autenticado = False

    if not st.session_state.autenticado:
        tela_login()  # Exibe a tela de login se não autenticado
    else:
        # Menu lateral com navegação
        st.sidebar.title("Menu")
        menu = st.sidebar.selectbox(
            "Selecione uma página",
            ["Inicial", "Agendamentos", "Visualizar Agendamentos", "Estoque", "Profissionais", "Sair"]
        )

        # Redirecionamento para páginas
        if menu == "Inicial":
            pagina_inicial()
        elif menu == "Agendamentos":
            pagina_agendamentos()
        elif menu == "Visualizar Agendamentos":
            visualizar_agendamentos()
        elif menu == "Estoque":
            pagina_estoque()
        elif menu == "Profissionais":
            pagina_profissionais()
        elif menu == "Sair":
            st.session_state.autenticado = False
            st.rerun()  # Reinicia a aplicação para voltar à tela de login

if __name__ == "__main__":
    main()

import streamlit as st

def apply_custom_styles():
    st.markdown(
        """
        <style>
            /* Garantir que a tabela ocupe toda a largura */
            .streamlit-table {
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                font-size: 14px;
            }

            
        </style>
        """,
        unsafe_allow_html=True
    )

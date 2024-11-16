import streamlit as st
from utils.db import conectar_banco
from datetime import date

# Função para exibir o estoque
def exibir_estoque():
    st.subheader("Estoque Atual")
    connection = conectar_banco()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT id_item, nome_item, quantidade, descricao, data_vencimento, preco_unitario FROM estoque")
        estoque = cursor.fetchall()

        if estoque:
            for item in estoque:
                st.write(f"**ID Item**: {item[0]}")
                st.write(f"**Nome**: {item[1]}")
                st.write(f"**Quantidade**: {item[2]}")
                st.write(f"**Descrição**: {item[3]}")
                st.write(f"**Data de Vencimento**: {item[4].strftime('%d/%m/%Y') if item[4] else 'Sem data'}")
                # Tratar preco_unitario nulo
                preco_unitario = item[5] if item[5] is not None else 0.00
                st.write(f"**Preço Unitário**: R$ {preco_unitario:.2f}" if item[5] is not None else "Preço Unitário: Não informado")
                st.write("---")
        else:
            st.write("Nenhum item encontrado no estoque.")
    except Exception as e:
        st.error(f"Erro ao carregar estoque: {e}")
    finally:
        connection.close()

# Função para adicionar itens ao estoque
def adicionar_item():
    st.subheader("Adicionar Novo Item ao Estoque")

    nome_item = st.text_input("Nome do Item")
    quantidade = st.number_input("Quantidade", min_value=1, step=1)
    descricao = st.text_area("Descrição")
    data_vencimento = st.date_input("Data de Vencimento (opcional)", value=None)
    preco_unitario = st.number_input("Preço Unitário (opcional)", min_value=0.0, step=0.01, format="%.2f")

    if st.button("Adicionar Item"):
        if nome_item and quantidade > 0:
            connection = conectar_banco()
            cursor = connection.cursor()

            try:
                cursor.execute(
                    """
                    INSERT INTO estoque (id_item, nome_item, quantidade, descricao, data_vencimento, preco_unitario)
                    VALUES (seq_estoque.NEXTVAL, :nome_item, :quantidade, :descricao, :data_vencimento, :preco_unitario)
                    """,
                    {
                        "nome_item": nome_item,
                        "quantidade": quantidade,
                        "descricao": descricao,
                        "data_vencimento": data_vencimento if data_vencimento else None,
                        "preco_unitario": preco_unitario if preco_unitario > 0 else None,
                    }
                )
                connection.commit()
                st.success("Item adicionado ao estoque com sucesso!")
            except Exception as e:
                st.error(f"Erro ao adicionar item ao estoque: {e}")
            finally:
                connection.close()
        else:
            st.error("Todos os campos obrigatórios devem ser preenchidos.")

# Função principal da página de estoque
def pagina_estoque():
    st.title("Gerenciamento de Estoque")
    
    # Menu para escolher a ação
    opcao = st.radio("Escolha uma ação", ["Exibir Estoque", "Adicionar Item"])
    
    if opcao == "Exibir Estoque":
        exibir_estoque()
    elif opcao == "Adicionar Item":
        adicionar_item()

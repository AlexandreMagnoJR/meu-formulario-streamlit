import streamlit as st
import pandas as pd

# --- 1. Configuração da Página ---
st.set_page_config(
    page_title="Meu Formulário Interativo",
    layout="wide"
)

st.title("📝 Formulário de Dados")

# --- 2. Criação do DataFrame (Tabela) Inicial ---
dados_iniciais = {
    'Nome do Produto': ['Caneta', 'Lápis', 'Borracha'],
    'Quantidade': [1, 2, 3],
    'Preço (€)': [1.00, 0.50, 0.75],
    'Urgente': [True, False, False]
}
df = pd.DataFrame(dados_iniciais)

# --- 3. Uso do st.data_editor (Onde a mágica acontece!) ---
st.markdown("### Preencha a Tabela Abaixo:")
df_editado = st.data_editor(
    df,
    num_rows="dynamic", # Permite adicionar/apagar linhas
    column_config={
        "Preço (€)": st.column_config.NumberColumn(
            "Preço (€)",
            format="€%.2f",
        ),
        "Urgente": st.column_config.CheckboxColumn(
            "Urgente",
            default=False
        )
    },
    hide_index=True
)

# --- 4. Processamento dos Dados ---
if st.button("Salvar os Dados"):
    # AQUI você usaria o DataFrame 'df_editado' para salvar ou analisar
    st.success("Dados preenchidos e prontos para uso!")
    st.dataframe(df_editado)

"""
Streamlit page for batch processing.
"""
import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"

st.title("📁 Processamento em Lote")

st.markdown("Upload de arquivos CSV ou JSON para processamento em massa.")

# File upload
st.subheader("📤 Upload de Arquivo")
uploaded_file = st.file_uploader(
    "Selecione um arquivo CSV ou JSON",
    type=['csv', 'json'],
    help="O arquivo deve conter uma coluna 'texto' ou campo 'texto' com os atendimentos"
)

if uploaded_file:
    file_details = {
        "Nome": uploaded_file.name,
        "Tipo": uploaded_file.type,
        "Tamanho": f"{uploaded_file.size / 1024:.2f} KB"
    }
    st.json(file_details)
    
    # Preview
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            import json
            data = json.loads(uploaded_file.getvalue())
            df = pd.DataFrame(data if isinstance(data, list) else [data])
        
        st.subheader("👁️ Preview dos Dados")
        st.dataframe(df.head(10), use_container_width=True)
        st.caption(f"Total de registros: {len(df)}")
        
        uploaded_file.seek(0)
    except Exception as e:
        st.error(f"Erro ao ler arquivo: {e}")

# Processing options
st.subheader("⚙️ Opções de Processamento")
col1, col2 = st.columns(2)

with col1:
    output_format = st.selectbox(
        "Formato de Saída",
        ["JSON", "CSV"],
        index=0
    )

with col2:
    st.checkbox("Incluir justificativas", value=False, disabled=True)
    st.caption("_Em desenvolvimento_")

# Process button
if st.button("🚀 Processar Lote", type="primary", use_container_width=True):
    if not uploaded_file:
        st.warning("⚠️ Por favor, faça upload de um arquivo primeiro.")
    else:
        with st.spinner("Processando arquivo... (implementação pendente)"):
            st.info("📝 O processamento em lote ainda está sendo implementado.")
            st.markdown("""
            ### Próximos Passos:
            1. Implementar endpoint `/batch/` no backend
            2. Adicionar parsing de CSV/JSON
            3. Processar itens em paralelo
            4. Gerar arquivo de saída
            5. Mostrar relatório de processamento
            """)

# Template download
st.markdown("---")
st.subheader("📋 Template de Entrada")

if st.button("⬇️ Baixar Template CSV"):
    template_df = pd.DataFrame({
        "id": ["1", "2", "3"],
        "texto": [
            "Cliente solicitou reembolso por cobrança duplicada...",
            "Dúvida sobre funcionamento do produto...",
            "Reclamação de demora na entrega..."
        ],
        "data": ["2024-01-15", "2024-01-15", "2024-01-16"]
    })
    st.download_button(
        "Confirmar Download",
        template_df.to_csv(index=False),
        "template_atendimentos.csv",
        "text/csv"
    )

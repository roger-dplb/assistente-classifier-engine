"""
Streamlit page for analytics reports and dashboard.
"""
import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("📊 Relatórios Analíticos")

st.markdown("Dashboard com métricas e insights dos atendimentos classificados.")

# Filters
st.subheader("🔍 Filtros")
col1, col2 = st.columns(2)

with col1:
    date_range = st.date_input(
        "Período",
        value=[],
        help="Selecione o período de análise"
    )

with col2:
    st.multiselect(
        "Categorias",
        ["Financeiro", "Técnico", "Comercial", "Suporte", "Reclamação", "Dúvida", "Sugestão"],
        default=[]
    )

st.info("📝 O dashboard analítico ainda está sendo implementado.")

# Placeholder charts
st.subheader("📈 Visualizações")

tab1, tab2, tab3 = st.tabs(["Distribuição", "Qualidade", "Tendências"])

with tab1:
    st.markdown("### Distribuição por Categoria")
    st.bar_chart({"Categoria": [1, 2, 3]})  # Placeholder
    
    st.markdown("### Distribuição por Sentimento")
    cols = st.columns(3)
    cols[0].metric("😊 Positivo", "0%")
    cols[1].metric("😐 Neutro", "0%")
    cols[2].metric("😞 Negativo", "0%")

with tab2:
    st.markdown("### Métricas de Qualidade")
    
    metrics_cols = st.columns(4)
    metrics_cols[0].metric("Empatia", "0.0")
    metrics_cols[1].metric("Clareza", "0.0")
    metrics_cols[2].metric("Objetividade", "0.0")
    metrics_cols[3].metric("Resolutividade", "0.0")
    
    st.markdown("### Score Final Médio")
    st.line_chart({"Score": [5, 5, 5, 5]})  # Placeholder

with tab3:
    st.markdown("### Tendência de Sentimento")
    st.area_chart({"Positivo": [1], "Neutro": [1], "Negativo": [1]})
    
    st.markdown("### Tópicos Mais Frequentes")
    st.write("- Nenhum dado disponível")

# Export section
st.markdown("---")
st.subheader("💾 Exportação")

col_exp1, col_exp2, col_exp3 = st.columns(3)

with col_exp1:
    st.button("⬇️ Exportar JSON", use_container_width=True)

with col_exp2:
    st.button("⬇️ Exportar CSV", use_container_width=True)

with col_exp3:
    st.button("⬇️ Exportar PDF", use_container_width=True, disabled=True)

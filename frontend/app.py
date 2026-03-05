"""
Main Streamlit application entry point.
"""
import streamlit as st

st.set_page_config(
    page_title="Sistema de Autoetiquetagem",
    page_icon="🏷️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏷️ Sistema de Autoetiquetagem Inteligente")

st.markdown("""
## Bem-vindo ao Sistema de Classificação de Atendimentos

Este sistema utiliza **Inteligência Artificial (LLM)** para classificar automaticamente 
atendimentos ao cliente, avaliar a qualidade das interações e gerar insights analíticos.

### 🚀 Funcionalidades

- **Classificação Automática**: Categorização por tema, intenção, sentimento e criticidade
- **Avaliação de Qualidade**: Scores de empatia, clareza, objetividade e resolutividade
- **Resumos Inteligentes**: Geração automática de resumos executivos e tópicos
- **Validação Humana**: Interface para revisão e correção de classificações
- **Relatórios Analíticos**: Dashboard com métricas e tendências

### 📋 Navegação

Use o menu lateral para acessar:

1. **🏷️ Classificar** - Análise individual de atendimentos
2. **📁 Processar Lote** - Upload e processamento em massa
3. **✅ Validação** - Revisão humana das classificações
4. **📊 Relatórios** - Dashboard analítico

### 📖 Como Usar

1. Configure sua API Key da OpenAI no arquivo `.env`
2. Inicie a API: `uvicorn api.main:app --reload`
3. Execute o frontend: `streamlit run frontend/app.py`
4. Acesse http://localhost:8501

---

**Status do Sistema**: 🟢 Online | **Versão**: 1.0.0
""")

# Sidebar navigation
st.sidebar.title("Navegação")
st.sidebar.info("Selecione uma página no menu acima.")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔗 Links Úteis")
st.sidebar.markdown("- [Documentação API](http://localhost:8000/docs)")
st.sidebar.markdown("- [Repositório](#)")
st.sidebar.markdown("- [PRD](./prd.md)")

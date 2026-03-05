"""
Streamlit page for human validation.
"""
import streamlit as st

st.title("✅ Validação Humana")

st.markdown("Revisão e correção das classificações automáticas.")

st.info("📝 Esta funcionalidade está em desenvolvimento.")

st.markdown("""
### Funcionalidades Planejadas:

1. **📋 Lista de Atendimentos Pendentes**
   - Ver atendimentos classificados automaticamente
   - Filtrar por confiança baixa do modelo
   - Ordenar por criticidade

2. **🔍 Interface de Revisão**
   - Comparar classificação automática vs. correção
   - Editar cada campo da taxonomia
   - Adicionar notas de revisão

3. **📊 Métricas de Divergência**
   - Taxa de concordância humano vs. IA
   - Campos mais corrigidos
   - Tendências de erro do modelo

4. **💾 Exportação**
   - Exportar golden dataset atualizado
   - Log de todas as correções
""")

# Placeholder for stats
st.subheader("📈 Estatísticas de Validação")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Pendentes", "0", "+")
col2.metric("Validados", "0", "+")
col3.metric("Taxa Concordância", "0%")
col4.metric("Correções", "0")

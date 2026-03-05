"""
Streamlit page for single interaction classification.
"""
import streamlit as st
import requests
import json

API_URL = "http://localhost:8000"

st.title("🏷️ Classificar Atendimento")

st.markdown("Classifique um atendimento individual usando o motor de IA.")

# Input section
st.subheader("📝 Texto do Atendimento")

texto = st.text_area(
    "Cole o texto da conversa ou atendimento:",
    height=200,
    placeholder="Ex: Cliente: Olá, fui cobrado duas vezes no meu cartão...\nAtendente: Olá! Vou verificar..."
)

if st.button("🔍 Classificar", type="primary", use_container_width=True):
    if not texto.strip():
        st.warning("⚠️ Por favor, insira o texto do atendimento.")
    else:
        with st.spinner("Processando com IA..."):
            try:
                response = requests.post(
                    f"{API_URL}/classify/",
                    json={"texto": texto},
                    timeout=30
                )
                
                if response.status_code == 200:
                    result = response.json()
                    
                    if result.get("success"):
                        data = result["data"]
                        
                        st.success("✅ Classificação concluída!")
                        
                        # Display results in columns
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.subheader("🏷️ Etiquetas")
                            st.write(f"**Categoria:** {data['categoria']}")
                            st.write(f"**Intenção:** {data['intencao']}")
                            
                            sentimento = data['sentimento']
                            emoji = "😊" if sentimento == "Positivo" else "😐" if sentimento == "Neutro" else "😞"
                            st.write(f"**Sentimento:** {emoji} {sentimento}")
                            
                            criticidade = data['criticidade']
                            color = "green" if criticidade == "Baixa" else "orange" if criticidade == "Média" else "red"
                            st.write(f"**Criticidade:** :{color}[{criticidade}]")
                            st.write(f"**SLA/Urgência:** {data['sla_urgencia']}")
                        
                        with col2:
                            st.subheader("⭐ Qualidade do Atendimento")
                            qualidade = data['qualidade']
                            
                            st.write(f"**Empatia:** {qualidade['empatia']}/10")
                            st.write(f"**Clareza:** {qualidade['clareza']}/10")
                            st.write(f"**Objetividade:** {qualidade['objetividade']}/10")
                            st.write(f"**Resolutividade:** {qualidade['resolutividade']}/10")
                            
                            score = qualidade['score_final']
                            st.metric("**Score Final**", f"{score}/10")
                        
                        # Summary and topics
                        st.subheader("📝 Resumo")
                        st.write(data['resumo'])
                        
                        st.subheader("🔑 Tópicos Principais")
                        for topico in data['topicos']:
                            st.markdown(f"- {topico}")
                        
                        # JSON output
                        with st.expander("📄 Ver JSON Completo"):
                            st.json(data)
                        
                        # Processing time
                        if result.get("processing_time_ms"):
                            st.caption(f"⏱️ Tempo de processamento: {result['processing_time_ms']}ms")
                    else:
                        st.error(f"❌ Erro na classificação: {result.get('error', 'Erro desconhecido')}")
                else:
                    st.error(f"❌ Erro na API: {response.status_code}")
                    
            except requests.exceptions.ConnectionError:
                st.error("❌ Não foi possível conectar à API. Verifique se o servidor está rodando em http://localhost:8000")
            except Exception as e:
                st.error(f"❌ Erro: {str(e)}")

st.markdown("---")
st.caption("💡 Dica: Para melhores resultados, inclua toda a conversa entre cliente e atendente.")

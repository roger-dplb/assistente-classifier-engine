"""
UI helper components for Streamlit frontend.
"""
import streamlit as st


def render_classification_card(data: dict):
    """
    Render a classification result card.
    
    Args:
        data: Classification result dictionary
    """
    sentimento = data.get('sentimento', 'Neutro')
    emoji = "😊" if sentimento == "Positivo" else "😐" if sentimento == "Neutro" else "😞"
    
    st.markdown(f"""
    <div style="padding: 1rem; border: 1px solid #ddd; border-radius: 0.5rem; margin-bottom: 1rem;">
        <h4>🏷️ {data.get('categoria', 'N/A')}</h4>
        <p><strong>Intenção:</strong> {data.get('intencao', 'N/A')}</p>
        <p><strong>Sentimento:</strong> {emoji} {sentimento}</p>
        <p><strong>Criticidade:</strong> {data.get('criticidade', 'N/A')}</p>
        <p><strong>SLA:</strong> {data.get('sla_urgencia', 'N/A')}</p>
    </div>
    """, unsafe_allow_html=True)


def render_quality_badge(score: float):
    """
    Render a quality score badge with color.
    
    Args:
        score: Quality score (0-10)
    """
    if score >= 8:
        color = "#28a745"
        label = "Excelente"
    elif score >= 6:
        color = "#ffc107"
        label = "Bom"
    elif score >= 4:
        color = "#fd7e14"
        label = "Regular"
    else:
        color = "#dc3545"
        label = "Precisa Melhorar"
    
    st.markdown(f"""
    <div style="display: inline-block; padding: 0.25rem 0.5rem; 
                background-color: {color}; color: white; 
                border-radius: 0.25rem; font-weight: bold;">
        {score}/10 - {label}
    </div>
    """, unsafe_allow_html=True)


def show_api_error(error_message: str):
    """Show API error message."""
    st.error(f"❌ Erro de API: {error_message}")


def show_success_message(message: str):
    """Show success message."""
    st.success(f"✅ {message}")


def format_processing_time(ms: int) -> str:
    """Format processing time for display."""
    if ms < 1000:
        return f"{ms}ms"
    else:
        return f"{ms/1000:.1f}s"

"""
Classification service - main business logic for auto-tagging.
"""
from api.models.classification import ClassificationResult, QualityMetrics
from api.services.llm import generate_structured_output
from core.prompts import get_classification_prompt


async def classify_interaction(texto: str) -> ClassificationResult:
    """
    Classify a customer service interaction using LLM.
    
    Args:
        texto: Raw text of the customer service interaction
        
    Returns:
        ClassificationResult with all tags, quality metrics, and summary
        
    Raises:
        Exception: If classification fails
    """
    # Build the prompt
    prompt = get_classification_prompt(texto)
    
    # Call LLM with structured output
    try:
        result_dict = await generate_structured_output(prompt)
        
        # Parse quality metrics
        qualidade_dict = result_dict.get("qualidade", {})
        qualidade = QualityMetrics(
            empatia=qualidade_dict.get("empatia", 5),
            clareza=qualidade_dict.get("clareza", 5),
            objetividade=qualidade_dict.get("objetividade", 5),
            resolutividade=qualidade_dict.get("resolutividade", 5),
            score_final=qualidade_dict.get("score_final", 5.0)
        )
        
        # Build final result
        return ClassificationResult(
            categoria=result_dict.get("categoria", "Não classificado"),
            intencao=result_dict.get("intencao", "Não identificada"),
            sentimento=result_dict.get("sentimento", "Neutro"),
            criticidade=result_dict.get("criticidade", "Média"),
            sla_urgencia=result_dict.get("sla_urgencia", "48h"),
            qualidade=qualidade,
            resumo=result_dict.get("resumo", ""),
            topicos=result_dict.get("topicos", [])
        )
        
    except Exception as e:
        raise Exception(f"Classification failed: {str(e)}")

"""
Tests for classifier service.
"""
import pytest
from api.models.classification import ClassificationResult, QualityMetrics
from api.services.classifier import classify_interaction
from core.taxonomy import calcular_score_final, validar_classificacao


def test_calcular_score_final():
    """Test quality score calculation."""
    score = calcular_score_final(8, 8, 8, 8)
    assert score == 8.0
    
    score = calcular_score_final(10, 5, 5, 5)
    assert score == 6.25


def test_validar_classificacao_valid():
    """Test validation with valid values."""
    assert validar_classificacao(
        "Financeiro",
        "Solicitação de reembolso",
        "Negativo",
        "Alta"
    ) is True


def test_validar_classificacao_invalid():
    """Test validation with invalid values."""
    assert validar_classificacao(
        "Categoria Inexistente",
        "Intenção Inexistente",
        "Sentimento Inexistente",
        "Criticidade Inexistente"
    ) is False


def test_quality_metrics_model():
    """Test QualityMetrics Pydantic model."""
    metrics = QualityMetrics(
        empatia=7,
        clareza=8,
        objetividade=9,
        resolutividade=6,
        score_final=7.5
    )
    assert metrics.empatia == 7
    assert metrics.score_final == 7.5


def test_classification_result_model():
    """Test ClassificationResult Pydantic model."""
    qualidade = QualityMetrics(
        empatia=7, clareza=8, objetividade=9, resolutividade=6, score_final=7.5
    )
    
    result = ClassificationResult(
        categoria="Financeiro",
        intencao="Solicitação de reembolso",
        sentimento="Negativo",
        criticidade="Alta",
        sla_urgencia="24h",
        qualidade=qualidade,
        resumo="Cliente solicitou reembolso...",
        topicos=["Cobrança duplicada"]
    )
    
    assert result.categoria == "Financeiro"
    assert result.qualidade.score_final == 7.5


@pytest.mark.skip(reason="Requires OpenAI API key")
@pytest.mark.asyncio
async def test_classify_interaction():
    """Test classification with real LLM call."""
    texto = "Cliente solicitou reembolso por cobrança duplicada no cartão."
    result = await classify_interaction(texto)
    
    assert isinstance(result, ClassificationResult)
    assert result.categoria is not None
    assert result.qualidade.score_final >= 0
    assert result.qualidade.score_final <= 10

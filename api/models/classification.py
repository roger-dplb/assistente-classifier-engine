"""
Pydantic models for classification responses.
"""
from pydantic import BaseModel, Field
from typing import List


class QualityMetrics(BaseModel):
    """Quality assessment metrics for a customer service interaction."""
    empatia: int = Field(..., ge=0, le=10, description="Empathy score (0-10)")
    clareza: int = Field(..., ge=0, le=10, description="Clarity score (0-10)")
    objetividade: int = Field(..., ge=0, le=10, description="Objectivity score (0-10)")
    resolutividade: int = Field(..., ge=0, le=10, description="Resolution effectiveness (0-10)")
    score_final: float = Field(..., ge=0, le=10, description="Weighted final quality score")


class ClassificationResult(BaseModel):
    """Complete classification result for a customer service interaction."""
    categoria: str = Field(..., description="Main category of the interaction")
    intencao: str = Field(..., description="Customer intent")
    sentimento: str = Field(..., description="Sentiment: Positivo, Neutro, or Negativo")
    criticidade: str = Field(..., description="Urgency/Impact level")
    sla_urgencia: str = Field(..., description="Expected resolution timeframe")
    qualidade: QualityMetrics = Field(..., description="Quality assessment")
    resumo: str = Field(..., description="Executive summary (max 5 lines)")
    topicos: List[str] = Field(..., description="Key topics addressed")


class ClassificationResponse(BaseModel):
    """API response wrapper for classification."""
    success: bool
    data: ClassificationResult | None = None
    error: str | None = None
    processing_time_ms: int | None = None

"""
Pydantic models for API requests.
"""
from pydantic import BaseModel, Field
from typing import List, Optional


class ClassifyRequest(BaseModel):
    """Request to classify a single customer service interaction."""
    texto: str = Field(..., min_length=1, description="Raw text of the interaction")
    metadata: Optional[dict] = Field(default=None, description="Optional metadata")


class BatchItem(BaseModel):
    """Single item in a batch classification request."""
    id: str = Field(..., description="Unique identifier")
    texto: str = Field(..., min_length=1, description="Raw text of the interaction")
    metadata: Optional[dict] = Field(default=None, description="Optional metadata")


class BatchRequest(BaseModel):
    """Request to classify multiple interactions."""
    items: List[BatchItem] = Field(..., min_length=1, max_length=1000)


class ValidationRequest(BaseModel):
    """Request to validate/correct a classification."""
    classification_id: str = Field(..., description="ID of the classification")
    corrected_data: dict = Field(..., description="Corrected classification data")
    reason: Optional[str] = Field(default=None, description="Reason for correction")

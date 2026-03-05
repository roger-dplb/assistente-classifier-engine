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


class BatchItemResult(BaseModel):
    """Result for a single batch item."""
    id: str = Field(..., description="Unique identifier")
    success: bool = Field(..., description="Whether classification succeeded")
    data: Optional[dict] = Field(default=None, description="Classification result if successful")
    error: Optional[str] = Field(default=None, description="Error message if failed")


class BatchResponse(BaseModel):
    """Response for batch classification."""
    success: bool = Field(..., description="Whether batch processing completed")
    processed: int = Field(..., description="Number of items processed")
    results: List[BatchItemResult] = Field(..., description="Results for each item")
    processing_time_ms: int = Field(..., description="Total processing time in milliseconds")

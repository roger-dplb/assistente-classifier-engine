"""
Routes for single classification requests.
"""
from fastapi import APIRouter, HTTPException
import time

from api.models.requests import ClassifyRequest
from api.models.classification import ClassificationResponse
from api.services.classifier import classify_interaction

router = APIRouter()


@router.post("/", response_model=ClassificationResponse)
async def classify(request: ClassifyRequest):
    """
    Classify a single customer service interaction.
    
    Returns full classification with category, sentiment, quality metrics, and summary.
    """
    start_time = time.time()
    
    try:
        result = await classify_interaction(request.texto)
        processing_time = int((time.time() - start_time) * 1000)
        
        return ClassificationResponse(
            success=True,
            data=result,
            processing_time_ms=processing_time
        )
    except Exception as e:
        return ClassificationResponse(
            success=False,
            error=str(e),
            processing_time_ms=int((time.time() - start_time) * 1000)
        )

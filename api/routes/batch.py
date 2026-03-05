"""
Routes for batch processing requests.
"""
from fastapi import APIRouter, UploadFile, File, Form
from typing import List
import time

from api.models.requests import BatchRequest, BatchResponse, BatchItemResult
from api.models.classification import ClassificationResponse
from api.services.classifier import classify_interaction

router = APIRouter()


@router.post("/")
async def batch_classify(
    file: UploadFile = File(None),
    format: str = Form("json")
):
    """
    Process a batch of customer service interactions from uploaded file.
    
    Supports CSV and JSON file formats.
    """
    # TODO: Implement file parsing and batch processing
    return {"message": "Batch processing endpoint - implementação pendente"}


@router.post("/items", response_model=BatchResponse)
async def batch_classify_items(request: BatchRequest) -> BatchResponse:
    """
    Process a batch of interactions provided directly in the request body.
    
    Maximum 1000 items per request.
    """
    start_time = time.time()
    results = []
    
    for item in request.items:
        try:
            result = await classify_interaction(item.texto)
            results.append(BatchItemResult(
                id=item.id,
                success=True,
                data=result
            ))
        except Exception as e:
            results.append(BatchItemResult(
                id=item.id,
                success=False,
                error=str(e)
            ))
    
    return BatchResponse(
        success=True,
        processed=len(results),
        results=results,
        processing_time_ms=int((time.time() - start_time) * 1000)
    )

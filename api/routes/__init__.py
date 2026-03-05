"""API routes package."""
from .batch import router as batch_router
from .classify import router as classify_router
from .reports import router as reports_router

__all__ = ["batch_router", "classify_router", "reports_router"]
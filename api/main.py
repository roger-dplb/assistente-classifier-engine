"""
Main entry point for FastAPI application.
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from api.routes import classify, batch, reports
from api.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan events for startup and shutdown."""
    # TODO: Implement startup logic (e.g., initialize resources, load models)
    yield
    # TODO: Implement shutdown logic (e.g., cleanup resources)


app = FastAPI(
    title="Sistema de Autoetiquetagem Inteligente",
    description="API para classificação automática de atendimentos usando LLM",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(classify.router, prefix="/api/v1/classify", tags=["Classificação"])
app.include_router(batch.router, prefix="/api/v1/batch", tags=["Processamento em Lote"])
app.include_router(reports.router, prefix="/api/v1/reports", tags=["Relatórios"])


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler for unhandled exceptions."""
    # TODO: Add logging for production
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "success": False}
    )


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "version": "1.0.0"}


@app.get("/")
def root():
    """Root endpoint with API info."""
    return {
        "name": "Sistema de Autoetiquetagem Inteligente",
        "version": "1.0.0",
        "docs": "/docs"
    }

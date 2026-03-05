"""
Main entry point for FastAPI application.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import classify, batch, reports
from api.core.config import settings

app = FastAPI(
    title="Sistema de Autoetiquetagem Inteligente",
    description="API para classificação automática de atendimentos usando LLM",
    version="1.0.0"
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
app.include_router(classify.router, prefix="/classify", tags=["Classificação"])
app.include_router(batch.router, prefix="/batch", tags=["Processamento em Lote"])
app.include_router(reports.router, prefix="/reports", tags=["Relatórios"])


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

"""
Tests for API endpoints.
"""
import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_health_check():
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_root():
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert "name" in response.json()
    assert "docs" in response.json()


@pytest.mark.skip(reason="Requires OpenAI API key")
def test_classify_endpoint():
    """Test classification endpoint."""
    payload = {
        "texto": "Cliente solicitou reembolso por cobrança duplicada."
    }
    response = client.post("/classify/", json=payload)
    assert response.status_code == 200
    result = response.json()
    assert "success" in result


def test_classify_empty_text():
    """Test classification with empty text returns error."""
    payload = {"texto": ""}
    response = client.post("/classify/", json=payload)
    assert response.status_code == 422  # Validation error


def test_reports_endpoints_exist():
    """Test that report endpoints exist."""
    endpoints = [
        "/reports/distribution",
        "/reports/quality",
        "/reports/sentiment-trend",
        "/reports/topics"
    ]
    
    for endpoint in endpoints:
        response = client.get(endpoint)
        assert response.status_code in [200, 422]  # 422 if query params required

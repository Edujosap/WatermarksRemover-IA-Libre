"""MCP adapter for a locally running Watermarks Remover service."""
import os
import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

BASE_URL = os.getenv("WMR_BASE_URL", "http://127.0.0.1:8765").rstrip("/")
API_KEY = os.getenv("WMR_API_KEY", "")
TIMEOUT = float(os.getenv("WMR_TIMEOUT", "60"))

mcp = FastMCP("watermarks-remover-local")


def _request(method: str, endpoint: str, payload: dict | None = None):
    headers = {}
    if API_KEY:
        headers["Authorization"] = f"Bearer {API_KEY}"
    try:
        with httpx.Client(timeout=TIMEOUT) as client:
            response = client.request(
                method, f"{BASE_URL}/{endpoint.lstrip('/')}",
                json=payload if method.upper() != "GET" else None,
                headers=headers,
            )
            response.raise_for_status()
            try:
                return response.json()
            except ValueError:
                return {"text": response.text}
    except httpx.HTTPError as exc:
        return {"error": str(exc), "endpoint": endpoint}


@mcp.tool()
def service_health() -> dict:
    """Comprueba si el servicio local responde en /health."""
    return _request("GET", "/health")


@mcp.tool()
def service_capabilities() -> dict:
    """Consulta las capacidades declaradas por el servicio local."""
    return _request("GET", "/capabilities")


@mcp.tool()
def inspect_content(payload: dict) -> dict:
    """Envía un objeto JSON al endpoint /inspect. Usar solo contenido autorizado."""
    return _request("POST", "/inspect", payload)


@mcp.tool()
def detect_marks(payload: dict) -> dict:
    """Envía un objeto JSON al endpoint /detect. Usar solo contenido autorizado."""
    return _request("POST", "/detect", payload)


@mcp.tool()
def clean_content(payload: dict) -> dict:
    """Envía un objeto JSON al endpoint /clean. Usar solo contenido propio o autorizado."""
    return _request("POST", "/clean", payload)


if __name__ == "__main__":
    mcp.run(transport="stdio")

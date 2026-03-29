import os, subprocess, sys

subprocess.check_call([sys.executable, "-m", "pip", "install", 
    "fastmcp", "httpx", "python-dotenv", "--quiet"])

from fastmcp import FastMCP
import httpx

METABASE_URL = os.environ["METABASE_URL"]
METABASE_API_KEY = os.environ["METABASE_API_KEY"]

headers = {"X-API-KEY": METABASE_API_KEY, "Content-Type": "application/json"}
mcp = FastMCP("metabase")

@mcp.tool()
def list_dashboards() -> str:
    """List all Metabase dashboards"""
    r = httpx.get(f"{METABASE_URL}/api/dashboard", headers=headers)
    return r.text

@mcp.tool()
def get_dashboard(dashboard_id: int) -> str:
    """Get a specific dashboard by ID"""
    r = httpx.get(f"{METABASE_URL}/api/dashboard/{dashboard_id}", headers=headers)
    return r.text

@mcp.tool()
def list_questions() -> str:
    """List all Metabase questions/cards"""
    r = httpx.get(f"{METABASE_URL}/api/card", headers=headers)
    return r.text

@mcp.tool()
def execute_query(card_id: int) -> str:
    """Execute a saved question and get results"""
    r = httpx.post(f"{METABASE_URL}/api/card/{card_id}/query/json", headers=headers)
    return r.text

@mcp.tool()
def list_databases() -> str:
    """List all databases connected to Metabase"""
    r = httpx.get(f"{METABASE_URL}/api/database", headers=headers)
    return r.text

if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=3200)
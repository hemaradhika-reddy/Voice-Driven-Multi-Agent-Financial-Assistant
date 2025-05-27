# tests/test_agents.py
import pytest
from agents.api_agent import APIAgent

def test_api_agent():
    agent = APIAgent(alpha_vantage_key="YOUR_ALPHA_VANTAGE_KEY")
    data = agent.fetch_stock_data("TSM")
    assert "symbol" in data
    assert data["symbol"] == "TSM"
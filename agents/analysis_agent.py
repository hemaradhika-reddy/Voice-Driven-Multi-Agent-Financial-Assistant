# agents/analysis_agent.py
import pandas as pd
import numpy as np

class AnalysisAgent:
    def calculate_risk_exposure(self, portfolio_data, market_data):
        total_aum = portfolio_data['value'].sum()
        asia_tech = portfolio_data[portfolio_data['sector'] == 'Asia Tech']['value'].sum()
        exposure = (asia_tech / total_aum) * 100
        return {"exposure": exposure, "aum": total_aum}

    def detect_earnings_surprise(self, actual_eps, expected_eps):
        surprise = ((actual_eps - expected_eps) / expected_eps) * 100
        return {"surprise": surprise, "actual_eps": actual_eps, "expected_eps": expected_eps}
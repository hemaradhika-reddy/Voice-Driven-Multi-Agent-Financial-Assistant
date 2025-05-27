# streamlit_app/chart_utils.py
import streamlit as st
import json

def display_portfolio_chart(portfolio_data):
    chart_data = {
        "type": "pie",
        "data": {
            "labels": portfolio_data["sector"].tolist(),
            "datasets": [{
                "label": "Portfolio Allocation",
                "data": portfolio_data["value"].tolist(),
                "backgroundColor": ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0", "#9966FF"],
                "borderColor": ["#FFFFFF"] * len(portfolio_data),
                "borderWidth": 1
            }]
        },
        "options": {
            "responsive": True,
            "plugins": {
                "legend": {"position": "top"},
                "title": {"display": True, "text": "Portfolio Allocation by Sector"}
            }
        }
    }
    st.write("### Portfolio Allocation")
    st.write(json.dumps(chart_data), format="chartjs")
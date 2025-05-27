import streamlit as st
import requests
from agents.voice_agent import VoiceAgent
from streamlit_app.chart_utils import display_portfolio_chart
import pandas as pd

st.set_page_config(page_title="Morning Market Brief", layout="wide")
st.markdown("""
    <style>
    .main {background-color: #f0f2f6;}
    .stButton>button {background-color: #4CAF50; color: white;}
    </style>
""", unsafe_allow_html=True)

st.title("Morning Market Brief")
query = st.text_input("Enter your query", "What's our risk exposure in Asia tech stocks today?")
audio_file = st.file_uploader("Or upload a voice query", type=["wav", "mp3"])

if st.button("Get Brief"):
    voice_agent = VoiceAgent()
    if audio_file:
        query_data = voice_agent.speech_to_text(audio_file)
        query = query_data["text"]
        if query_data["fallback"]:
            st.warning(query_data["fallback"])
    
    # Call orchestrator
    response = requests.post("http://localhost:8000/process_query", json={"query": query})
    result = response.json()
    
    st.write("### Market Brief")
    st.write(result["response"])
    st.audio(result["audio"])
    
    # Display chart
    portfolio_data = pd.DataFrame({"sector": ["Asia Tech", "Other"], "value": [result["exposure"]["aum"] * result["exposure"]["exposure"] / 100, result["exposure"]["aum"] * (1 - result["exposure"]["exposure"] / 100)]})
    display_portfolio_chart(portfolio_data)

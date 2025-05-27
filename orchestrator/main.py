
from fastapi import FastAPI
from agents.api_agent import APIAgent
from agents.retriever_agent import RetrieverAgent
from agents.analysis_agent import AnalysisAgent
from agents.language_agent import LanguageAgent
from agents.voice_agent import VoiceAgent

app = FastAPI()

@app.post("/process_query")
async def process_query(query: str):
    api_agent = APIAgent(alpha_vantage_key="YOUR_ALPHA_VANTAGE_KEY")
    retriever_agent = RetrieverAgent()
    analysis_agent = AnalysisAgent()
    language_agent = LanguageAgent(retriever_agent.retrieve)
    voice_agent = VoiceAgent()
    
    # Fetch data
    market_data = api_agent.fetch_stock_data("TSM")
    context = retriever_agent.retrieve(query)
    exposure = analysis_agent.calculate_risk_exposure(pd.DataFrame({"sector": ["Asia Tech"], "value": [220000]}), market_data)
    narrative = language_agent.generate_narrative(query, context)
    audio_file = voice_agent.text_to_speech(narrative)
    
    return {"response": narrative, "audio": audio_file, "exposure": exposure}
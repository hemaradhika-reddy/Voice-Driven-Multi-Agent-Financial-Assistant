# data_ingestion/sentiment_analyzer.py
from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    
    def analyze_sentiment(self, text):
        result = self.analyzer(text)
        return {"label": result[0]["label"], "score": result[0]["score"]}
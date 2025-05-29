# 🧠 Multi-Agent Voice Finance Assistant

An AI-powered, modular system for delivering market briefs via text and voice using microservices.

## 🎯 Use Case
> “What’s our risk exposure in Asia tech stocks today, and highlight any earnings surprises?”

---

## 📦 Architecture
![Alt text](https://github.com/hemaradhika-reddy/finance-assistant/blob/main/Architecture.png)<!-- Use a placeholder or draw.io export -->

### Agent Roles
- **API Agent**: Gets market data using yfinance.
- **Scraper Agent**: Parses earnings from online filings.
- **Retriever Agent**: FAISS-based document search.
- **Language Agent**: LLM (OpenAI) to generate summary.
- **Voice Agent**: Whisper + pyttsx3 or gTTS.

---

## 🚀 Streamlit App

- Upload voice or type a query.
- View simulated API/scraping results.
- Get generated summary + audio playback.

---

## 🧪 Tools Used

| Agent | Tools |
|-------|-------|
| API | yfinance |
| Scraper | BeautifulSoup |
| Retriever | FAISS + SentenceTransformers |
| LLM | OpenAI GPT-3.5 via LangChain |
| Voice | Whisper, pyttsx3 |

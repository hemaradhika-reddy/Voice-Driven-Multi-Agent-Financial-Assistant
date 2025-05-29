# 🧠 Multi-Agent Voice Finance Assistant

An AI-powered, modular system for delivering market briefs via text and voice using microservices.

## 🎯 Use Case
At 8 AM daily, the assistant provides a verbal and textual summary that includes:
- Risk exposure % in Asia tech stocks
- Recent earnings surprises (beats/misses)
- Sentiment or contextual notes (e.g., macroeconomic factors)

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
- This prototype uses Streamlit as a lightweight orchestration layer to coordinate agents and simulate end-to-end flow. In a production setup, this would be handled by an asynchronous FastAPI service for scalability and modularity.


---

## 🧪 Tools Used

| Agent | Tools |
|-------|-------|
| API | yfinance |
| Scraper | BeautifulSoup |
| Retriever | FAISS + SentenceTransformers |
| LLM | OpenAI GPT-3.5 via LangChain |
| Voice | Whisper, pyttsx3 |

## 🚀 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/finance-agent.git
cd finance-agent ```

### 2. Install Dependencies



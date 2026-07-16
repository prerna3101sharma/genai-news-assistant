# 📰 GenAI News Assistant

An intelligent news analysis application built using Large Language Models (LLMs) that helps users quickly understand news articles by generating summaries, analyzing sentiment, extracting important entities and keywords, and answering questions about the selected article.

The application fetches the latest news in real time, extracts the complete article content, and uses an open-source language model to perform various NLP tasks through an interactive Streamlit interface.

---

## ✨ Features

- 🔍 Search the latest news by any topic
- 📰 Read complete news articles
- 📄 Generate concise AI-powered summaries
- 😊 Perform sentiment analysis
- 🏷️ Extract named entities (People, Organizations, Locations, Dates, etc.)
- 🔑 Identify important keywords
- 💬 Ask questions about the selected article using natural language
- 🌐 Interactive and responsive Streamlit interface
- ⚡ Powered by open-source Large Language Models

---

## Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Frontend | Streamlit |
| LLM | Hugging Face Inference API |
| NLP | Prompt Engineering |
| News Source | NewsAPI |
| Article Extraction | Trafilatura + BeautifulSoup |
| Environment | Python Virtual Environment |

---

## Project Structure

```
genai-news-assistant/
│
├── app.py
├── requirements.txt
├── .env
│
├── prompts/
│   ├── summary_prompt.py
│   ├── sentiment_prompt.py
│   ├── entity_prompt.py
│   ├── keyword_prompt.py
│   └── qa_prompt.py
│
├── services/
│   ├── llm.py
│   ├── news_service.py
│   ├── summarizer.py
│   ├── sentiment.py
│   ├── keyword.py
│   ├── entities.py
│   └── qa_engine.py
│
├── utils/
│   └── preprocessing.py
│
└── README.md
```

---

## How It Works

1. Search for any news topic.
2. Fetch the latest articles using NewsAPI.
3. Extract the full article text from the news webpage.
4. Use an open-source LLM to:
   - Generate a summary
   - Detect sentiment
   - Extract entities
   - Extract keywords
   - Answer user questions
5. Display the results in an interactive Streamlit application.

---

## Installation

### Clone the repository

```bash
git clone https://github.com/prerna3101sharma/genai-news-assistant.git

cd genai-news-assistant
```

### Create a virtual environment

```bash
python -m venv myvenv
```

### Activate the environment

**Windows**

```bash
myvenv\Scripts\activate
```

**macOS/Linux**

```bash
source myvenv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
NEWS_API_KEY=your_news_api_key
NEWS_API_ENDPOINT=https://newsapi.org/v2/everything

HF_TOKEN=your_huggingface_token
HF_MODEL=google/gemma-2-2b-it
```

---

## Running the Application

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## Application Preview

The application provides:

- Search latest news
- Read full article
- AI-generated summary
- Sentiment analysis
- Named entity extraction
- Keyword extraction
- Interactive question answering

---

## Future Improvements

- User authentication
- Search history
- Save favourite articles
- Multi-language support
- Voice-based interaction
- RAG-based question answering
- News recommendation system
- Article comparison
- PDF export of analysis

---

## Challenges Faced

During development, several practical challenges were addressed, including:

- Extracting readable text from different news websites
- Handling inconsistent article formats
- Managing structured JSON responses from LLMs
- Improving prompt reliability for entity extraction
- Deploying an LLM-powered Streamlit application using free services
- Optimizing response quality while working within API limits

---

## Learning Outcomes

This project helped strengthen practical understanding of:

- Prompt Engineering
- Large Language Models
- NLP workflows
- API Integration
- Streamlit development
- Python application architecture
- Error handling
- Real-world GenAI application deployment

---

## Author

**Prerna Sharma**

Computer Science Engineering Student

GitHub: https://github.com/prerna3101sharma

LinkedIn: https://www.linkedin.com/in/prerna-sharma-9b78b7228/

# 🏆 AI-Powered Sports Quiz Generator

An interactive Streamlit web app that generates fresh, factually grounded multiple-choice sports quizzes using a Retrieval-Augmented Generation (RAG) pipeline — combining a local ChromaDB knowledge base, live web search, and Google's Gemini API.

## How it works

1. User selects a sport and difficulty from the sidebar.
2. The app retrieves relevant historic facts from a local ChromaDB vector database.
3. The app simultaneously performs a live web search (via DuckDuckGo/ddgs) for recent news on that sport.
4. Both sources are merged into a single grounding context and sent to Gemini with strict instructions to only use the provided facts (no hallucination).
5. Gemini's response is parsed into structured question objects and rendered as interactive, clickable quiz cards with instant right/wrong feedback and a live-updating score tracker.

## Tech stack

| Tool | Purpose |
|---|---|
| Streamlit | Web UI |
| ChromaDB | Local vector database for offline sports facts |
| ddgs (DuckDuckGo Search) | Live web search for recent sports news |
| Google Gemini API (`google-genai`) | Quiz question generation |
| python-dotenv | Secure API key loading |

## Project structure

sports-quiz-agent/
├── .env                  # Your Gemini API key (not committed)
├── .gitignore
├── requirements.txt
├── README.md
├── data/
│   └── sports_facts.json # Offline knowledge base (20 facts across 4 sports)
├── chroma_db/             # Auto-created by ChromaDB on first run
├── src/
│   ├── config.py          # Loads the Gemini API key from .env
│   ├── database.py        # ChromaDB insert/query logic
│   ├── search.py           # Live web search logic (ddgs)
│   ├── generator.py       # RAG orchestration + Gemini API call
│   ├── parser.py           # Parses raw Gemini text output into structured Q&A objects
│   └── styles.py            # Custom UI styling and theming
└── app.py                 # Streamlit entry point

## Setup instructions

1. **Clone/download this project** and open a terminal inside the project folder.

2. **Create and activate a virtual environment:**
```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
```

3. **Install dependencies:**
```bash
   pip install -r requirements.txt
```

4. **Get a free Gemini API key** from [Google AI Studio](https://aistudio.google.com/apikey).

5. **Create a `.env` file** in the project root:
GEMINI_API_KEY=your_actual_key_here

6. **Run the app:**
```bash
   streamlit run app.py
```

7. Open `http://localhost:8501` in your browser (it should open automatically).

## Usage

- Select a sport (Cricket, Football, Badminton, or Tennis) and difficulty (Easy/Medium/Hard) from the sidebar.
- Click "Generate Fresh Quiz."
- Answer each question by selecting an option — you'll get instant feedback (correct/incorrect) plus an explanation grounded in the retrieved facts.
- Expand "Inspect Ground Truth" to see exactly which ChromaDB facts and live web search results were used to generate the quiz — useful for verifying accuracy and absence of hallucination.

## Design decisions

- **Modular file structure**: each file has a single responsibility (database, search, generation, parsing, UI) rather than one large script, for readability and easier debugging.
- **Grounding via RAG**: the LLM is explicitly instructed to answer strictly from retrieved context, minimizing hallucination — the app exposes the exact retrieved context in an "Inspect Ground Truth" panel for transparency and auditability.
- **Graceful fallbacks**: if web search fails (rate limiting, connectivity), the app falls back to ChromaDB facts alone instead of crashing; malformed LLM output is skipped rather than crashing the parser.
- **Interactive UI**: quiz questions render as clickable cards with instant feedback and a live score tracker, rather than plain text, for a better user experience.
- **Provider choice**: the reference material used OpenAI; this implementation uses Google Gemini (`google-genai` SDK) instead, which the reference material explicitly allows as a substitute.

## Known limitations

- Gemini's free-tier API has a daily/rate-based request quota; heavy testing may temporarily produce a `429 RESOURCE_EXHAUSTED` error until the quota resets.
- DuckDuckGo's free search API can occasionally rate-limit; the app handles this gracefully with a fallback message rather than failing.
- The local knowledge base currently covers 4 sports (Cricket, Football, Badminton, Tennis); can be extended by adding more entries to `data/sports_facts.json`.
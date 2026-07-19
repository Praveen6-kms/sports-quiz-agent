CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Inter:wght@400;500;600&display=swap');

/* Force a consistent theme regardless of the user's system light/dark mode */
[data-testid="stAppViewContainer"] {
    background-color: #0f1620;
}
[data-testid="stSidebar"] {
    background-color: #141d2b;
    border-right: 1px solid #263141;
}
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: #e6ecf3;
}

/* ---------- Hero header ---------- */
.main-header {
    background: linear-gradient(135deg, #0f2d4a 0%, #1c4e7c 60%, #2d6ba6 100%);
    padding: 2.5rem 2.5rem 2rem;
    border-radius: 18px;
    margin-bottom: 1.75rem;
    border: 1px solid #2d6ba6;
}
.main-header h1 {
    font-family: 'Poppins', sans-serif;
    color: #ffffff;
    margin: 0;
    font-size: 2.1rem;
    font-weight: 700;
    letter-spacing: -0.5px;
}
.main-header p {
    color: #b9d3ea;
    margin: 0.6rem 0 0 0;
    font-size: 1rem;
}
.main-header .tags {
    margin-top: 1rem;
}
.tag-chip {
    display: inline-block;
    background: rgba(255,255,255,0.12);
    color: #d9ebfa;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 500;
    margin-right: 8px;
}

/* ---------- Sidebar ---------- */
[data-testid="stSidebar"] h2, [data-testid="stSidebar"] label {
    color: #e6ecf3 !important;
    font-weight: 600;
}
[data-testid="stSidebar"] .stButton button {
    background: linear-gradient(135deg, #2d6ba6, #3a86c8);
    color: white;
    font-weight: 600;
    border: none;
    border-radius: 10px;
    padding: 0.6rem 0;
    transition: transform 0.1s ease;
}
[data-testid="stSidebar"] .stButton button:hover {
    transform: translateY(-1px);
    background: linear-gradient(135deg, #3a86c8, #4d99db);
}

/* ---------- Difficulty badge ---------- */
.difficulty-badge {
    display: inline-block;
    padding: 4px 14px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    color: white;
    margin-left: 10px;
    vertical-align: middle;
}
.badge-easy { background-color: #2e9e5b; }
.badge-medium { background-color: #d68a1c; }
.badge-hard { background-color: #d13b3b; }

.quiz-title {
    font-family: 'Poppins', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: #ffffff;
    margin: 0.5rem 0 1rem 0;
}

/* ---------- Score card ---------- */
.score-card {
    background: #141d2b;
    border: 1px solid #263141;
    border-radius: 14px;
    padding: 1.1rem 1.6rem;
    margin-bottom: 1.5rem;
    display: flex;
    justify-content: space-around;
    align-items: center;
}
.score-number {
    font-family: 'Poppins', sans-serif;
    font-size: 1.9rem;
    font-weight: 700;
    color: #4d99db;
    text-align: center;
}
.score-label {
    font-size: 0.82rem;
    color: #8fa3ba;
    text-align: center;
    margin-top: 2px;
}

/* ---------- Question card ---------- */
.question-card {
    background: #141d2b;
    border: 1px solid #263141;
    border-radius: 14px;
    padding: 1.3rem 1.5rem 0.6rem;
    margin-bottom: 0.5rem;
}
.question-card strong {
    color: #f2f5f8;
    font-size: 1.02rem;
    line-height: 1.5;
}
.question-number {
    display: inline-block;
    background: linear-gradient(135deg, #2d6ba6, #4d99db);
    color: white;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    text-align: center;
    line-height: 28px;
    font-size: 0.85rem;
    font-weight: 700;
    margin-right: 12px;
}

/* Radio options readability */
[data-testid="stRadio"] label p {
    color: #dbe4ee !important;
    font-size: 0.95rem;
}

/* ---------- Footer ---------- */
.app-footer {
    text-align: center;
    color: #5c6b80;
    font-size: 0.8rem;
    margin-top: 2.5rem;
    padding-top: 1.2rem;
    border-top: 1px solid #263141;
}
</style>
"""

SPORT_ICONS = {
    "Cricket": "🏏",
    "Football": "⚽",
    "Badminton": "🏸",
    "Tennis": "🎾",
}

DIFFICULTY_BADGE_CLASS = {
    "Easy": "badge-easy",
    "Medium": "badge-medium",
    "Hard": "badge-hard",
}
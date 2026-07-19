import streamlit as st
from src.generator import compile_quiz_data
from src.database import setup_and_populate_db
from src.parser import parse_quiz_text
from src.styles import CUSTOM_CSS, SPORT_ICONS, DIFFICULTY_BADGE_CLASS

# 1. Warm-up and initialize the vector DB with our offline facts on startup
@st.cache_resource
def prepare_knowledge_base():
    setup_and_populate_db()

prepare_knowledge_base()

# 2. Page configuration + global styles
st.set_page_config(page_title="Sports Quiz Agent", page_icon="🏆", layout="centered")
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# 3. Hero header
st.markdown(
    """
    <div class="main-header">
        <h1>🏆 AI-Powered Sports Quiz Generator</h1>
        <p>Grounded, hallucination-free quiz questions — powered by RAG (ChromaDB knowledge + live web search + Gemini).</p>
        <div class="tags">
            <span class="tag-chip">🔎 ChromaDB retrieval</span>
            <span class="tag-chip">🌐 Live web search</span>
            <span class="tag-chip">✨ Gemini-generated</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# 4. Sidebar inputs
st.sidebar.header("Quiz Settings")
sport_choice = st.sidebar.selectbox("Select Sport", ["Cricket", "Football", "Badminton", "Tennis"])
difficulty = st.sidebar.select_slider("Select Difficulty", options=["Easy", "Medium", "Hard"])

# 5. Session state initialization
if "quiz_questions" not in st.session_state:
    st.session_state.quiz_questions = None
    st.session_state.quiz_context = None
    st.session_state.user_answers = {}

# 6. Generate button
if st.sidebar.button("Generate Fresh Quiz", use_container_width=True):
    with st.spinner("Fetching historical facts & scouring the live web..."):
        try:
            quiz_text, context_used = compile_quiz_data(sport_choice, difficulty)
            parsed = parse_quiz_text(quiz_text)

            if not parsed:
                st.error("Gemini's response couldn't be parsed into questions. Try generating again.")
            else:
                st.session_state.quiz_questions = parsed
                st.session_state.quiz_context = context_used
                st.session_state.user_answers = {}
        except Exception as e:
            st.error(f"Failed to generate quiz: {e}")

# 7. Display the generated quiz as interactive cards
if st.session_state.quiz_questions:
    icon = SPORT_ICONS.get(sport_choice, "🏆")
    badge_class = DIFFICULTY_BADGE_CLASS.get(difficulty, "badge-medium")

    st.markdown(
        f"<div class='quiz-title'>{icon} {sport_choice} Quiz "
        f"<span class='difficulty-badge {badge_class}'>{difficulty}</span></div>",
        unsafe_allow_html=True,
    )

    total = len(st.session_state.quiz_questions)

    # Sync answers from widget state FIRST — Streamlit already updated
    # st.session_state[f"radio_{idx}"] for this rerun before we get here,
    # so reading it now (before drawing the score card) keeps counts accurate.
    for idx in range(total):
        widget_key = f"radio_{idx}"
        if widget_key in st.session_state and st.session_state[widget_key] is not None:
            st.session_state.user_answers[idx] = st.session_state[widget_key]

    answered = len(st.session_state.user_answers)
    correct = sum(
        1 for idx, ans in st.session_state.user_answers.items()
        if ans == st.session_state.quiz_questions[idx]["correct"]
    )

    st.markdown(
        f"""
        <div class="score-card">
            <div><div class="score-number">{total}</div><div class="score-label">Questions</div></div>
            <div><div class="score-number">{answered}/{total}</div><div class="score-label">Answered</div></div>
            <div><div class="score-number">{correct}/{total}</div><div class="score-label">Correct</div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for idx, q in enumerate(st.session_state.quiz_questions):
        st.markdown(
            f"""<div class="question-card">
                <span class="question-number">{idx + 1}</span>
                <strong>{q['question']}</strong>
            </div>""",
            unsafe_allow_html=True,
        )

        selected = st.radio(
            "Choose an answer:",
            options=list(q["options"].keys()),
            format_func=lambda key, opts=q["options"]: f"{key}) {opts[key]}",
            key=f"radio_{idx}",
            index=None,
            label_visibility="collapsed",
        )

        if selected:
            st.session_state.user_answers[idx] = selected

        if idx in st.session_state.user_answers:
            chosen = st.session_state.user_answers[idx]
            if chosen == q["correct"]:
                st.success(f"✅ Correct! Answer: {q['correct']}) {q['options'][q['correct']]}")
            else:
                st.error(f"❌ Incorrect. You chose {chosen}. Correct answer: {q['correct']}) {q['options'][q['correct']]}")
            st.info(f"**Explanation:** {q['explanation']}")

        st.write("")

    with st.expander("🔍 Inspect Ground Truth (RAG Context Used)"):
        st.code(st.session_state.quiz_context, language="markdown")

# 8. Footer
st.markdown(
    "<div class='app-footer'>Built with Streamlit · ChromaDB · Gemini · DuckDuckGo Search</div>",
    unsafe_allow_html=True,
)
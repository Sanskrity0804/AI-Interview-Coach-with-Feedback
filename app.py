import streamlit as st
import json
from answer_evaluator import evaluate_answer
from pathlib import Path

# Load questions from JSON
@st.cache_data
def load_questions():
    with open("interview_questions_full.json", "r") as file:
        return json.load(file)

questions = load_questions()
topics = list(questions.keys())

# Streamlit UI
st.set_page_config(page_title="AI Interview Coach", layout="centered")
st.title("🧠 AI Interview Coach")
st.markdown("Practice technical interview questions and get instant feedback!")

# Topic selection
selected_topic = st.selectbox("Choose a topic", topics)
question_list = questions[selected_topic]

# Session state to track question index
if "question_index" not in st.session_state:
    st.session_state.question_index = 0

# Display question
current_question = question_list[st.session_state.question_index]
st.subheader(f"Q: {current_question}")

# Input area for user's answer
user_answer = st.text_area("Your Answer", height=200)

if st.button("Submit Answer"):
    if user_answer.strip():
        feedback = evaluate_answer(user_answer, current_question)
        st.markdown("### 📝 Feedback:")
        st.write(feedback)
    else:
        st.warning("Please enter an answer before submitting.")

if st.button("Next Question"):
    if st.session_state.question_index < len(question_list) - 1:
        st.session_state.question_index += 1
    else:
        st.success("You have completed all questions in this topic!")

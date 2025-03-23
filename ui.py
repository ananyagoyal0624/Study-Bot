import streamlit as st
from pdf_to_quizz import pdf_to_quizz
from text_to_quizz import txt_to_quizz
from generate_pdf import generate_pdf_quiz
import json
import asyncio

st.title("PDF to Quiz (:-)(-: )")

def build_question(count, json_question):
    if json_question.get("question") is not None:
        st.write("Question:", json_question.get("question", ""))
        choices = ['A', 'B', 'C', 'D']
        selected_answer = st.selectbox(f"Select your answer:", choices, key=f"select_{count}")
        for choice in choices:
            choice_str = json_question.get(choice, "None")
            st.write(f"{choice}: {choice_str}")
                    
        color = ""
        if st.button("Submit", key=f"button_{count}"):
            correct_answer = json_question.get("reponse")
            if selected_answer == correct_answer:
                color = ":green"
                st.write(f":green[Correct Answer: {correct_answer}]")
            else:
                color = ":red"
                st.write(f":red[Incorrect. Correct Answer: {correct_answer}].")                

        st.write(f"{color}[Your Answer: {selected_answer}]")

        count += 1

    return count

# Upload PDF file
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
txt = st.text_area('Enter text to generate a quiz')

if st.button("Generate Quiz", key="button_generate"):
    if txt.strip():
        with st.spinner("Generating quiz..."):
            st.session_state['questions'] = asyncio.run(txt_to_quizz(txt))
            st.write("Quiz generated successfully!")

import os
import streamlit as st
import asyncio

if uploaded_file is not None:
    old_file_name = st.session_state.get('uploaded_file_name', None)

    # Agar naye file ka naam purane se alag hai, tabhi process karo
    if old_file_name != uploaded_file.name:
        with st.spinner("Generating quiz..."):
            try:
                # Ensure "data" folder exists
                os.makedirs("data", exist_ok=True)

                # Save uploaded file
                file_path = f"data/{uploaded_file.name}"
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getvalue())

                # Update session state
                st.session_state['uploaded_file_name'] = uploaded_file.name

                # Process PDF to generate quiz
                st.session_state['questions'] = asyncio.run(pdf_to_quizz(file_path))

                st.success("Quiz generated successfully!")

            except Exception as e:
                st.error(f"An error occurred while processing the PDF: {e}")


if 'questions' in st.session_state:
    count = 0
    for json_question in st.session_state['questions']:
        count = build_question(count, json_question)  # Fixed issue

# Generate PDF quiz
if st.button("Generate PDF Quiz", key="button_generate_pdf"):
    if 'questions' in st.session_state:
        with st.spinner("Generating quiz PDF..."):
            json_questions = st.session_state['questions']
            file_name = uploaded_file.name if uploaded_file else "quiz"

            # Remove .pdf extension if present
            if file_name.endswith(".pdf"):
                file_name = file_name[:-4]

            # Save quiz as JSON
            with open(f"data/quiz-{file_name}.json", "w", encoding='latin-1', errors='ignore') as f:
                f.write(json.dumps(json_questions))

            # Generate the PDF
            generate_pdf_quiz(f"data/quiz-{file_name}.json", json_questions)
            
            st.write("PDF Quiz generated successfully!")

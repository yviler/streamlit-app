from modeling import scoring, test_prediction
from save_score import save_score
from model import model_load
from questions import load_question
from tasks import load_tasks
from courses import load_courses
from student_name import load_student_names
from evaluate_score import evaluate_score
import streamlit as st
import sqlite3 

st.set_page_config(page_title="Page Title", layout="wide")

st.markdown("""
    <style>
        .block-container {
            #background-color: white;
            padding-top: 0.5rem;
            padding-bottom: 0rem;
            padding-left: 0.5rem;
            padding-right: 0.5rem;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        body{ background-color: white;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

head1 = st.header('Real Time Online Tutorial Test',  divider='rainbow')
head2 = st.write('**Open University** | :sunglasses: **:blue[Automatic Essay Scoring]**')

conn = sqlite3.connect('/content/gdrive/MyDrive/Asset/database_baru.db')

student_names = load_student_names(conn)
courses = load_courses(conn)

with st.sidebar:
    image = Image.open('/content/gdrive/MyDrive/Asset/student.jpg')
    st.image(image)

    add_identity = st.sidebar.selectbox(
        "Student Identity", student_names
    )

    add_header = st.header('Main Menu', divider='rainbow')
    course_info = st.radio(
        "Choose Exam Course", courses
    )

    task_info = st.radio(
        "Choose Tutorial Task", load_tasks(conn, course_info)
    )

question = load_question(course_info, task_info)

txt_soal1 = st.text_area("Question", question, disabled=True)

txt_jawaban_student = st.text_area("Answer", height=400)

st.write(f'You wrote {len(txt_jawaban_student)} characters.')

col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

with col1:
    btn_evaluate = st.button('Evaluate')

with col2:
    btn_save = st.button('Save')

with col3:
    btn_close = st.button('Close')

if btn_evaluate:
    evaluate_score(txt_jawaban_student, course_info, task_info, question)

if btn_save:
    save_score()

if btn_close:
    conn.close()

from modeling import scoring, test_prediction
from save_score import save_score
from model import model_load
from questions import load_question
from tasks import load_tasks
from courses import load_courses
from student_name import load_student_names
from evaluate_score import evaluate_score
from PIL import Image
import streamlit as st
import sqlite3
from streamlit_login_auth_ui.widgets import __login__
from upload_pdf import upload_pdf
import fitz

nomor_soal = 0
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

__login__obj = __login__(auth_token="courier_auth_token",
                         company_name="Shims",
                         width=200, height=250,
                         logout_button_name='Logout', hide_menu_bool=False,
                         hide_footer_bool=False,
                         lottie_url='https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:
    conn = sqlite3.connect('database_aes.db')
    student_names = load_student_names(conn)
    courses = load_courses(conn)

    with st.sidebar:
        image = Image.open('student.jpg')
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

    question_info = st.radio("Question Number", ['1', '2', '3', '4'], horizontal=True)
    question = load_question(conn, course_info, task_info, question_info)
    txt_soal = st.text_area(
        "Question:",
        question,
        disabled=True
    )

    txt_jawaban_student = st.text_area("Answer", height=400)

    st.write(f'You wrote {len(txt_jawaban_student)} characters.')
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

    with col1:
        btn_evaluate = st.button('Evaluate')

    with col2:
        btn_save = st.button('Save')

    conn = sqlite3.connect('aestest1.db')


    uploaded_file = st.file_uploader("Choose a file", type=["pdf"], accept_multiple_files=False)

    if uploaded_file:
        st.write('File uploaded successfully.')

        upload_pdf(uploaded_file, conn, course_info, task_info, txt_soal, add_identity)

    if btn_evaluate:
        st.write(evaluate_score(conn, txt_jawaban_student, course_info, task_info, txt_soal))

    if btn_save:
        score = evaluate_score(conn, txt_jawaban_student, course_info, task_info, txt_soal)
        save_score(txt_jawaban_student, score, course_info, add_identity, task_info)

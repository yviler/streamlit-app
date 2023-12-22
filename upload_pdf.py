import streamlit as st
import fitz
import io
from evaluate_score import evaluate_score
from save_score import save_score
import sqlite3 
import pandas as pd 

def upload_pdf(file_name, conn, course_info, task_info, txt_soal, add_identity):
    if file_name is not None and hasattr(file_name, 'type') and file_name.type == "application/pdf":
        st.write("PDF file detected. Processing...")
        # Read the content of the PDF file
        pdf_content = file_name.read()

        # Create a file-like object from the content
        pdf_file = io.BytesIO(pdf_content)

        # Process the PDF file with PyMuPDF (fitz)
        pdf_document = fitz.open(stream=pdf_file, filetype="pdf")
        text = ''
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            text += page.get_text()

        # Close the PDF document
        pdf_document.close()

        # Evaluate and save the score
        score = evaluate_score(conn, text, course_info, task_info, txt_soal)
        save_score(text, score, course_info, add_identity, task_info)
        st.write(f'Score: {score}')

    else:
        st.write("Unsupported file format. Please upload a PDF file.")
        text = 'Salah Input'

    return text

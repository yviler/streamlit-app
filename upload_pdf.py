import streamlit as st
import fitz

def upload_pdf(file_name):
  if file_name.type == "application/pdf":
    # Proses file PDF dengan Fitz (PyMuPDF)
    st.write(file_name.name)
    doc = fitz.open(file_name)
    text = ''
    for page in doc:
      page_text = page.get_text()
      text += page_text
  else:
      st.write("Unsupported file format. Please upload a PDF, PNG, or JPG file.")
      text = 'Salah Input'
  return text

import streamlit as st
import fitz

def upload_pdf(file_pdf):
  doc = fitz.open(stream=file_pdf.read(), filetype="pdf")
  text = ""
  for page in doc:
    text += page.get_text()
  doc.close()
  return text

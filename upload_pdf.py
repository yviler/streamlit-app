import streamlit as st
import fitz 

def upload_pdf(uploaded_file):
  if uploaded_file.type is not None:
    # Proses file PDF dengan Fitz (PyMuPDF)
    st.write(uploaded_file.upload_url)
    doc = fitz.open(uploaded_file.upload_url)
    text = ''
    for page in doc:
        page_text = page.get_text()
        text += page_text	
  else:
        st.write("Unsupported file format. Please upload a PDF, PNG, or JPG file.")
        text = 'Salah Input'
  # else:
  # doc = fitz.open(uploaded_file)
  #       text = 'init'
  #       for page in doc:
  #                   page_text = page.get_text()
  #                   text += page_text
  #       pymupdf_test = text
  
  return text

  #show output
  #answers = []
  #answers.append(st.text_area(f'Write answer question {i}', value=str(pymupdf_test) ,height= 300))

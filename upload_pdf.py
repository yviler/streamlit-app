import streamlit as st
import fitz 
import PyPDF2

def upload_pdf(file_name):
  if file_name.type == "application/pdf":
    # Proses file PDF dengan Fitz (PyMuPDF)
    st.write(file_name)
    with open(file_name.name , "rb") as pdf_file:
      pdf_reader = PyPDF2.PdfReader(pdf_file)
      text = ""
      for page_num in range(len(pdf_reader.pages)):
          page = pdf_reader.pages[page_num]
          text += page.extract_text()
    #words = file_name.read()
    #text = words.decode('iso-8859-1')

    #doc = fitz.open(file_name.name)
    #text = ''
    #for page in doc:
        #page_text = page.get_text()
        #text += page_text	
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

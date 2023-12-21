import pandas as pd 
import streamlit as st
import sqlite3

def save_score(txt_jawaban_student, score, course_info, add_identity, task_info):

  prediction_score = pd.read_csv('prediction_score.csv', sep="\t", encoding="ISO-8859-1")
  string_student_score = prediction_score['score']
  student_score = score
  
  conn = sqlite3.connect('database_aes.db')
  cursor = conn.cursor()
  #course_info = course_info[:-1]
  course_info = "%"+course_info+"%"
  cursor.execute('SELECT * FROM aes_course WHERE courseName LIKE ?', (course_info, ))
  table = cursor.fetchall()
  course_id = []
  
  for row in table:
    course_id.append(row[0])
    
  cursor.execute('SELECT studentID FROM aes_student WHERE studentName = ?', (add_identity, ))
  student_id = cursor.fetchone()
  task_info = "Task " + str(task_info)
  
  cursor.execute('SELECT assignmentID FROM aes_assignment WHERE courseID = ? AND assignmentType = ?', (course_id[0], task_info))
  assignment_id = cursor.fetchone()

  cursor.execute('SELECT answerTake FROM aes_student_answer_score WHERE studentName = ? AND courseID = ?', (add_identity, course_id[0]))
  result = cursor.fetchone()

  cursor.execute('SELECT answerID FROM aes_student_answer_score ORDER BY answerID DESC LIMIT 1')
  answer_id = cursor.fetchone()
  id = answer_id[0] + 2

  insert_query = '''INSERT INTO aes_student_answer_score (answerID, studentID, studentName, courseID, assignmentID, answerText, answerScore, answerTake, answerNoted, answerActivied, answerStatus)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
  st.write(id)
  st.write(student_id[0])
  st.write(add_identity)
  st.write(course_id[0], assignment_id[0], txt_jawaban_student, student_score, result[0])
  if result is not None:
    cursor.execute(insert_query, (id, student_id[0], add_identity, course_id[0], assignment_id[0], txt_jawaban_student, student_score, result[0] + 1, 'Ok', 1, 'Ok'))

  else:
    cursor.execute(insert_query, (id, student_id[0], add_identity, course_id[0], assignment_id[0], txt_jawaban_student, student_score, 1, 'Ok', 1, 'Ok'))

  conn.commit()
  
  #close connection
  cursor.close()
  conn.close()
  
  st.write ('Score Data saved.')

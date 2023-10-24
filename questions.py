
def load_question(conn, course_name, task_info, question_number):
  cursor = conn.cursor()
  question_num = str(task_info)+"_"+str(question_number)
  cursor.execute('SELECT Question FROM course_info WHERE course = ? AND question_id = ?', (task_info, question_num))
  result = [row[0] for row in cursor.fetchall()]
  return result[0]


def model_load(conn, course_name, task_info, problem):
  cursor = conn.cursor()
  cursor.execute('SELECT Model_Name FROM course_info WHERE Task = ? AND Course = ? AND Question = ?', (task_info, course_name, problem))
  #result = [row[0] for row in cursor.fetchall()]
  result = cursor.fetchone()
  
  if result is None:
    result =('aesindo-bert-bilstm1_1.h5.',)
    
  return result[0]

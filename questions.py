
def load_question(conn, course_name, task_info):
  cursor = conn.cursor()
  cursor.execute('SELECT Question FROM course_info WHERE Task = ? AND Course = ?', (task_info, course_name))
  result = [row[0] for row in cursor.fetchall()]
  return result[0]

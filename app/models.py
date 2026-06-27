import sqlite3

def get_db():
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, roll_no TEXT, grade TEXT)')
    conn.commit()
    conn.close()

def get_all_students():
    conn = get_db()
    students = conn.execute(
        'SELECT id, name, roll_no, grade FROM students ORDER BY id'
    ).fetchall()
    conn.close()
    return students

def get_student_by_id(student_id):
    conn = get_db()
    student = conn.execute(
        'SELECT id, name, roll_no, grade FROM students WHERE id = ?',
        (student_id,),
    ).fetchone()
    conn.close()
    return student

def update_student_grade(student_id, grade):
    conn = get_db()
    cursor = conn.execute(
        'UPDATE students SET grade = ? WHERE id = ?',
        (grade, student_id),
    )
    conn.commit()
    updated = cursor.rowcount > 0
    conn.close()
    return updated

def delete_student(student_id):
    conn = get_db()
    cursor = conn.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted

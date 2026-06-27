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
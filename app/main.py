from flask import Flask, render_template

from models import get_all_students, init_db

app = Flask(__name__)

@app.route('/')
def home():
    return 'Student Management System - v0.1'

@app.route('/students')
def list_students():
    students = get_all_students()
    return render_template('students.html', students=students)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

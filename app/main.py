from flask import Flask, abort, redirect, render_template, request, url_for

from models import add_student, delete_student, get_all_students, get_student_by_id, init_db, update_student_grade

app = Flask(__name__)

@app.route('/')
def home():
    return 'Student Management System - v0.1'

@app.route('/students')
def list_students():
    students = get_all_students()
    return render_template('students.html', students=students)

@app.route('/students/new', methods=['GET'])
def new_student_form():
    return render_template('add_student.html')

@app.route('/students', methods=['POST'])
def create_student():
    name = request.form.get('name', '').strip()
    roll_no = request.form.get('roll_no', '').strip()
    grade = request.form.get('grade', '').strip()
    if not name or not roll_no or not grade:
        abort(400, 'Name, roll number, and grade are required')
    add_student(name, roll_no, grade)
    return redirect(url_for('list_students'))

@app.route('/students/<int:student_id>/grade', methods=['POST'])
def update_grade(student_id):
    grade = request.form.get('grade', '').strip()
    if not grade:
        abort(400, 'Grade is required')
    if not get_student_by_id(student_id):
        abort(404)
    update_student_grade(student_id, grade)
    return redirect(url_for('list_students'))

@app.route('/students/<int:student_id>/delete', methods=['POST'])
def delete_student_route(student_id):
    if not get_student_by_id(student_id):
        abort(404)
    delete_student(student_id)
    return redirect(url_for('list_students'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

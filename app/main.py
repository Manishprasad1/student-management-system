from flask import Flask

from models import init_db

app = Flask(__name__)

@app.route('/')
def home():
    return 'Student Management System - v0.1'

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

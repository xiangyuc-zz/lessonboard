from flask import render_template
from lessonboard import app
from lessonboard.models import Subject


@app.route('/')
def index():
    subjects = Subject.query.all()
    return render_template('index.html', subjects=subjects)

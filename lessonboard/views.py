from flask import render_template
from flask_login import login_user
from lessonboard import app
from lessonboard.models import Subject, Board, User
from lessonboard.forms import LoginForm
from lessonboard.extensions import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def index():
    subjects = Subject.query.all()
    return render_template('index.html', subjects=subjects)


@app.route('/subject/<subject_id>/')
def subject_page(subject_id):
    subject = Subject.query.get(subject_id)

    if subject is None:
        return render_template('404.html'), 404

    return render_template('subject_page.html',
                           subject=subject,
                           boards=subject.boards.all())


@app.route('/board/<board_id>/')
def board_page(board_id):
    board = Board.query.get(board_id)

    if board is None:
        return render_template('404.html'), 404

    return render_template('board_page.html',
                           board=board,
                           chapters=board.chapters.all())


@app.route('/login/', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()

    if form.validate_on_submit():
        login_user()

    return render_template('login_page.html', form=form)

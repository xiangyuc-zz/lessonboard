from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
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
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user is not None and user.check_password(password):
            login_user(user)
            flash('Login succeeded')
            return redirect(url_for('index'))
        else:
            flash('Login failed')

    return render_template('login_page.html', form=form)


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('Logout succeeded')
    return redirect(url_for('index'))

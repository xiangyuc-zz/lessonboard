from lessonboard import app


@app.route('/')
def hello_world():
    return 'Hello Flask!'

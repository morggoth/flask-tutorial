from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    # Mock the user object
    user = {'username': 'Morggoth'}
    # Mock the posts object
    posts = [
        {
            'author': {'username': 'Morggoth'},
            'body': 'Breaking news: the Sun over the SPb'
        },
        {
            'author': {'username': 'Alcopenguin'},
            'body': 'Schizophrenia is not a verdict'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
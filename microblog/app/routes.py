from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # Allows us to process the form. When the browser sends the GET request, it returns False and skips,
    # but on the POST request it returns True, gathers all the data in the request and apply all validators
    if form.validate_on_submit():
        # flash() shows a message to the user
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
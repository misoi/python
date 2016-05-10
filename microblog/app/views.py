from flask import render_template, flash, redirect,session, url_for, request, g
from app import app, db, lm, oid
from flask.ext.login import login_user, logout_user, current_user, login_required
from .forms import LoginForm
from .models import User



@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        },
        {
            'author': {'nickname': 'LINDA'},
            'body': 'HULULULU!!!! AM HOME!'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

from .forms import LoginForm
@app.route('/login', methods=['GET', 'POST']) #tells the server that it accepts/support both GET and POST REQUESTS
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit(): #Does all the processing work.It will collect the data and run all the validators
        flash('login requested for OpenID="%s", remember_me=%s' %(form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                        providers=app.config['OPENID_PROVIDERS'])

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

from flask import Flask
from flask import Flask, render_template, session, redirect, url_for
from app import app
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
def index():
    user = {'nickname': 'Cynthia'}  # fake user
    posts = [  # fake array of post
        {
            'body': 'How to implement facebook API in your project'
        }
    ]
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
            session['name'] = form.name.data
            form.name.data = ''
    return render_template('index.html', form=form, name=session.get('name'), title='Home', user=user, posts=posts,)


@app.route('/about')
def about():
    user = {'nickname': 'Cynthia'}  # fake user
    posts = [  # fake array of post
        {
            'body': 'Some thing here'
        }
    ]
    return render_template("about.html",
                           user=user,
                           posts=posts)
class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
    
def login():
    return render_template('login.html')
    
    



    






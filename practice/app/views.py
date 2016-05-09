from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Cynthia'}  # fake user
    posts = [  # fake array of post
        {
            'body': 'How to implement facebook API in your project'
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

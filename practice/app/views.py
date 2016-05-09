from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Cynthia'}
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''<br> Cynthia's blog</h1>

  </body>
</html>
    '''




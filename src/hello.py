from flask import Flask, url_for, render_template, request, abort, redirect
app = Flask(__name__.split('.')[0])
from functools import wraps

def assess(f):
  @wraps(f)
  def decorator():
    print('>>>> decorator')
    return redirect(url_for('hello_world'))
  return decorator

@app.route('/')
def hello_world():
  return 'Hello World'

@app.route('/template')
def template(name=None):
  return render_template('index.html', name=name)

@app.errorhandler(403)
def logger(err):
  print('>>>>', err)
  return 'test'

@app.route('/user', methods=['GET', 'POST'])
@assess
def user():
  ''' get user '''
  user = ''
  if request.method == 'POST':
    user = request.form['username']
    return 'User: %s' % user
  return 'Users'

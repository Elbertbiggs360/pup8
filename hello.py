from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World'

@app.route('/user/<username>')
def show_user_profile(username):
  ''' Show user profile for that user '''
  return 'User: %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
  ''' return the post with the given id '''
  return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
  ''' return the subpath '''
  return 'Subpath: %s' % subpath

@app.route('/projects/')
def fetch_projects():
  return 'Prjkts'

@app.route('/about')
def about():
  ''' return about info '''
  return 'about'
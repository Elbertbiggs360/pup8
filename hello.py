from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World'

@app.route('/template')
def template(name=None):
  return render_template('index.html', name=name)

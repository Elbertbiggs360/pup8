''' Application main module '''

from flask import Flask, jsonify

def create_app():
  ''' method to instantiate Flask app '''
  app = Flask(__name__)

  @app.route('/')
  def home():
    return jsonify({'Home': 'Welcome Home'})

  return app

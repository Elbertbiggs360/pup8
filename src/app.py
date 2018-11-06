''' Application module'''

from flask import Flask
from flask_restplus import Api

def create_app():
  '''
  Creates an instance of the application

  Returns:
    app(Flask): Returns an instance of the flask application
  '''

  app = Flask(__name__.split('.')[0])

  @app.route('/')
  def hello_world():
    return 'test'

  return app

''' Application module'''

from flask import Flask
from flask_restplus import Api

try:
  from .config import Configuration
except ImportError:
  from config import configuration

def create_app(environ='Development'):
  '''
  Creates an instance of the application

  Returns:
    app(Flask): Returns an instance of the flask application
  '''

  app = Flask(__name__.split('.')[0])
  app.config.from_object(configuration[environ])

  @app.route('/')
  def hello_world():
    ''' test method '''
    return 'test'

  @app.errorhandler(404)
  def resource_not_found(error):
    return error, 404
  
  return app

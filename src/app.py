''' Application main module '''
import os
from flask import Flask, request, jsonify, abort

try:
  from .config import configuration
except ImportError:
  from config import configuration

from api.models import Fellow

environment = os.getenv('ENVIRONMENT') or 'development'
USERS = []

def create_app(environment=environment):
  ''' method to instantiate Flask app '''
  
  app = Flask(__name__.split('.')[0])
  app.config.from_object(configuration[environment])

  @app.route('/')
  def home():
    return 'welcome'

  @app.route('/fellow', methods=['GET', 'POST'])
  def fellow():
    if request.method == 'GET':
      return jsonify({'Fellow': 'Bruce'})
    if request.method == 'POST':
      level = request.form['level']
      name = request.form['name']
      if not name:
        abort(406)
      return jsonify({'message': 'Successfull!'}), 201

  @app.errorhandler(406)
  def not_acceptable():
    return 406, 'Unacceptable'

  return app

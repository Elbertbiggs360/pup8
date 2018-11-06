''' Contain's App's configurations '''
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Config(object):
  ''' Base config model '''

  DEBUG = False
  TESTING = False
  SECRET_KEY = os.environ.get('SECRET_KEY')

class Development(Config):
  ''' Model for development '''
  DEBUG = True
  DEVELOPMENT = True

configuration = {
  'Development': Development
}
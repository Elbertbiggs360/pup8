''' Contain's App's configurations '''

class Config(object):
  ''' Base config model '''

  DEBUG = False
  TESTING = False

class Development(Config):
  ''' Model for development '''
  DEBUG = True
  DEVELOPMENT = True

configuration = {
  'Development': Development
}
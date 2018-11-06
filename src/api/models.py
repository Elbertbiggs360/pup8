''' Models for creating entities '''

class Base(object):
  ''' Base model '''
  __DATE_CREATED = None
  __DATE_MODIFIED = None

  @staticmethod
  def __item_exists():
    return True
  
  def save(self):
    pass
  
  def delete(self):
    pass

class User(Base):
  ''' User model '''
  
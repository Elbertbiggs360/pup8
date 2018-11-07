''' File with models for data handling '''

class Base(object):

  def __init__(self, name):
    self._NAME = name

  def __repr__(self):
    pass
  
  def save(self):
    pass

  def delete(self):
    pass

class Fellow(Base):
  __tablename__ = 'fellows'
  
  def __init__(self, name, level='D1'):
    self.name = name
    self.level = level

class Staff(Base):
  __tablename__ = 'staff'

  def __init__(self, role):
    self.role = role
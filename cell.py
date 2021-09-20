class Cell():
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.value = None
    self.open = False
    self.flagged = False
  def toggleFlag(self):
    if not self.open:
      self.flagged = not self.flagged
  def openCell(self):
    if not self.flagged:
      self.open = True
      return self.value
    return None
  def setValue(self,value):
    self.value=value
  def getValue(self):
    return self.value

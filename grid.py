import preset,random
from cell import Cell
from getkey import keys
textDict = preset.getText()


class Grid():
  def __init__(self,size,mines):
    self.grid = []
    self.size = size
    self.mines = mines
    self.cursorX = 0
    self.cursorY = 0
    for y in range(self.size):
      row = []
      for x in range(self.size):
        row.append(Cell(x,y))
      self.grid.append(row)
    self.setMines()
    self.setNumbers()
    self.running = True
  def setMines(self):
    minesSet = 0
    while minesSet<self.mines:
      mineX = random.randint(0,self.size-1)
      mineY = random.randint(0,self.size-1)
      if self.grid[mineY][mineX].getValue() == None:
        self.grid[mineY][mineX].setValue('X')
        minesSet+=1
  def setNumbers(self):
    for y in range(self.size):
      for x in range(self.size):
        minesTouching = 0
        if x > 0 and self.grid[y][x-1].getValue() == 'X':
          minesTouching+=1
        if x < self.size-1 and self.grid[y][x+1].getValue() == 'X':
          minesTouching+=1
        if y > 0 and self.grid[y-1][x].getValue() == 'X':
          minesTouching+=1
        if y < self.size-1 and self.grid[y+1][x].getValue() == 'X':
          minesTouching+=1
        #
        if x > 0 and y > 0 and self.grid[y-1][x-1].getValue() == 'X':
          minesTouching+=1
        if x < self.size-1 and y>0 and self.grid[y-1][x+1].getValue() == 'X':
          minesTouching+=1
        if x>0 and y < self.size-1 and self.grid[y+1][x-1].getValue() == 'X':
          minesTouching+=1
        if x < self.size-1 and y < self.size-1 and self.grid[y+1][x+1].getValue() == 'X':
          minesTouching+=1

        if self.grid[y][x].getValue()==None:
          self.grid[y][x].setValue(str(minesTouching))
  def openCells(self,x,y):
    if x in range(0,self.size) and y in range(0,self.size):
      if not self.grid[y][x].open:
        self.grid[y][x].openCell()
        if self.grid[y][x].getValue() == '0':
          self.openCells(x+1,y)
          self.openCells(x-1,y)
          self.openCells(x,y+1)
          self.openCells(x,y-1)
          self.openCells(x+1,y-1)
          self.openCells(x-1,y-1)
          self.openCells(x+1,y+1)
          self.openCells(x-1,y+1)
  def handleKeys(self,key):
    if key == keys.UP or key == 'w':
      self.cursorY-=1
      self.cursorY = self.cursorY%self.size
    if key == keys.DOWN or key == 's':
      self.cursorY+=1
      self.cursorY = self.cursorY%self.size
    if key == keys.LEFT or key == 'a':
      self.cursorX-=1
      self.cursorX = self.cursorX%self.size
    if key == keys.RIGHT or key == 'd':
      self.cursorX+=1
      self.cursorX = self.cursorX%self.size
    if key == 'f':
      self.grid[self.cursorY][self.cursorX].toggleFlag()
    if key == keys.ENTER:
      self.openCells(self.cursorX,self.cursorY)
  def checkWin(self):
    minesClicked = 0
    cellsNeedOpen = 0
    for y in range(self.size):
      for x in range(self.size):
        if self.grid[y][x].getValue() == 'X' and self.grid[y][x].open:
          print('clicked mine')
          minesClicked+=1
        if self.grid[y][x].getValue() != 'X' and not self.grid[y][x].open:
          cellsNeedOpen+=1
    if minesClicked > 0:
      self.running = False
      return False
    elif cellsNeedOpen == 0:
      self.running = False
      return True
    return None
  def getGrid(self):
    return self.grid
  def display(self):
    for y in range(len(self.grid)):
      for x in range(len(self.grid[y])):
        c=self.grid[y][x]
        if x == self.cursorX and y == self.cursorY:
          print('\u001b[48;2;255;255;0m',end='')
        if c.flagged:
          print('\u001b[38;2;255;127;0m'+'█'+'\u001b[0m',end='')
        elif not c.open:
          print('\u001b[38;2;127;127;127m'+'█'+'\u001b[0m',end='')
        else:
          if c.getValue() in textDict.keys():
            print(textDict[c.getValue()]+c.getValue()+'\u001b[0m',end='')
          elif c.getValue() == 'X':
            print('\u001b[38;2;255;0;0m'+'X'+'\u001b[0m',end='')
          else:
            print('\u001b[38;2;127;127;127m'+'▒'+'\u001b[0m',end='')
      print()
      #█
  def printGrid(self):
    for row in self.grid:
      for c in row:
        print(c.getValue(),end='')
      print()

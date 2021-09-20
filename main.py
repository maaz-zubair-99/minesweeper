import preset,grid,replit, getkey
replit.clear()
print('===================================================')
diff=  preset.getDifficulty()
numText = preset.getText()
g = grid.Grid(diff['very easy']['size'],
diff['very easy']['mines'])
result = None
while g.running:
  replit.clear()
  g.display()
  k = getkey.getkey()
  g.handleKeys(k)
  result = g.checkWin()
replit.clear()
g.display()
if result:
  print("You win!")
else: 
  print("You lose...")

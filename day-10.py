
def getKey(x,y):
  return "%d,%d" % (x,y)

class Node:
  def __init__(self, x, y, shape):
    self.x = x
    self.y = y
    self.key = getKey(x,y)
    self.neighbors = []
    self.shape = shape

    if shape == 'F':
      self.addNeighbor(1,0)
      self.addNeighbor(0,1)
    elif shape == 'J':
      self.addNeighbor(0,-1)
      self.addNeighbor(-1,0)
    elif shape == '|':
      self.addNeighbor(0,-1)
      self.addNeighbor(0,1)
    elif shape == '-':
      self.addNeighbor(-1,0)
      self.addNeighbor(1,0)
    elif shape == 'L':
      self.addNeighbor(0,-1)
      self.addNeighbor(1,0)
    elif shape == '7':
      self.addNeighbor(-1,0)
      self.addNeighbor(0,1)

  def __str__(self):
    return "(%d, %d): %s" % (self.x, self.y, self.shape )

  def addNeighbor(self, dx, dy):
    global max_x, max_y
    tryX = self.x + dx
    tryY = self.y + dy
    if tryX < 0 or tryX > max_x or tryY < 0 or tryY > max_y:
      return

    self.neighbors.append(getKey(tryX, tryY))


row = -1 
col = -1 
nodes = {}

max_x = None
max_y = None

file = open("day-10.txt", 'r')
lines = []
max_y = -1 
for line in file:
  max_y += 1
  lines.append(line.strip())
file.close()
max_x = len(lines[0])-1

startX = startY = None
for line in lines:
  row += 1
  for c in line.strip():
    col += 1
    if c == '.':
      continue
    else:
      n = Node(col, row, c)
      nodes[n.key] = n
      if c == 'S':
        startX = col
        startY = row
  col = -1

#for k, v in nodes.items():
  #print(k, "...", v)

N = 0
E = 1
S = 2
W = 3

# find any direction that connects to Start
curX = startX
curY = startY
curKey = startKey = getKey(curX, curY)
for d in range(4):
  tryX = curX
  tryY = curY

  if d == N:
    tryY -= 1
  elif d == E:
    tryX += 1
  elif d == S:
    tryY += 1
  else:
    tryX -= 1

  tryKey = getKey(tryX, tryY)
  if tryKey in nodes and curKey in nodes[tryKey].neighbors:
    #print( 'found neighbor in', tryKey)
    curKey = tryKey
    break

path = [curKey]
curNode = nodes[curKey]
while curNode.shape != 'S':
  #print( path, curNode.neighbors )
  for tryKey in curNode.neighbors:
    #print( '+', tryKey, startKey, len(path))
    if tryKey == startKey and len(path) ==1:
      continue

    if tryKey not in path:
      curKey = tryKey
      path.append(curKey)
      curNode = nodes[curKey]
      #print( '  ... adding', curKey )
      break


print()
print( path )
part_one = int(len(path)/2)
print( "part_one:", part_one )






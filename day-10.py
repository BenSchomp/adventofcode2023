import sys
sys.setrecursionlimit(100000)

def getKey(x,y):
  return "%d,%d" % (x,y)

def display(grid):
  for row in grid:
    out = ''
    for c in row:
      if c == 0:
        out += '.'
      else:
        out += 'X'
    print( out )

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

def isOutside(x, y):
  global width, height
  global maze, visited
  k = getKey(x,y)
  if k in outside:
    return True
  if maze[y][x] == 0 and (x == 0 or x == width-1 or y == 0 or y == height-1):
    outside.add(k)
    return True
  if maze[y][x] == 1 or k in visited:
    return False

  visited.add(k)

  if isOutside(x-1, y):
    outside.add(k)
    return True
  if isOutside(x+1, y):
    outside.add(k)
    return True
  if isOutside(x, y-1):
    outside.add(k)
    return True
  if isOutside(x, y+1):
    outside.add(k)
    return True

  return False

max_x = max_y = None
widgh = height = None
maze = []
visited = set()
outside = set()

# --- main ---
def main():
  row = -1 
  col = -1 
  nodes = {}
  global max_x, max_y, width, height
  global maze, visited, outside

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

  # --- part one --- #
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
      curKey = tryKey
      break

  path = []
  path.append(curKey)
  curNode = nodes[curKey]
  while curNode.shape != 'S':
    for tryKey in curNode.neighbors:
      if tryKey == startKey and len(path) ==1:
        continue

      if tryKey not in path:
        curKey = tryKey
        path.append(curKey)
        curNode = nodes[curKey]
        break

  part_one = int(len(path)/2)
  print( "part_one:", part_one )

  # --- part two --- #

  # make the map double sized so can use maze solving to find
  #  cells that are inner vs outer (doubling allows travel through
  #  adjacent pipes more obvious)
  width = (max_x+1)*2
  height = (max_y+1)*2
  maze = [[ 0 for x in range(width)] for y in range(height)]

  # translate to the double map
  for y in range(max_y+1):
    for x in range(max_x+1):
      curKey = getKey(x, y)
      if curKey in path:
        maze[y*2][x*2] = 1

  # now just need to connect the pipes along the path to fill in the gaps
  curX = startX*2
  curY = startY*2
  for p in path:
    (tgtX, tgtY) = p.split(',')
    tgtX = int(tgtX)*2
    tgtY = int(tgtY)*2
    gapX = int((curX+tgtX)/2)
    gapY = int((curY+tgtY)/2)
    maze[gapY][gapX] = 1

    curX = tgtX
    curY = tgtY

  # lastly, try every spot not in the path
  part_two = 0
  for tryX in range(max_x+1):
    for tryY in range(max_y+1):
      if getKey(tryX, tryY) in path:
        continue

      visited.clear()
      if not isOutside(tryX*2, tryY*2):
        part_two += 1

  print( "part_two:", part_two )

if __name__=="__main__":
  main()

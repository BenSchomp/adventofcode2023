
grid = []
width = height = None
part_one = part_two = 0

def check( r, c ):
  #print( r, c )
  if r < 0 or r >= height or c < 0 or c >= width:
     return False
  return not (grid[r][c].isdigit() or grid[r][c] == '.')

def checkRow( r, dr, a, b ):
  if r+dr < 0:
    return False
  if dr == 0:
    return check(r,a) or check(r,b)
  if r+dr > height-1:
    return False

  i = a
  while( i <= b ):
    if check( r+dr, i ):
      return True
    i += 1

  return False

def isAdjacent( row, a, b ):
  result = checkRow( row, -1, a-1, b+1 ) or \
           checkRow( row,  0, a-1, b+1 ) or \
           checkRow( row,  1, a-1, b+1 )
  return result


file = open('day-03.txt', 'r')
for line in file:
  row = []
  line = line.strip()
  for c in line:
    row.append(c)

  grid.append(row)
file.close()

width = len(grid[0])
height = len(grid)

checkAdj = False
num = num_start = None
for y in range(height):
  for x in range(width):
    cur = grid[y][x]

    if cur.isdigit():
      if not num:
        num_start = x
        num = ''
      num += cur

      if x == width-1:
        checkAdj = True

    else: # not cur.isdigit():
      if not num:
        continue
      else:
        checkAdj = True

    if checkAdj:
      #print( '\n*', num )
      if isAdjacent( y, num_start, num_start+len(num)-1 ):
        #print( '! Adjacent !' )
        part_one += int(num)
      num = num_start = None
      checkAdj = False

print()
print( 'part one:', part_one )
print( 'part two:', part_two )

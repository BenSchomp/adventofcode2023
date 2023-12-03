width = height = None

def checkOne( r, c ):
  if r < 0 or r >= height or c < 0 or c >= width:
     return None

  if not( grid[r][c].isdigit() or grid[r][c] == '.' ):
    return (str(c)+','+str(r), grid[r][c])

def checkRow( r, dr, a, b ):
  if r+dr < 0:
    return None
  if dr == 0:
    return checkOne(r,a) or checkOne(r,b)
  if r+dr > height-1:
    return None

  i = a
  done = None
  while( i <= b and not done ):
    done = checkOne( r+dr, i )
    i += 1

  return done

def isAdjacent( row, a, b ):
  result = checkRow( row, -1, a-1, b+1 ) or \
           checkRow( row,  0, a-1, b+1 ) or \
           checkRow( row,  1, a-1, b+1 )
  return result


# -------------------------------------------

grid = []
gears = {}
part_one = part_two = 0
x = y = 0

file = open('day-03.txt', 'r')
for line in file:
  row = []
  line = line.strip()
  for c in line:
    row.append(c)
    if c == '*':
      k = str(x)+','+str(y)
      gears[k] = []
    x += 1

  y += 1
  x = 0

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
      result = isAdjacent( y, num_start, num_start+len(num)-1 )

      if result:
        part_one += int(num)
        if result[1] == '*':
          gears[result[0]].append(num)

      num = num_start = None
      checkAdj = False

print( 'part one:', part_one )

for k,v in gears.items():
  if( len(v) == 2 ):
    part_two += int(v[0]) * int(v[1])
print( 'part two:', part_two )


N = 0
E = 1
S = 2
W = 3

def display(grid):
  for g in grid:
    print( g )
  print()

def getNumStepsUntilStop( grid, dir, r, c ):
  dx = dy = 0
  steps = 0

  height = len(grid)
  width = len(grid[0])

  if dir == N:
    dy = -1
  elif dir == S:
    dy = 1
  elif dir == W:
    dx = -1
  elif dir == E:
    dx = 1

  while True:
    r = r + dy
    c = c + dx

    if r < 0 or r >= height or c < 0 or c >= width:
      break

    if grid[r][c] == '.':
      steps += 1
    else:
      break

  if dir == S or dir == E:
    steps *= -1

  return steps

def getLoad( grid ):
  result = 0
  height = len(grid)
  for r, row in enumerate(grid):
    load = height - r
    for col in row:
      if col == 'O':
        result += load

  return result


def tilt( grid, dir ):
  height = len(grid)
  width = len(grid[0])

  rowStep = 1
  if dir == S:
    rowStep = -1

  colStep = 1
  if dir == E:
    colStep = -1

  for r in range(height)[::rowStep]:
    row = grid[r]

    for c in range(width)[::colStep]:
      col = row[c]
      if col == 'O':
        steps = getNumStepsUntilStop( grid, dir, r, c )

        if steps != 0:
          row = row[:c] + '.' + row[c+1:]

          if dir == N or dir == S:
            grid[r-steps] = grid[r-steps][:c] + 'O' + grid[r-steps][c+1:]
          elif dir == W or dir == E:
            row = row[:c-steps] + 'O' + row[c-steps+1:]

          grid[r] = row


# --- main --- #
file = open("day-14.txt", 'r')
grid = []
for line in file:
  line = line.strip()
  grid.append(line)

file.close()

tilt(grid, N)
print( 'part_one:', getLoad(grid) )

loads = {}
cycles = 1000000000
cycles = 1000
for cycle in range( cycles ):
  tilt( grid, N)
  tilt( grid, W)
  tilt( grid, S)
  tilt( grid, E)
  print( cycle+1, getLoad(grid) )
  load = getLoad(grid)
  if not load in loads:
    loads[load] = 1
  else:
    loads[load] += 1

period = 0
for k, v in loads.items():
  if v > 1:
    period += 1
    print( k, v, int(1000/v))

print( loads )
print( period )
#print( 'part_two:', getLoad(grid) )



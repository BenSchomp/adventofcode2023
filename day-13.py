def display( grid ):
  for g in grid:
    print( g )

H = 0
V = 1

def isMirror(line, i):
  j = i+1
  while i>=0 and j<len(line):
    if line[i] != line[j]:
      return False
    i -= 1
    j += 1
  return True

def getMirrorIndexes(line):
  result = []
  i = 0
  while i < len(line)-1:
    if isMirror(line, i):
      result.append(i)
    i += 1
  return result

def getMirrorScore(grid, scoreToIgnore=None):
  # instead, find a mirror in row 1 ... then try all other rows at that col only
  # if all rows find a mirror at same col, that's the mirror col
  # if not, continue searching across row 1
  score = None
  vIndexes = getMirrorIndexes(grid[0])

  found = None
  for i in vIndexes:
    found = [H, i]
    for line in grid[1:]:
      if not isMirror(line, i):
        found = None
        break

    if found:
      score = found[1]+1
      if score != scoreToIgnore:
        return score

  hIndexes = getMirrorIndexes( ''.join([g[0] for g in grid]) )

  found = None
  for i in hIndexes:
    found = [V, i]
    col = 1 
    while col < len(grid[0]):
      line = ''.join([g[col] for g in grid])
      if not isMirror(line, i):
        found = None
        break
      col += 1

    if found:
      score = (found[1]+1) * 100
      if score != scoreToIgnore:
        return score

  return None


# --- main --- #
file = open("day-13.txt", 'r')
grid = []
grids = []
for line in file:
  line = line.strip()
  if not line:
    grids.append(grid)
    grid = []
    continue
  else:
    grid.append(line)
grids.append(grid)
grid = []

file.close()

part_one = part_two = 0
for grid in grids:
  # --- part one --- #
  origScore = getMirrorScore( grid )
  part_one += origScore

  # --- part two --- #
  done = False
  for r, row in enumerate(grid):
    if done:
      break
    for c, ch in enumerate(row):
      newGrid = grid[:]
      newRow = row[:]
      if ch == '.':
        newRow = row[:c] + '#' + row[c+1:]
      else:
        newRow = row[:c] + '.' + row[c+1:]
      newGrid[r] = newRow

      newScore = getMirrorScore( newGrid, origScore )
      if newScore:
        part_two += newScore
        done = True
        break

print( "part_one:", part_one )
print( "part_two:", part_two )



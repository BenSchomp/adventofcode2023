def display( grid ):
  for g in grid:
    print( g )

H = 0
V = 1

def isMirror(line, i):
  #print( 'isMirror', line, i )
  j = i+1
  while i>=0 and j<len(line):
    #print( i, j, line[i], line[j] )
    if line[i] != line[j]:
      #print( 'nope' )
      return False
    i -= 1
    j += 1
  #print( 'yep:', )
  return True

def getMirrorIndexes(line):
  #print( 'getMirrorIndexes', line )
  result = []
  i = 0
  while i < len(line)-1:
    if isMirror(line, i):
      result.append(i)
    i += 1
  return result

def getMirrorScore(grid):
  # instead, find a mirror in row 1 ... then try all other rows at that col only
  # if all rows find a mirror at same col, that's the mirror col
  # if not, continue searching across row 1

  hIndexes = getMirrorIndexes(grid[0])
  #print( hIndexes )

  found = None
  for i in hIndexes:
    found = [H, i]
    for line in grid[1:]:
      if not isMirror(line, i):
        #print( ' ! not a mirror !' )
        found = None
        break

    if found:
      break

  if found:
    #print( 'found one!', found )
    return found[1]+1

  vIndexes = getMirrorIndexes( [g[0] for g in grid] )

  found = None
  for i in vIndexes:
    found = [V, i]
    col = 1 
    while col < len(grid[0]):
      line = [g[col] for g in grid]
      if not isMirror(line, i):
        found = None
        break
      col += 1

    if found:
      break

  #if found:
    #print( 'found one!', found)

  return (found[1]+1) * 100



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

# --- part one --- #
part_one = 0
for grid in grids:
  tmp = getMirrorScore( grid )
  #print( 'mirror score:',tmp )
  part_one += tmp

print( "part_one:", part_one )



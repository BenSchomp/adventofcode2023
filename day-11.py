
def display(grid):
  for row in grid:
    print( row )

h = w = 0
grid = []
galaxy_columns = set()

file = open("day-11.txt", 'r')
for line in file:
  grid.append(line.strip())

  if not '#' in line:
    grid.append(line.strip())
  else:
    for i, c in enumerate(line):
      if c == '#':
        galaxy_columns.add(i)

file.close()

height = len(grid)
width = len(grid[0])

empty_columns = set()
for i in range(width):
  if not i in galaxy_columns:
    empty_columns.add( i )

offset = 0
for i in range(width):
  if i in empty_columns:
    for j in range(height):
      grid[j] = grid[j][:i+offset] + '.' + grid[j][i+offset:]
    offset += 1

#display( grid )

galaxies = []
for i, row in enumerate(grid):
  for j, c in enumerate(row):
    if c == '#':
      galaxies.append((i,j))

#print( galaxies )

part_one = 0
numGalaxies = len(galaxies)
for i in range(numGalaxies):
  for j in range(numGalaxies):
    if i == j:
      continue
    g1 = galaxies[i]
    g2 = galaxies[j]
    dist = abs(g2[0] - g1[0]) + abs(g2[1] - g1[1])
    part_one += dist

print( "part_one:", int(part_one/2) )




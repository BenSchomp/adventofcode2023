
from itertools import combinations
def display(grid):
  for row in grid:
    print( row )

grid = []
galaxy_cols = set()
empty_rows = set()

file = open("day-11.txt", 'r')
row = 0
for line in file:
  grid.append(line.strip())

  if not '#' in line:
    empty_rows.add(row)
  else:
    for col, c in enumerate(line):
      if c == '#':
        galaxy_cols.add(col)

  row += 1

file.close()

empty_cols = set()
for i in range(len(grid[0])):
  if not i in galaxy_cols:
    empty_cols.add( i )

def expand(expansion):
  global grid, empty_cols, empty_rows
  galaxies = []

  er = sorted(empty_rows)
  erl = len(empty_rows) # empty rows length

  ec = sorted(empty_cols)
  ecl = len(empty_cols) # empty cols length

  eri = row_offset = 0 # empty rows index
  for i, row in enumerate(grid):
    if eri < erl and i >= er[eri]:
      eri += 1
      row_offset += expansion-1

    eci = col_offset = 0 # empty cols index
    for j, c in enumerate(row):
      if eci < ecl and j >= ec[eci]:
        eci += 1
        col_offset += expansion-1
      if c == '#':
        galaxies.append((j+col_offset,i+row_offset))

  result = 0
  galaxy_pairs = combinations(galaxies, 2)
  for p in galaxy_pairs:
    g1 = p[0]
    g2 = p[1]
    dist = abs(g2[0] - g1[0]) + abs(g2[1] - g1[1])
    result += dist

  return result

print( "part_one:", expand(2) )
print( "part_two:", expand(1000000) )




import math

nodes = {}

file = open("day-08.txt", 'r')
f = enumerate(file)

instructions = next(f)[1].strip()
next(f)
for line in file:
  nodes[line[0:3].strip()] = (line[7:10], line[12:15])

file.close()

# --- one --- #
def one():
  done = False
  count = 0
  curNode = 'AAA'
  while not done:
    for d_ in instructions:
      d = 0
      if d_ == 'R':
        d = 1

      count += 1
      curNode = nodes[curNode][d]
      if curNode == 'ZZZ':
        done = True
        break

  print( "part_one:", count )


# --- two --- #
def two():
  ghosts = []

  for k, v in nodes.items():
    if k[2] == 'A':
      ghosts.append([k,None])

  done = False
  count = 0
  lcm_count = 0
  while not done:
    for d_ in instructions:
      d = 0
      if d_ == 'R':
        d = 1

      count += 1
      done = True
      for i, curNode in enumerate(ghosts):
        newNode = nodes[curNode[0]][d]
        if newNode[2] != 'Z':
          done = False
        else:
          if not ghosts[i][1]:
            ghosts[i][1] = count
            lcm_count += 1
            if lcm_count == len(ghosts):
              done = True
              break

        ghosts[i][0] = newNode

      if done:
        break

  if lcm_count == len(ghosts):
    multiples = []
    for g in ghosts:
      multiples.append(g[1])
    part_two = math.lcm( *multiples )
  else:
    part_two = count

  print( "part_two:", part_two )

one()
two()

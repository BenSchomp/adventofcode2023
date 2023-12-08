
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
    for i in instructions:
      count += 1
      if i == 'L':
        curNode = nodes[curNode][0]
      else:
        curNode = nodes[curNode][1]
      #print( curNode )
      if curNode == 'ZZZ':
        done = True
        break

  print( "part_one:", count )

# --- two --- #
def two():
  ghosts = []

  for k, v in nodes.items():
    if k[2] == 'A':
      ghosts.append(k)

  print( ghosts )

  done = False
  count = 0
  max_x = 0
  while not done:
    for d in instructions:
      dir = 0
      if d == 'R':
        dir = 1

      count += 1

      done = True
      x = 0
      for i, curNode in enumerate(ghosts):
        newNode = nodes[curNode][dir]
        #print( newNode )
        if newNode[2] != 'Z':
          done = False
        else:
          x += 1

        ghosts[i] = newNode

      if x > max_x:
        max_x = x
        print( ghosts, x, max_x, count )

      if done:
        break

  print( "part_two:", count )

two()

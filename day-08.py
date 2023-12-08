
nodes = {}

file = open("day-08.txt", 'r')
f = enumerate(file)

instructions = next(f)[1].strip()
next(f)
for line in file:

  nodes[line[0:3].strip()] = (line[7:10], line[12:15])

file.close()

#print( instructions, nodes )

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


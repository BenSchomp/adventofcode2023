
file = open('day-01.txt', 'r')

answer = 0
for line in file:
  line = line.strip()

  term = 0
  for c in line:
    if c.isdigit():
      term += int(c)*10
      break

  for c in reversed(line):
    if c.isdigit():
      term += int(c)
      break

  answer += term
  print( line, term )

file.close()

print( answer )


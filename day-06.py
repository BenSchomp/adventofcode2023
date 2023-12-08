
file = open("day-06.txt", 'r')
f = enumerate(file)
line1 = next(f)
line2 = next(f)
file.close()

parts = line1[1].split(':')
times = list(map(lambda x: int(x), parts[1].split()))
parts = line2[1].split(':')
dists = list(map(lambda x: int(x), parts[1].split()))

# --- part one --- #
part_one = 1
for i, time in enumerate(times):
  goal = dists[i] 
  count = 0
  t = 1
  speed = 1
  while t < time:
    speed = t
    distance = (time - t) * speed
    if distance > goal:
      count += 1
    t += 1

  part_one *= count

print( "part_one:", part_one )



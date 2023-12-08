
file = open("day-06.txt", 'r')
f = enumerate(file)
line1 = next(f)
line2 = next(f)
file.close()

parts = line1[1].split(':')
times = list(map(lambda x: int(x), parts[1].split()))
parts = line2[1].split(':')
dists = list(map(lambda x: int(x), parts[1].split()))

def getGoalCount(time, goal):
  count = 0
  t = 1
  speed = 1
  while t < time:
    speed = t
    distance = (time - t) * speed
    if distance > goal:
      count += 1
    t += 1

  return count

# --- part one --- #
part_one = 1

for i, time in enumerate(times):
  goal = dists[i] 
  count = getGoalCount(time, goal)
  part_one *= count

print( "part_one:", part_one )

time = int(''.join(map(lambda x: str(x), times)))
goal = int(''.join(map(lambda x: str(x), dists)))

# --- part two ---
part_two = 1

count = getGoalCount(time, goal)
part_two *= count

print( "part_two:", part_two )

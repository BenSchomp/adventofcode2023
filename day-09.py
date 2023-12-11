
FWD = 0
BACK = 1

def extrapolate( values, direction ):
  cur = None
  reduced = True
  for v in values:
    if not cur:
      cur = v
    else:
      if v != cur:
        reduced = False
        break

  if reduced:
    # base case
    return cur

  # keep going
  tmp = []
  for i,v in enumerate(values):
    if i == 0:
      continue
    tmp.append(v - values[i-1])

  if direction == FWD:
    return values[len(values)-1] + extrapolate( tmp, direction )
  else:
    return values[0] - extrapolate( tmp, direction )



part_one = part_two = 0
file = open("day-09.txt", 'r')
for line in file:
  values = list(map(lambda x: int(x), line.split()))

  part_one += extrapolate( values, FWD )
  part_two += extrapolate( values, BACK )


file.close()

print( "part_one:", part_one )
print( "part_two:", part_two )



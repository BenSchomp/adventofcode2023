class FarmMap:
  def __init__(self, source, dest):
    self.source_name = source
    self.dest_name = dest
    self.mappings = {} 

  def __str__(self):
    result = "%s:%s | " % (self.source_name, self.dest_name)
    for k, v in self.mappings.items():
      result += "%s %s | " % (k, v)
    return result

  def addMapping(self, dest_start, source_start, n):
    self.mappings[int(source_start)] = (int(dest_start), int(n))

  def convert( self, value ):
    for k,v in self.mappings.items():
      n = v[1]
      source_lo = k
      source_hi = source_lo + n - 1
      dest_lo = v[0]

      if value >= source_lo and value <= source_hi:
        offset = value - source_lo
        return( dest_lo+offset, self.dest_name)
        break

    return (value, self.dest_name)

# --- main --- #

seeds = []
maps = {}
part_one = part_two = None

filename = 'day-05.txt'
#filename = 'day-05.example'
file = open(filename, 'r')
for line in file:
  line = line.strip()
  if not line:
    continue

  parts = line.split()
  if parts[0] == "seeds:":
    seeds = parts[1:]
  elif parts[1] == "map:":
    (curSource, x, curDest) = parts[0].split('-')
    maps[curSource] = FarmMap(curSource, curDest)
  else:
    maps[curSource].addMapping( parts[0], parts[1], parts[2] )


file.close()

# --- part one --- #

for s in seeds:
  i = 'seed'
  x = int(s) 
  while i != 'location':
    (x, i) = maps[i].convert(x)

  if not part_one or x < part_one:
    part_one = x

print( "part_one:", part_one )

# --- part two --- #

seen = set()
seed_index = 0
while seed_index+1 < len(seeds):
  seed_start = int(seeds[seed_index])
  seed_range = int(seeds[seed_index+1])

  done = False
  for seed_offset in range(seed_range):
    x = seed_start + seed_offset
    #print( "* trying seed:%d" % x)

    k = None
    i = 'seed'
    while i != 'location':
      k = "%s:%i" % (i, x)
      if k in seen:
        done = True
        break

      (x, i) = maps[i].convert(x)
      seen.add(k)

    if done:
      break

    #print( "%s:%i !! done !!" % (i,x) )
    if not part_two or x < part_two:
      part_two = x

  seed_index += 2

print( "part_two:", part_two )

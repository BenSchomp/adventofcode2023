
totals = {'red':12, 'green':13, 'blue':14}

def checkGame( id, game ):
  for draws in game:
    draw = draws.split(',')
    for d in draw:
      c = d.strip().split(' ')
      if int(c[0]) > totals[c[1]]:
        return 0

  return int(id)

part_one = 0

file = open('day-02.txt', 'r')
for line in file:
  line = line.strip()
  (game_id, game) = line.split(':')
  part_one += checkGame( game_id.split(' ')[1], game.split(';') )
file.close()

print( "part_one:", part_one )


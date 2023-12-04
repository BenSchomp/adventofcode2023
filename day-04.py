
part_one = part_two = 0

file = open('day-04.txt', 'r')
for line in file:
  winning_numbers = set(())
  row = []
  line = line.strip()
  card = line.split(':')
  id = card[0].split(' ')[1]
  (winners, yours) = card[1].split('|')

  for w in winners.strip().split():
    winning_numbers.add(w)

  win_count = 0
  for y in yours.strip().split():
    if y in winning_numbers:
      win_count += 1

  if win_count > 0:
    part_one += pow(2, win_count-1)

file.close()

print( "part_one:", part_one )
print( "part_two:", part_two )

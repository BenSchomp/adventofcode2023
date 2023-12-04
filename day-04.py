
cards = []
part_one = 0

file = open('day-04.txt', 'r')
for line in file:
  winning_numbers = set()
  card = line.strip().split(':')
  (winners, yours) = card[1].split('|')

  for w in winners.split():
    winning_numbers.add(w)

  win_count = 0
  for y in yours.split():
    if y in winning_numbers:
      win_count += 1

  if win_count > 0:
    part_one += pow(2, win_count-1)

  cards.append( win_count )

file.close()
print( "part_one:", part_one )

# ------------ part two ------------ #

part_two = card_num = len(cards)
while card_num > 0:
  win_count = cards[card_num-1]
  for i in range(win_count):
    win_count += cards[card_num+i]

  cards[card_num-1] = win_count
  part_two += win_count

  card_num -= 1

print( "part_two:", part_two )


cardRank = {'2':2, '3':3, '4':4, '5': 5, '6':6, '7':7, '8':8, '9':9, \
            'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

class Hand:
  def __init__(self, cards, wager):
    self.cards = cards
    self.counts = {}
    self.score = 0
    self.wager = int(wager)

    self.scoreHand()

  def __eq__(self, other):
    return sorted(self.cards) == sorted(other.cards)

  def __lt__(self, other):
    if self.score != other.score:
      return self.score < other.score

    for i in range(5):
      a = cardRank[self.cards[i]]
      b = cardRank[other.cards[i]]
      if a != b:
        return a < b

    return False

  def scoreHand(self, part_two=False):
    self.counts = {}
    self.score = 0

    for i in range(5):
      cur = self.cards[i]
      if cur in self.counts:
        self.counts[cur] += 1
      else:
        self.counts[cur] = 1

    if part_two and 'J' in self.counts:
      # jacks are wild
      self.score += self.counts['J'] * 10
      self.counts['J'] = 0

    scores = sorted(self.counts.values(), reverse=True)
    self.score += scores[0]*10
    if len(scores) > 1:
      self.score += scores[1]


# --- main --- #

file = open("day-07.txt", 'r')
hands = []
for line in file:
  line = line.strip()
  parts = line.split()
  hands.append( Hand(parts[0], parts[1]) )

file.close()

# --- part one --- #

part_one = 0
for i, h in enumerate(sorted(hands)):
  part_one += (i+1) * h.wager

print( "part_one:", part_one )

# --- part two --- #

# jacks are now wild and lowest rank
cardRank['J'] = 1
for h in hands:
  h.scoreHand(part_two=True)

part_two = 0
for i, h in enumerate(sorted(hands)):
  part_two += (i+1) * h.wager

print( "part_two:", part_two )

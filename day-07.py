
cardRank = {'2':2, '3':3, '4':4, '5': 5, '6':6, '7':7, '8':8, '9':9, \
            'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
rankDisplay = {10:'T', 11:'J', 12:'Q', 13:'K', 14:'A'}


class Hand:
  def __init__(self, cards, wager):
    self.cards = cards
    self.hiGroup = None
    self.hiCount = 0
    self.loGroup = None
    self.loCount = 0
    self.kickers = []

    self.wager = int(wager)

    self.rankHand()

  def __str__(self):
    return self.getDisplayHand()

  def __eq__(self, other):
    return sorted(self.cards) == sorted(other.cards)

  def __lt__(self, other):
    selfRank = (self.hiCount * 10) + self.loCount
    otherRank = (other.hiCount * 10) + other.loCount
    if selfRank != otherRank:
      return selfRank < otherRank

    if self.hiGroup != other.hiGroup:
      return self.hiGroup < other.hiGroup

    if self.loGroup != other.loGroup:
      return self.loGroup < other.loGroup

    for i in range(len(self.kickers)):
      if self.kickers[i] != other.kickers[i]:
        return self.kickers[i] < other.kickers[i]

    return False

  def getRankDisplay(self, card):
    if card > 9:
      return rankDisplay[card]
    else:
      return str(card)

  def getDisplayHand(self):
    result = ''
    if self.hiGroup:
      c = self.getRankDisplay(self.hiGroup)
      for i in range(self.hiCount):
        result += c
    if self.loGroup:
      c = self.getRankDisplay(self.loGroup)
      for i in range(self.loCount):
        result += c
    for c in self.kickers:
      result += self.getRankDisplay(c)
    return result

  def rankHand(self):
    for i in range(5):
      count = 1
      cur = cardRank[self.cards[i]]
      if not cur in self.kickers:
        self.kickers.append(cur)
      for j in range(5):
        if i == j:
          continue

        if self.cards[i] == self.cards[j]:
          count += 1

      if count > 1:
        if count > self.hiCount:
          if cur != self.hiGroup:
            self.loGroup = self.hiGroup
            self.loCount = self.hiCount
            self.hiGroup = cur
          self.hiCount = count
        elif count == self.hiCount and cur != self.hiGroup:
          self.loCount = count
          if cur > self.hiGroup:
            self.loGroup = self.hiGroup
            self.hiGroup = cur
          else:
            self.loGroup = cur
        elif cur != self.hiGroup:
          if count > self.loCount:
            self.loCount = count
            self.loGroup = cur
          elif count == self.loCount:
            if cur > self.loGroup:
              self.loGroup = cur

    for i in [self.hiGroup, self.loGroup]:
      if i in self.kickers:
        self.kickers.remove(i)
    self.kickers.sort(reverse=True)

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
  print( i+1, h.getDisplayHand(), h.wager )
  part_one += (i+1) * h.wager

#for h in sorted(hands, reverse=True):
  #print( h, h.hiCount, h.loCount )

print( "part_one:", part_one )

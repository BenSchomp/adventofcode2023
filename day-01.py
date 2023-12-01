

NUMBERS = ['one','two','three','four','five','six','seven','eight','nine']

def getWordDigit( word ):
  for i,n in enumerate(NUMBERS):
    if word[:len(n)] == n:
      return i+1
  return None

def getTerm( word, part ):
  result = 0
  for i,c in enumerate(word):
    if c.isdigit():
      result += int(c)*10
      break
    elif( part == 2 ):
      d = getWordDigit( word[i:] )
      if d:
        result += d*10
        break

  for i,c in enumerate(reversed(word)):
    if c.isdigit():
      result += int(c)
      break
    elif( part == 2 ):
      d = getWordDigit( word[-i-1:] )
      if d:
        result += d
        break

  return result

part_one = part_two = 0

file = open('day-01.txt', 'r')
for line in file:
  line = line.strip()
  part_one += getTerm( line, 1 )
  part_two += getTerm( line, 2 )
file.close()

print( 'part one:', part_one )
print( 'part two:', part_two )

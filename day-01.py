
file = open('day-01.txt', 'r')

def getTerm_one( word ):
  result = 0
  for c in word:
    if c.isdigit():
      result += int(c)*10
      break

  for c in reversed( word ):
    if c.isdigit():
      result += int(c)
      break

  return result

NUMBERS = ['one','two','three','four','five','six','seven','eight','nine']

def getWordDigit( word ):
  for i,n in enumerate(NUMBERS):
    if word[:len(n)] == n:
      return i+1
  return None

def getTerm_two( word ):
  result = 0
  for i,c in enumerate(word):
    if c.isdigit():
      result += int(c)*10
      break
    else:
      d = getWordDigit( word[i:] )
      if d:
        result += d*10
        break

  for i,c in enumerate(reversed(word)):
    if c.isdigit():
      result += int(c)
      break
    else:
      d = getWordDigit( word[-i-1:] )
      if d:
        result += d
        break

  return result


part_one = part_two = 0
for line in file:
  line = line.strip()
  part_one += getTerm_one( line )
  part_two += getTerm_two( line )

file.close()

print( 'part one:', part_one )
print( 'part two:', part_two )

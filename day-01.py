
file = open('day-01.txt', 'r')

def getTerm( word ):
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

def convertLine( word ):
  word = word.replace( "one", "1" )
  word = word.replace( "two", "2" )
  word = word.replace( "three", "3" )
  word = word.replace( "four", "4" )
  word = word.replace( "five", "5" )
  word = word.replace( "six", "6" )
  word = word.replace( "seven", "7" )
  word = word.replace( "eight", "8" )
  word = word.replace( "nine", "9" )
  print( word )
  return word



part_one = part_two = 0
for line in file:
  line = line.strip()
  part_one += getTerm( line )
  part_two += getTerm( convertLine( line ) )

file.close()

print( 'part one:', part_one )
print( 'part two:', part_two )

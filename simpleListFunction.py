"""
The aim of code is to get a list where the last element get a
and on the begin.
Example a, b, c, d
Result a, b, c and d
"""
def modefication(theLitsElements):
 for i in range (len(theLitsElements)):
  if (i != len(theLitsElements)-1):
   print(theLitsElements[i])
  else:
   print('and '+theLitsElements[i])


spam=['apples', 'bananas', 'tofu', 'cats', 'mouse']
modefication(spam)
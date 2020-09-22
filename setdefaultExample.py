"""
how dictionary looks like
dictionary{key:value, key:value}
The target for this code is to count how
often some letters appears in a sentence
"""
import pprint

message = 'It was a day'

count = {}

for character in message:
 #this line create a key and a default value. For example first catch get 0
 #character, 0 --> I:0, t:0...
 count.setdefault(character, 0)
 #The value of a key increase +1. It means a key in our example a letter
 #was found once again increase the counter +1 for key key
 count[character] = count[character] + 1

print(count)
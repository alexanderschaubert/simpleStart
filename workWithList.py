# How can you assigne a hello in a liste on 3rd position?
spam = [2, 4, 6, 8, 10]
# first how the list looks like before we change it
print(spam)
spam[2] = 'hello'
# how the list looks like after manipulation
print(spam)

"""
Simple examples with list
"""
spam = ['a', 'b', 'c', 'd']
# '3'*2 is equal to 33. In next step 33/11 is 3. So spam on 3rd position is d
print(spam[int(int('3' * 2) / 11)])

# In the list from first element till second.
# Result is a,b
print(spam[:2])

bacon = [3.14, 'cat', 11, 'cat', True, 'cat']
print(bacon.index('cat'))
bacon.append(99)
print(bacon)
bacon.remove('cat')
print(bacon)

"""
Tupel
"""
tupleSimple = (42)
#Convert a list to tuple with tuple
fromListTuple = tuple(bacon)
print(fromListTuple.count('cat'))

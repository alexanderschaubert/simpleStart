wovels = ['a', 'e', 'e', 'o', 'u', 'i']
found = {}

#it's a very simple way how you can count wovels
#in dictionary
found['a']=0
found['a'] = found['a']+2
found['o']=0
found['o']=found['o']+1
print(found)

#next time something elegant solution
found.setdefault('b',0)
found.setdefault('a',2)
print(found)

# how to get key and value
# for k in found --> key
# found[k] --> is value
for k in found:
    print(k, 'was found ', found[k])

#how to access to data/value
print(found['a'])
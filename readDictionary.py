someDictionary = {'A':1, 'B':2, 'C':3}

for key, value in someDictionary.items():
    print(key + ' '+ str(value))

#what will happen if we just try to get values without .items
for a in someDictionary:
    print(a + '*')

#what will happen if we just try to get value and keys without .items
#The result is an error.
#for a, b in someDictionary:
#    print (a+' '+b)
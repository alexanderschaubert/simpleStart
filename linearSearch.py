import timeit
def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1

list = ('A','B','C')
starttime = timeit.default_timer()
print('B is in the list on position: ',linear_search(list, 'B'))
print("The time difference is :", timeit.default_timer() - starttime)
import timeit

def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.
    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1

list=('A','B','C')
starttime = timeit.default_timer()
print(binary_search(list,'B'))
print("The time difference is :", timeit.default_timer() - starttime)
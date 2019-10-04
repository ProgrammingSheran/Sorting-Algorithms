# Sorting algorithms
# sorting-algorithms.py
# Selection and Bubble sort algorithms written in Python

# These three sorting algorithms are my implemented versions of the selection algorithm
def selection_sort_one(a):

    '''
    >>> selection_sort_one([77, 9, 102, 99, 12])
    [9, 12, 77, 99, 102]
    '''

    for element in a:
        mi = a.index(element)
        for j in range(mi + 1, len(a)):
            if a[j] < a[mi]:
                mi = j

        if mi != a.index(element):
            a[a.index(element)], a[mi] = a[mi], a[a.index(element)]
    return a

def selection_sort_two(a):

    '''
    >>> selection_sort_two([77, 9, 102, 99, 12])
    [9, 12, 77, 99, 102]
    '''

    l = len(a)
    for i in range(l):
        minimum = i
        for j in range(minimum + 1, l):
            if a[j] < a[minimum]:
                minimum = j

        if minimum != i:
            a[i], a[minimum] = a[minimum], a[i]
    return a

def selection_sort_three(a):

    '''
    >>> selection_sort_three([77, 9, 102, 99, 12])
    [9, 12, 77, 99, 102]
    '''

    l = len(a)
    for i in range(l):
        minimum = i
        for j in range(minimum + 1, l):
            if a[j] < a[minimum]:
                minimum = j
        a[minimum], a[i] = a[i], a[minimum]

    return a

# ----------------------------------------------------------------------------------------------------------------------

# Wikipedia's implementation of the selection sort algorithm
def selectionsort(l): # Why variable 'l'? It's an array ('a')
    '''
    Overall confusing code!

    >>> bubble_sort_one([77, 9, 102, 99, 12])
    [9, 12, 77, 99, 102]
    '''
    for passesLeft in range(0,len(l)-1,+1): # No spaces, third parameter -> '+1' why? '1' is positive anyway
        min   = passesLeft # Spaces between variable and equal operator, min is a reserved built-in function
        for index in range(passesLeft+1,len(l),+1): # No spaces, again '+1' -> '1'
            if (l[index]<l[min]): # No spaces, brackets??? They have no business here!
                min = index # Again reserved built-in func
        l[min] , l[passesLeft] = l[passesLeft] , l[min] # No spaces, reserved built-in func
    return l

# I revised the Wikipedia implementation
def revised_selectionsort(a):

    '''
    >>> bubble_sort_one([77, 9, 102, 99, 12])
    [9, 12, 77, 99, 102]
    '''

    for passesLeft in range(0, len(a) - 1, 1):
        minimum = passesLeft
        for index in range(passesLeft + 1, len(a), 1):
            if a[index] < a[minimum]:
                minimum = index
        a[minimum], a[passesLeft] = a[passesLeft], a[minimum]
    return a

# You can have a look at the implementation (which i wouldn't recommend!)
# https://en.wikipedia.org/wiki/Talk:Selection_sort#Python

# ----------------------------------------------------------------------------------------------------------------------

# My implementations of the bubble sort algorithm

def bubble_sort_one(a):

    '''
    >>> bubble_sort_one([77, 9, 102, 99, 12])
    [9, 12, 77, 99, 102]
    '''

    for element in a:
        for j in range(len(a) - a.index(element) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a

def bubble_sort_two(a):
    '''
    >>> bubble_sort_two([77, 9, 102, 99, 12])
    [9, 12, 77, 99, 102]
    '''

    l = len(a)
    for i in range(l):
        for j in range(l - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a

if __name__ == "__main__":
    import doctest
    doctest.testmod()
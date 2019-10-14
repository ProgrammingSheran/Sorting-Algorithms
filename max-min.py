
def get_min(a):

    '''
    Get lowest item of a list
    :param a: Array given
    :returns: Lowest element of the array given

    >>> get_min([10, 102, 77])
    10
    '''

    l = len(a)
    for i in range(l - 1):
        for j in range(l - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a[0]

def get_max(a):

    '''
    Get highest item of a list
    :param a: Array given
    :returns: Highest element of the array given

    >>> get_max([7, 1, 99, 1782, 14])
    1782
    '''

    l = len(a)
    for i in range(l - 1):
        for j in range(l - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a[len(a) - 1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
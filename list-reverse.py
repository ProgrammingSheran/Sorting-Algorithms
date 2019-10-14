
def list_reverse(a: list) -> list:
    '''
    Reverses a list given as an array
    :param a: Array of numbers
    :returns: Reversed array

    >>> list_reverse([1, 2, 3])
    [3, 2, 1]
    '''

    length = len(a)
    for i in range(length):
        print(f"i: {i} --- a[i]: {a[i]}")
        a[i] = length
        length -= 1

    return a

if __name__ == "__main__":
    import doctest
    doctest.testmod()
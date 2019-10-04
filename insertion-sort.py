from random import randint

def insertion_sort(a):
	'''Insertion-Sort algorithm
	
	>>> insertion_sort([99, 21, 102, 8, 7, 3, 1, 9])
	[1, 3, 7, 8, 9, 21, 99, 102]
	'''

	for i in range(len(a)):
		val = a[i]
		j = i
		while j > 0 and a[j - 1] > val:
			a[j] = a[j - 1]
			j -= 1

		a[j] = val

	return a

if __name__ == '__main__':
	import doctest
	doctest.testmod()
from random import randint

def quick_sort(a):

	'''
	>>> quick_sort([99, 21, 79, 27, 92, 102])
	[21, 27, 79, 92, 99, 102]
	'''

	l = len(a)
	left =  []
	equal = []
	right = []

	if l > 1:
		pivotElement = a[randint(0, l - 1)]
		for i in range(l):
			if a[i] < pivotElement:
				left.append(a[i])
			elif a[i] == pivotElement:
				equal.append(a[i])
			elif a[i] > pivotElement:
				right.append(a[i])

		return quick_sort(left) + equal + quick_sort(right)
		
	else:
		return a

if __name__ == '__main__':
	import doctest
	doctest.testmod()
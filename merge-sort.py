from random import randint

def merge_sort(a):

	'''Merge-Sort algorithm

	>>> merge_sort([77, 21, 102, 807, 1, 9])
	[1, 9, 21, 77, 102, 807]
	'''

	if len(a) <= 1:
		return a
	else:
		divide = len(a) // 2
		first = a[:divide]
		second = a[divide:]
		l_list = merge_sort(first)
		r_list = merge_sort(second)
		return merge(l_list, r_list)

def merge(l_list, r_list):

	'''Merging l_list and r_list together'''

	new_list = []
	
	while len(l_list) and len(r_list) > 0:
		if l_list[0] <= r_list[0]:
			new_list.append(l_list[0])
			l_list.remove(l_list[0])
		else:
			new_list.append(r_list[0])
			r_list.remove(r_list[0])

	while len(l_list) > 0:
		new_list.append(l_list[0])
		l_list.remove(l_list[0])

	while len(r_list) > 0:
		new_list.append(r_list[0])
		r_list.remove(r_list[0])

	return new_list

if __name__ == '__main__':
	import doctest
	doctest.testmod()
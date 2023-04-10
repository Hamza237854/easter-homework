from random import randint

def bubble_sort(l):
	sorted = 0
	while not sorted:
		sorted = 1
		for i in range(len(l)-1):
			if l[i] > l[i+1]:
				sorted = 0
				l[i], l[i+1] = l[i+1], l[i]
	
	return l


def selection_sort(l):
	for i in range(len(l)):
		min = i
		for j in range(i, len(l)):
			if l[j] < l[i]:
				min = j
		l[i], l[min] = l[min], l[i]
	return l


l1 = [randint(0, 200) for i in range(0, 30)]
l2 = l1

print(l1)
l1 = bubble_sort(l1)
print(l1)

l2 = selection_sort(l2)
print(l2)

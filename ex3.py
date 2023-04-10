from random import randint

def merge(r, l):
	res = []
	i = 0
	j = 0
	
	while i < len(l) and j < len(r):
		if l[i] <= r[j]:
			res.append(l[i])
			i = i+1
		else:
			res.append(r[j])
			j = j+1
	
	res = res + l[i::]
	res = res + r[j::]
	return res


def merge_sort(l):
	if len(l) < 2:
		return l
	else:
		mid = len(l) // 2
		left = merge_sort(l[:mid])
		right = merge_sort(l[mid:])
		return merge(left, right)

l1 = [randint(0, 200) for i in range(100)]

print(l1)

l1_sorted = merge_sort(l1)
print(l1_sorted)

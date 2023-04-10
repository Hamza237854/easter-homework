from random import randint

l = [randint(-200, 200) for i in range(1000)]

print(l)


sorted = 0

while not sorted:
	sorted = 1
	for i in range(len(l)-1):
		if l[i] > l[i+1]:
			sorted = 0
			l[i], l[i+1] = l[i+1], l[i]


print(l)

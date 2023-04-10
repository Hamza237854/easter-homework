from random import randint

t = tuple([randint(0, 10) for i in range(30)])
print(t)

d = {str(i) : 0 for i in range(11)}
print(d)

for i in t:
	d[str(i)] += 1

print(d)

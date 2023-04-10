from random import randint
import time

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


l1 = [randint(0, 200) for i in range(300)]
l2 = l1

start_time_1 = time.time()
l1 = merge_sort(l1)
end_time_1 = time.time()



start_time_2 = time.time()
l2.sort()
end_time_2 = time.time()


print("merge sort:",end_time_1 - start_time_1)
print("built in:",end_time_2 - start_time_2)

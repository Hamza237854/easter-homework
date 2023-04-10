from random import randint
import time

l = [randint(-200, 200) for i in range(1000)]
l2 = l


start_time_1 = time.time()
sorted = 0
while not sorted:
        sorted = 1
        for i in range(len(l)-1):
                if l[i] > l[i+1]:
                        sorted = 0
                        l[i], l[i+1] = l[i+1], l[i]

end_time_1 = time.time()



start_time_2 = time.time()
l2.sort()
end_time_2 = time.time()



print("insertion:",end_time_1 - start_time_1)
print("built in:",end_time_2 - start_time_2)

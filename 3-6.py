import random

arr = []
for i in range(15):
    arr.append(random.randint(-20, 20))
print(arr)
min_ind = arr.index(min(arr))
max_ind = arr.index(max(arr))
print(min_ind, max_ind)
if min_ind > max_ind:
    min_ind, max_ind = max_ind, min_ind

print(arr[min_ind + 1:max_ind])

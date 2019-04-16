"""
 Определить, какое число в массиве встречается чаще всего.
"""

import random

arr = []
for i in range(10):
    arr.append(random.randint(1, 20))
print(arr)

num = arr[0]
max_chs = 1
for i in range(len(arr) - 1):
    chs = 1
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            chs += 1
        if chs > max_chs:
            max_chs = chs
            num = arr[i]
if max_chs > 1:
    print(max_chs, 'раз встречается число', num)
else:
    print('числа не встречаются более одного раза')

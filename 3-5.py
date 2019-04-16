"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
"""
import random

arr = []
for i in range(15):
    arr.append(random.randint(-20, 20))
print(arr)
i = 0
index = -1
for i in range(len(arr)):
    if arr[i] < 0 and index == -1:
        index = i
    elif arr[i] < 0 and arr[i] > arr[index]:
        index = i
    i += 1

print(index, ':', arr[index])

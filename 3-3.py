"""
 В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

arr = []
for i in range(10):
    arr.append(random.randint(1, 20))
print(arr)
mn = min(arr)
mx = max(arr)
imn = arr.index(mn)
imx = arr.index(mx)
print(imn, imx)
imn, imx = imx, imn
print(arr)

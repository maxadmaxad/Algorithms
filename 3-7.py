"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""
import random

a = []
b = []
for i in range(15):
    a.append(random.randint(-20, 20))
print(a)
for j in range(2):
    b.append(min(a))
    a.remove(min(a))
print(b)

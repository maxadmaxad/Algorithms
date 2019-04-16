"""
 В диапазоне натуральных чисел от 2 до 99 определить,
 сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

a = []
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            a.append(j)
print(f"2 - {a.count(2)}")
print(f"3 - {a.count(3)}")
print(f"4 - {a.count(4)}")
print(f"5 - {a.count(5)}")
print(f"6 - {a.count(6)}")
print(f"7 - {a.count(7)}")
print(f"8 - {a.count(8)}")
print(f"9 - {a.count(9)}")

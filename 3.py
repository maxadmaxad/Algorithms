# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

k, b = float, float
k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1
print(f"y={k}*x+{b}")

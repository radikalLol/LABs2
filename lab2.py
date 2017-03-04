import math

a = float(input("Введите число из которого нужно извлечь корень: "))
y = 0
x = a

while True:
    y = (x + a/x)/2
    if math.fabs(x - y) == 0: break

    x = y
    print(float("%.2f" % x))

a = float(input("Введите число из которого нужно извлечь корень: "))
while True:
    for x in range(1, 999, 1):
        y = 1/2 * (x + a/x)
    if y == x/a:
        print("%.2f" % y)

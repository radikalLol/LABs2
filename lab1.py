def plus(x, y):
    print("%.2f" % (x + y))

def minus(x, y):
    print("%.2f" % (x - y))


def division(x, y):
    print("%.2f" % (x / y))


x = float(input("x="))
y = float(input("y="))

print('Знак (+,-,*,/): ')


calculations = {
        '+': plus,
        '-': minus,
        '/': division
}

calc_item = calculations[]
calc_item(x, y)


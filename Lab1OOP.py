class A:

    def plus(x, y):
        print("%.2f" % (x + y))

    def minus(x, y):
        print("%.2f" % (x - y))

    def multiplication(x, y):
        print("%.2f" % (x * y))

    def division(x, y):
        print("%.2f" % (x / y))

    x = float(input("x="))
    y = float(input("y="))

    calculations = {
        '+': plus,
        '-': minus,
        '*': multiplication,
        '/': division
     }

    calc_item = calculations[input("Знак (+,-,*,/): ")]
    calc_item(x, y)

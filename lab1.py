x = float(input("x="))
y = float(input("y="))
print('Знак (+,-,*,/): ')
calculations = {
        '+': print("%.2f" % (x+y)),
        '-': print("%.2f" % (x-y)),
        '/': print("%.2f" % (x/y))
    }

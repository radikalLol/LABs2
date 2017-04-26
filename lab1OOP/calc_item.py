
class clalc_item:

    def calculation(self, x, y, oper):

        if oper == '+':
            self.__calc__ = self.plus(x, y)

        elif oper == '-':
            self.__calc__ = self.minus(x, y)

        elif oper == '*':
            self.__calc__ = self.multiplication(x, y)

        elif oper == '/':
            self.__calc__ = self.division(x, y)

        else:
            print('Знак (+,-,*,/): ')
            self.__calc__ = None

        self.getCalc()

    def plus(self, x, y):
       return x + y

    def minus(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        return x / y

    def getCalc(self):
        return self.__calc__

    def showCalc(self):
        print('Answer: {}'.format(self.getCalc()))

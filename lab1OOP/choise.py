import sys

class Choice():

    def __init__(self, x, y, oper, calc):
        self.__signal__ = 1
        self.x = x
        self.y = y
        self.oper = oper
        self.calc = calc

    def setVar(self):
        self.y.setNum(float(input()))
        self.oper.setOper(str(input()))

    def newChoice(self, choice):

        if choice == 1 and self.calc.getAnswer() != None:  # Продолжение работы с ответом
            print('Enter number 2 and operation:')
            self.setVar()
            self.calc.calculation(self.calc.getAnswer(), self.Y.getNum(), self.oper.getOper())

        elif choice == 1 and self.calc.getAnswer() == None:
            print('Error in first number! Please, try again.')
            return

        elif choice == 2:  # Новое выражение
            print('Enter number 1, number 2 and operation:')
            self.x.setNum(float(input()))
            self.setVar()
            self.calc.calculation(self.x.getNum(), self.y.getNum(), self.oper.getOper())

        elif choice == 3:  # Выход
            sys.exit()
        else:
            print('Error! Enter 1, 2 or 3')  # Ошибка ввода

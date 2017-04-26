from operation import Operation
from calc_item import clalc_item
from number import Number
from choise import Choice

class Application():

    def __init__(self):

        self.x = Number(float(input('x=')))
        self.y = Number(float(input('y=')))
        self.oper = Operation(str(input('Знак (+,-,*,/): ')))
        self.calc = clalc_item()
        self.calc.calculation(self.x.getNum(), self.y.getNum(), self.oper.getOper())
        self.choice = Choice(self.x, self.y, self.oper, self.calc)

    def run(self):

        while True:
            self.calc.showCalc()
            self.choice = Choice(self.x, self.y, self.oper, self.calc).newChoice(int(input()))

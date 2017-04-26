from number import Number
from lastN import LastN
from calculation import Calc

class Application:

    def __init__(self):
        self.a = Number()
        self.x = LastN()
        self.calc = Calc()
        self.calc.setAns(self.x.getLA(), self.a.getNum())

    def run(self):
        while abs(self.x.getLA() - self.calc.getAns()) > 0.00001:

            self.x.setLA(self.calc.getAns())
            self.calc.setAns(self.x.getLA(), self.a.getNum())

        self.calc.showAns(self.a)

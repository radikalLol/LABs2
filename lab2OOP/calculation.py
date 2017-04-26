import math

class Calc:

    def setAns(self, x, a):
        self.y = ( x + a / x) / 2

    def getAns(self):
        return self.y

    def showAns(self, a):
        print('{}'.format(self.getAns()))

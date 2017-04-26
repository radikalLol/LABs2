class Operation:
    def __init__(self, oper):

     self.__oper__ = oper

    def getOper(self):
        return self.__oper__

    def setOper(self, oper):
        self.__oper__ = oper

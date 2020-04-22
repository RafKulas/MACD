class Human:
    __money = 0
    __actions = 1000
    __data = None
    __day = 0
    __close = 0

    def __init__(self, data):
        self.__data = data
        self.__close = self.__data.getClose()[self.__day]

    def buy(self):
        amount = self.__money // self.__data.getClose()[self.__day]
        self.__actions += amount
        self.__money -= amount * self.__data.getClose()[self.__day]

    def sell(self):
        self.__money += self.__actions * self.__data.getClose()[self.__day]
        self.__actions = 0

    def nextDay(self):
        self.__close = self.__data.getClose()[self.__day]
        self.__day += 1

    def showEarn(self):
        print((self.__money+self.__actions*self.__close)/(self.__data.getClose()[0]*10))

    def printMoney(self):
        print(self.__money + self.__actions * self.__close)

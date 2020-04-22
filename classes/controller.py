class Controller:
    __data = None
    __human = None
    __mode = 0

    def __init__(self, data, human, mode=0):
        self.__data = data
        self.__human = human
        self.__mode = mode

    def stock(self):
        self.__human.printMoney()
        for index in range(self.__data.getLength()):
            if index < 30:
                self.__data.appMACD(0, 0)
                self.__data.appSignal(0, 0)
                self.__data.appDiff(0, 0)
                self.__human.nextDay()
            elif index < 40:
                self.__data.appMACD(index)
                self.__data.appSignal(0, 0)
                self.__data.appDiff(0, 0)
                self.__human.nextDay()
            else:
                self.__data.appMACD(index)
                self.__data.appSignal(index)
                self.__data.appDiff(index)
                if self.__data.getDiff(index) * self.__data.getDiff(index - 1) < 0 and self.__mode >= 2:
                    if self.__data.getDiff(index) < 0 and self.__data.getMACD(index) > 0 and self.__data.getMACD(index) \
                            - self.__data.getMACD(index - 1) < 0 and self.__data.getClose()[index] - \
                            self.__data.getClose()[index - 1] > 0:
                        self.__human.buy()
                    elif self.__data.getDiff(index) > 0 and self.__data.getMACD(index) < 0 and self.__data.getMACD(
                            index) \
                            - self.__data.getMACD(index - 1) > 0 and self.__data.getClose()[index] - \
                            self.__data.getClose()[index - 1] < 0:
                        self.__human.sell()
                elif self.__data.getDiff(index) * self.__data.getDiff(index - 1) < 0 and self.__mode == 1:
                    if self.__data.getDiff(index) < 0 and self.__data.getMACD(index) > 0:
                        self.__human.buy()
                    elif self.__data.getDiff(index) > 0 and self.__data.getMACD(index) < 0:
                        self.__human.sell()
                elif self.__data.getDiff(index) * self.__data.getDiff(index - 1) < 0 and self.__mode <= 0:
                    if self.__data.getDiff(index) < 0:
                        self.__human.buy()
                    elif self.__data.getDiff(index) > 0:
                        self.__human.sell()

                self.__human.nextDay()
        self.__human.printMoney()
        self.__human.showEarn()

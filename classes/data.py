import pandas as pd
import numpy as np


class Data:
    __data = None
    __macd = []
    __signal = []
    __diff = []
    __length = 0

    def getDate(self):
        return self.__data['Date']

    def getClose(self):
        return self.__data['Close']

    def __init__(self, name):
        self.__data = pd.read_csv(name)
        self.__data['Date'] = pd.to_datetime(self.__data['Date'])
        self.__length = len(self.__data['Date'])

    def getLength(self):
        return self.__length

    def appMACD(self, index, mode=1):
        if mode == 1:
            self.__macd.append(self.ema(12, index, self.__data['Close']) - self.ema(26, index, self.__data['Close']))
        else:
            self.__macd.append(np.nan)

    def getMACD(self, index=-1):
        if index == -1:
            return self.__macd
        else:
            return self.__macd[index]

    def appSignal(self, index, mode=1):
        if mode == 1:
            self.__signal.append(self.ema(9, index, self.__macd))
        else:
            self.__signal.append(np.nan)

    def getSignal(self, index=-1):
        if index == -1:
            return self.__signal
        else:
            return self.__signal[index]

    def appDiff(self, index, mode=1):
        if mode == 1:
            self.__diff.append(self.__signal[index] - self.__macd[index])
        else:
            self.__diff.append(0)

    def getDiff(self, index=-1):
        if index == -1:
            return self.__diff
        else:
            return self.__diff[index]

    @staticmethod
    def ema(n, m, data):  # n - okresowosc, m - do ktorego dnia
        ema_nominator = 0
        ema_denominator = 0
        const = 1 - (2 / (n + 1))
        for i in range(n + 1):
            ema_nominator *= const
            ema_denominator *= const
            ema_nominator += data[m - n + i]
            ema_denominator += 1
        return ema_nominator / ema_denominator

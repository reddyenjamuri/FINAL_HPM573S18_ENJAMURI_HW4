from enum import Enum
import numpy as np


class Coin(Enum):
    TAIL = 1
    HEAD = 0


class Game(object):
    def __init__(self, id, coin_probability):

        self._id = id
        self._coin_probability = coin_probability
        self._Coin = Coin.TAIL
        self._expectedCost = 250

    def simulate(self, n_flips):
        t = 0

        while self._Coin == Coin.TAIL and t < n_flips:

            if np.random.sample() < self.coin_probability:
                self._Coin = Coin.TAIL
            else:
                np.random.sample() > self.coin_probability
                self._Coin = Coin.HEAD

                t += 1

    def get_expectedCost(self):
        return self._expectedCost

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.style as style
import math
import random
from IPython.core.display import HTML
import poisson_only as poi
import seaborn as sn
import DictWithArray as dwa
import ramdom_walk as rw


class Man:
    def __init__(self, x, y, area, areal):
        self.x = x
        self.y = y
        self.area = area
        self.areal = list(areal)


class Init(user):
    w = 1  # 目標區域權重
    a = 1
    b = 0.3
    long = len(user.areal)
    if (5 in user.areal) is True:
        long += 1*w
    k1 = 1  # 目標區域數
    k = 9  # 所有區域數
    CD = len(user.areal)/k1
    CP = long/k
    F = a * CP + b * CD


if __name__ == '__main__':
    user = Man(1, 2, 3, [0, 1, 2])
    b = 3 in a.areal
    if b is False:
        print("ta")
        user.areal.append(5)
    Init(user)
    print(user.areal, b)
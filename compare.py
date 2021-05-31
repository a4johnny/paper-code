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


def pick(user, needk):
    picker = []
    pickerarea = []
    for i in user:
        stop = 0
        if len(picker) < needk:
            picker.append(i.F)
            pickerarea.append(i.area)
        elif len(picker) >= needk:
            if i.F > min(picker):
                pos = picker.index(min(picker))
                picker[pos] = i.F
                pickerarea[pos] = i.area
    # for i in picker:
    #     print(i)
    # print(len(picker))
    # print("-------------------------")
    # for i in user:
    #     print(i.F, i.area)
    return picker


def init(user):
    w = 1  # 目標區域權重
    a = 1
    b = 0.3
    for i in user:
        long = len(i.areal)
        if (5 in i.areal) is True:
            long += w
        k1 = 1  # 目標區域數
        k = 9  # 所有區域數
        CD = len(i.areal)/k1
        CP = long/k
        i.F = a * CP + b * CD
    return user


if __name__ == '__main__':
    needk = 250
    user, area = rw.userinit(9000)
    for n in range(5):
        user, area = rw.rw(user, area)
        for i in user:
            if i.area not in i.areal:
                i.areal.append(i.area)
    # b = 3 in a.areal
    # if b is False:
    #     print("ta")
    #     user.areal.append(5)
    # print(user.areal, b)
    user = init(user)
    p = pick(user, needk)
    print(len(p))


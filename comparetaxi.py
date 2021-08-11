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
import ramdom_taxi as rw


def pick(user, needk, time):
    picker = []
    pickerarea = []
    for i in user:
        stop = 0
        if len(picker) < needk:
            picker.append(i.F)
            if time < len(i.areal):
                pickerarea.append(i.areal[time])
            else:
                pickerarea.append(i.area)
        elif len(picker) >= needk:
            if i.F > min(picker):
                pos = picker.index(min(picker))
                picker[pos] = i.F
                if time < len(i.areal):
                    pickerarea[pos] = i.areal[time]
                else:
                    pickerarea[pos] = i.area
    # for i in picker:
    #     print(i)
    # print(len(picker))
    # print("-------------------------")
    # for i in user:
    #     print(i.F, i.area)
    return picker, pickerarea


def init(user, time):
    w = 5  # 目標區域權重
    a = 1
    b = 0.3
    for i in user:
        areal = []
        for ii in range(time):
            if time > len(i.areal):
                continue
            if i.areal[ii] not in areal:
                areal.append(i.areal[ii])
        long = len(areal)
        if (1 in areal) is True:
            long += w
        k1 = 1  # 目標區域數
        k = 6  # 所有區域數
        CD = len(areal)/k1
        CP = long/k
        if CD == 0:
            i.F = a * CP
        else:
            i.F = a * CP + b * math.log(CD)
    return user


if __name__ == '__main__':
    needk = 200
    coveragelist = []
    nmlist = []
    user = rw.start()

    for time in range(500):
        user = init(user, time)
        p, pa = pick(user, needk, time)
        nm = 0
        for i in pa:
            if i is 1:
                nm += 1

        coverage = nm/200
        nmlist.append(nm)
        coveragelist.append(coverage)
        print('coverage:', coverage, 'time:', time, len(user[time+1].areal))

    x = np.arange(500)
    plt.plot(x, nmlist)
    plt.ylim([0, 600])
    plt.grid()
    plt.show()
    print('nm:', nmlist)
    print('coverage:', coveragelist)
    print(round(np.mean(coveragelist), 3))


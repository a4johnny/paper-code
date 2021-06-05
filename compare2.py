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
    pickerf = []
    pickerarea = []
    for i in user:
        stop = 0
        if len(pickerf) < needk:
            picker.append(i)
            pickerf.append(i.F)
            pickerarea.append(i.area)
        elif len(pickerf) >= needk:
            if i.F > min(pickerf):
                pos = pickerf.index(min(pickerf))
                picker[pos] = i
                pickerf[pos] = i.F
                pickerarea[pos] = i.areal
    # for i in picker:
    #     print(i)
    # print(len(picker))
    # print("-------------------------")
    # for i in user:
    #     print(i.F, i.area)
    return picker, pickerarea


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
        i.F = a * CP + b * math.log(CD)
    return user


if __name__ == '__main__':
    needk = 500
    coveragelist = []
    nmlist = []
    user, area = rw.userinit(9000)
    for time in range(100):
        for n in range(5):
            user, area = rw.rw(user, area)
            for i in user:
                if i.area not in i.areal:
                    i.areal.append(i.area)

        user = init(user)
        p, pa = pick(user, needk)
        nm = 0
        for i in range(needk):
            if (5 in p[i].areal) is True:
                nm += 1

        coverage = nm/needk
        for iii in range(5):
            nmlist.append(nm)
            coveragelist.append(coverage)
        print('coverage:', coverage, 'time:', time, user[1].areal)
    x = np.arange(500)
    plt.plot(x, nmlist)
    plt.ylim([0, 500])
    plt.grid()
    # plt.show()
    print('nm:', nmlist)
    print('coverage:', coveragelist)
    print(round(np.mean(coveragelist), 3))


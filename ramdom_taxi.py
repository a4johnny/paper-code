import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.style as style
import math
import random
from IPython.core.display import HTML
import poisson_oneTOmany2 as poi
import seaborn as sn


# 隨機投放
class Man:
    def __init__(self, area):
        self.area = area
        self.areal = []
        self.F = 0


def start():
    num = 105
    turedata = -1
    turedatalist = []
    people = 0
    user = []

    for ii in range(100000):
        time = 0
        try:
            a = open('./Taxi/Taxi_' + str(num), mode='r')
            num += 1
            # a = open('./Taxi/Taxi_105', mode='r')
        except IOError:
            num += 1
            continue

        print(num)
        turedata += 1
        if turedata > 6000:
            continue

        u = Man(0)
        for i in a.readlines():
            if time < 500:
                i2 = i.split(",")
                if 121.43 <= float(i2[2]) <= 121.493 and 31.19 <= float(i2[3]) <= 31.247:
                    u.area = 1
                    u.areal.append(u.area)
                elif float(i2[2]) < 121.43:
                    u.area = 2
                    u.areal.append(u.area)
                elif float(i2[2]) > 121.493:
                    u.area = 3
                    u.areal.append(u.area)
                elif float(i2[3]) > 31.247:
                    u.area = 4
                    u.areal.append(u.area)
                elif float(i2[3]) < 31.19:
                    u.area = 5
                    u.areal.append(u.area)
                else:
                    u.area = 6
                    u.areal.append(u.area)
                time += 1
            else:
                break
        a.close()
        user.append(u)
    return user


if __name__ == '__main__':  # 此程式當主程式執行時，從這行開始
    user, areacount = userinit(100)
    for ii in range(20):
        rw(user, areacount)
        # for iii in range(10):
        #     areacount[iii] = 0

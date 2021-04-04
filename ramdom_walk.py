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


class Man:
    def __init__(self, x, y, area):
        self.x = x
        self.y = y
        self.area = area


def addman(areacount, user):
    addn = random.randint(200, 300)
    for i in range(addn):
        u = Man(random.randint(0, 8), random.randint(0, 8), 0)
        u.area = areajudge(u)
        areacount[u.area] += 1
        user.append(user)
    print("i am working")

def areajudge(u):
    if u.x < 3:
        if u.y < 3:
            u.area = 1
        elif 3 <= u.y <= 5:
            u.area = 4
        elif 6 <= u.y <= 8:
            u.area = 7
    elif 3 <= u.x <= 5:
        if u.y < 3:
            u.area = 2
        elif 3 <= u.y <= 5:
            u.area = 5
        elif 6 <= u.y <= 8:
            u.area = 8
    elif 6 <= u.x <= 8:
        if u.y < 3:
            u.area = 3
        elif 3 <= u.y <= 5:
            u.area = 6
        elif 6 <= u.y <= 8:
            u.area = 9
    elif u.x > 8 or u.y > 8 or u.x < 0 or u.y < 0:
        u.area = 0

    return u.area


def rw(user, areacount):  # 隨機亂走
    for i in range(len(user)):
        LorR = random.randint(0, 1)
        TorB = random.randint(0, 1)
        rangeX = random.randint(0, 5)
        rangeY = random.randint(0, 5)

        long = len(user)
        if i >= long:
            break

        if LorR == 1:
            user[i].x += rangeX
        elif LorR == 0:
            user[i].x -= rangeX

        if TorB == 1:
            user[i].y += rangeY
        elif TorB == 0:
            user[i].y -= rangeY

        user[i].area = areajudge(user[i])

        if user[i].area == 0:
            del user[i]
        elif user[i].area != 0:
            areacount[user[i].area] += 1

    print("areacount", areacount)
    addman(areacount, user)


def userinit(n):  # n現在區域內總人數
    user = []

    areacount = []
    for i in range(1, 11, 1):  # 起使 結束 地增值
        areacount.append(0)

    for i in range(n):
        u = Man(random.randint(0, 8), random.randint(0, 8), 0)
        u.area = areajudge(u)
        areacount[u.area] += 1
        if u.area == 0:
            print(u.x, u.y)
        user.append(u)
    return user, areacount


if __name__ == '__main__':  # 此程式當主程式執行時，從這行開始
    for i in range(1):
        user, areacount = userinit(3000)
        rw(user, areacount)
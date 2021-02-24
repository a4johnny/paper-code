import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.style as style
import math
from IPython.core.display import HTML


def Pcal (delp, trueN):
    style.use('fivethirtyeight')
    k = int(delp)
    print("pppk", k)
    n = trueN
    t = 5
    #p = k/n

    count = 0
    pp = []
    print("人數:", n)
    for i in range(10000) :
        count = count + 0.0001
        pp.append(count)

    bb = []
    bb2 = []
    bbb3 = []
    tempgod = 0
    thePP = 0
    for p in pp:
        mu = n * p * t
        b = stats.poisson.pmf(k, mu)
        bb.append(b)  #不同p達成相同k的機率 => bb
        ko = math.sqrt(k) # poisson 標準差 > 期望值是樣本母數=變異數，標準差=變異數開根號
        temp = 0
        if b > 0.005:
            bbb = []
            for kk in range(int(k - 1*ko), int(k + 2*ko), 1) : #平均值往上下找三個標準差  同p不同k
                b = stats.poisson.pmf(kk, mu)  #計算此k下此p機率
                temp = temp + b
                bbb.append(b) #此p下不同k總計
            bbb3.append(bbb) #二維陣列 紀錄所有p不同k
            if temp > tempgod : #找到累積最大值時的p (thePP)
                tempgod = temp
                thePP = p
        bb2.append(temp) #紀錄

    # plt.plot(np.arange(10000), bb2)
    # plt.show()
    print("thePP : ", thePP)
    return int(thePP*10000)

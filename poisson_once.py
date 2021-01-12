import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.style as style
import math
from IPython.core.display import HTML

def Pcalculate ():
    style.use('fivethirtyeight')

    k = 1500
    n = 3000
    t = 5
    p = k/n

    count = 0
    pp = []
    #for i in range(1000) :
    #    count = count + 0.001
    #    pp.append(count)
    for i in range(1000) :
        count = count + 0.001
        pp.append(count)

    bb = []
    bb2 = []
    bbb3 = []
    tempgod = 0
    thePP = 0
    for p in pp :
        mu= n * p * t
        b = stats.poisson.pmf(k, mu)
        bb.append(b)  #不同p達成相同k的機率 => bb
        ko = math.sqrt(k) # poisson 標準差 > 期望值是樣本母數=變異數，標準差=變異數開根號
        temp = 0
        num = 0
        bbb = []
        for kk in range(int(k - 1*ko), int(k + 2*ko), 1) : #平均值往上下找三個標準差  同p不同k
            b = stats.poisson.pmf(kk, mu)  #計算此k下此p機率
            temp = temp + b
            bbb.append(b) #此p下不同k總計
        bbb3.append(bbb) #二維陣列 紀錄所有p不同k
        num = num + 1
        if temp > tempgod : #找到累積最大值時的p (thePP)
            tempgod = temp
            thePP = p
        bb2.append(temp) #紀錄

    a = plt.bar(np.arange(1000), bb)
    plt.show()
    aa = plt.bar(np.arange(1000), bb2)
    plt.show()
    print("thePP : ", thePP)

    b = stats.poisson.pmf(k, mu)
    c = stats.poisson.pmf(np.arange(k), mu)
    plt.show()
    return thePP

if __name__ == "__main__":
   theP = Pcalculate()

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.style as style
import math
import random
from IPython.core.display import HTML

p = 4200
needK = 100 # k=2000
needpartK = 100/5
countlist = []
kp = 1 # 原本是 0.0001 不過這裡放大 10000 倍
low = 0
lowlist = []
largelist = []
for i in range(100) : #做100次
    count = 0
    partlist = []
    nextPlist = []
    plist = []
    coveragelist = []
    lifenumlist = []
    p = 4000
    lifetime = {}
    for num in range(200): #lifetime 初始化
        lifetime[num] = -1

    for ii in range(5) : #5個time slot
        NowIsEmpty = [] #紀錄 那些life以扣光 位置要填補
        lifenum = 0 #現有數量
        totalLife = 0
        if ii != 0: #第二輪開始資料衰減
            for num in range(200):
                if lifetime[num] == -1 or lifetime[num] == 0:
                    lifetime[num] = -1
                elif lifetime[num] > 0:
                    lifetime[num] = lifetime[num] - 1
                    totalLife = totalLife + lifetime[num]
                    lifenum = lifenum + 1

        for iii in range(50) : # n=1000 有幾個人
            if random.randint(1, 10000) <= p:
                count = count + 1
                for num in range(200):
                    if lifetime[num] == -1:
                        lifetime[num] = 5
                        break
        partlist.append(count)
        #校正P
        nextP = 0
        if count >= needpartK * (ii+1) :
            nextP = (needK / count) * (1/ (5-ii) ) * (count - needpartK*(ii+1) ) * -1 * kp
            # (1/ (5-ii) )
        elif count < needpartK * (ii+1) :
            nextP = 20 * (needK / count) * (1 / (5-ii) ) * (needpartK*(ii+1) - count ) * kp
        nextPlist.append(round(nextP/10000, 5))
        p = p + round(nextP, 0) #round 四捨五入
        plist.append(round(p/10000, 5))

        coverage = lifenum/100 - (1 - totalLife/(5*100))*0.01
        lifenumlist.append(lifenum)
        coveragelist.append(round(coverage, 4))

    if count < 100 :
        low = low + 1
        lowlist.append(100 - count)
    elif count >= 100 :
        largelist.append(count - 100)

    print("partlist: ", partlist)
    print("nextPlist: ", nextPlist)
    print("plist", plist)
    print("count", count)
    print("lifenum:", lifenumlist)
    print("coverage:", coveragelist)
    print("----------------------------")
print(low)
print(lowlist)
print(largelist)

temp = 0
for i in lowlist :
    temp = temp + i
if len(lowlist) != 0:
    ave = temp/len(lowlist)
else:
    ave = temp/1
print(ave)

temp = 0
for i in largelist :
    temp = temp + i
if len(largelist) != 0:
    ave = temp/len(largelist)
else:
    ave = temp/1
print(ave)
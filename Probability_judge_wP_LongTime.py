import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.style as style
import math
import random
from IPython.core.display import HTML

fu = 0
p = 1000
needK = 1000 # k=2000
originK = 2000
n = 2000 # n=1000 人數
needpartK = needK/5
countlist = []
kp = 1 # 原本是 0.0001 不過這裡放大 10000 倍
low = 0
lowlist = []
largelist = []
coverageAll = []
lifenumlist = [] #all data life time
lifetime = {}
lifetimesum = needK*3/2
for num in range(int(lifetimesum)):  # lifetime 初始化  *3 放收集到資料的lifetime
    lifetime[num] = -1

coveragelist = []
coverage = 1
nownum = 0
lastcoverage = 1
for i in range(100) : #做100次
    count = 0
    partlist = []
    nextPlist = []
    plist = []

    if i != 0:
        Covcount = 0
        for i in coveragelist:
            Covcount = Covcount + i
        lastCovAve = Covcount/5
    coveragelist = []
    nowlifenumlist = []
    for ii in range(5) : #5個time slot
        NowIsEmpty = [] #紀錄 那些life以扣光 位置要填補
        lifenum = 0 #現有數量
        totalLife = 0
        if (ii != 0 and i == 0) or (i != 0): #第二輪開始資料衰減
            for num in range(int(lifetimesum)):
                if lifetime[num] == -1 or lifetime[num] == 0:
                    lifetime[num] = -1
                elif lifetime[num] > 0:
                    lifetime[num] = lifetime[num] - 1
                    totalLife = totalLife + lifetime[num]
                    lifenum = lifenum + 1

        for iii in range(n) : # n=1000 有幾個人
            if random.randint(1, 10000) <= p:
                count = count + 1
                for num in range(int(lifetimesum)):
                    if lifetime[num] == -1:
                        lifetime[num] = 5
                        break

        partlist.append(count)

        if i != 0 :
            coverage = lifenum/needK - (1 - totalLife/(5*needK))*(1/needK)  #(永遠0.01?)
            coveragelist.append(round(coverage, 4))
            coverageAll.append(round(coverage, 4))
        lifenumlist.append(lifenum)
        nowlifenumlist.append(lifenum)
        #校正P
        nextP = 0
        if count >= needpartK * (ii+1) and i != 0:
            nextP = (needK / count) * (1/ (5-ii) ) * (count - needpartK*(ii+1)*(1/coverage)*1.6) * -1 * kp
            # (1/ (5-ii) )
        elif count < needpartK * (ii+1) and i != 0:
            nextP = 12 * (needK / count) * (1 / (5-ii) ) * (needpartK*(ii+1)*(1/coverage)*1.6 - count) * kp
        elif count >= needpartK * (ii+1) :
            nextP = (needK / count) * (1/ (5-ii) ) * (count - needpartK*(ii+1)) * -1 * kp
        elif count < needpartK * (ii+1) :
            nextP = 12 * (needK / count) * (1 / (5-ii) ) * (needpartK*(ii+1) - count ) * kp


        #if i >= 1 and len(coverageAll) > 10:
            #if abs(coverageAll[len(coverageAll)-1] - coverageAll[len(coverageAll)-2]) < 0.06 and fu == 0:
                #needK = needK * (1/lastcoverage)
               # fu = 1
            #------------------------------------
                #if lifenum > needK:
                    #needK2 = needK * (1/lastcoverage)
                    #needpartK = needK2/5
                #elif lifenum <= needK:
                 #   needK2 = needK2 * lastcoverage
                  #  needpartK = needK2/5
                #fu = 1

        nextPlist.append(round(nextP/10000, 5))
        p = p + round(nextP, 0) #round 四捨五入
        plist.append(round(p/10000, 5))
        nowneed = needpartK * (ii+1) * (1/coverage)*1.6
        if i >= 1 and len(coverageAll) > 3:
            cov = abs(coverageAll[len(coverageAll)-1] - coverageAll[len(coverageAll)-2])
            print("nowneed:", nowneed, "count:", count, "?:", needpartK, cov)
        else:
            print("nowneed:", nowneed, "count:", count, "?:", needpartK)

    if count < needK :
        low = low + 1
        lowlist.append(needK - count)
    elif count >= needK :
        largelist.append(count - needK)


    print("partlist: ", partlist)
    print("nextPlist: ", nextPlist)
    print("plist", plist)
    #print("count", count)
    #print("lifenum:", lifenumlist)
    print("nowlifenum:", nowlifenumlist)
    print("coverage:", coveragelist)
    print("num:", nownum)
    nownum += 1
    lastcoverage = coverage
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

temp = 0
temp1 = 0
lowlist = []
lowlistMinus = []
biglist = []
biglistMinus = []
low98 = 0
low95 = 0
avoidcycle0 = 0
for i in lifenumlist :
    if avoidcycle0 <= 4:
        avoidcycle0 += 1
        continue
    if i < needK:
        temp = temp + i
        lowlist.append(i)
        if i < needK*0.98:
            low98 += 1
        if i < needK*0.95:
            low95 += 1
        lowlistMinus.append(needK-i)
    elif i >= needK:
        temp1 = temp1 + i
        biglist.append(i)
        biglistMinus.append(i-needK)

print("lowlist:", lowlist)
if len(lowlist) != 0:
    print("lowave:", temp/len(lowlist))
elif len(lowlist) == 0:
    print("lowave:", temp)
print("lownum", len(lowlist))
print("low than 98 >", low98)
print("low than 95 >", low95)
print("biglist:", biglist)
print("bigave:", temp1/len(biglist))
print("bignum", len(biglist))
print("coverage:", coverageAll)

a = plt.plot(np.arange(500), lifenumlist)
plt.show()

# next plan 看每個 cycle 最後的coverage 來調係數? yep
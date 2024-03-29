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


def newCoverageFC (lifenumlist, life):
    countnum = 0  # 處理計算方式
    TheLife2 = 0
    TheLife2Num = 0
    for num2 in range(int(lifetimesum)):
        if lifetime[num2] >= (timeslot+1):
            TheLife2 += OriginLifetime[num2]
            TheLife2Num += 1
            if TheLife2Num == originK:
                break

    for newi in range(LT + 1):
        if newi == 0:
            life = life
        elif newi >= (timeslot + 1):  # 6
            life = life - (timeslot * lifenumlist[newi])
            countnum = countnum + lifenumlist[newi]
        elif newi <= timeslot and newi != 0:  # 5
            life = life - (newi * lifenumlist[newi])
    print(lifenumlist)

    AllLife = 0
    for iiii in range(len(AllLifeList)):
        AllLife += AllLifeList[iiii]
    # coverage2 = countnum / originK - (1 - life / ((AllLife/len(AllLifeList)) * originK)) * (1 / originK)
    if TheLife2Num <= originK:
        TheLife2 += (AllLife/len(AllLifeList)) * (originK - TheLife2Num)

    coverage2 = countnum / originK - (1 - life / TheLife2) * (1 / originK)
    print("coutnum:", countnum)
    print("life:", life)
    print("TheLife2:", TheLife2)
    print("TheLife2Num:", TheLife2Num)
    print("coverage2 : ", coverage2)
    return coverage2


if __name__ == '__main__':
    LT = 40  # 最長 lifetime
    LTrange = 20
    timeslot = 5
    totalcycle = 100
    fu = 0
    # p = 1050
    needK = 200  # k=2000
    originK = needK
    # n = random.randint(150, 150)  # n=1000 人數
    user, area = rw.userinit(9000)
    n = area[5]
    p = poi.Pcal(needK, n)
    trueP = p
    needpartK = needK/timeslot
    countlist = []
    kp = 0.1  # 原本是 0.0001 不過這裡放大 10000 倍
    kpp = 1  # 衰退用
    low = 0
    lowlist = []
    largelist = []
    coverageAll = []
    coverageFirst = []
    lifenumlist = []  # all data life time
    snlist = []  # 看收集差的變化 (常態???)
    AllLifeList = []  # 算平均 life 用
    lifetime = {}
    OriginLifetime = {}
    lifetimesum = needK*3
    LTkeep = 1
    CollectDelay = 1
    lifenum = 0  # 現有數量
    totaln = 0
    needpartkrecord = []
    countrecord = []
    for num in range(int(lifetimesum)):  # lifetime 初始化  *3 放收集到資料的lifetime
        lifetime[num] = -1
        OriginLifetime[num] = -1
    coveragelist = []
    coverage = 1
    nownum = 0
    lastcoverage = 1
    nownum222 = -1
    for i in range(totalcycle):  # 做100次
        count = 0
        partlist = []
        nextPlist = []
        plist = []
        if i != 0:
            Covcount = 0
            for i in coveragelist:
                Covcount = Covcount + i
            lastCovAve = Covcount/timeslot
        coveragelist = []
        nowlifenumlist = []
        deltaP = 0
        lastcount = 0
        deltaPlist = []
        for ii in range(timeslot):  # 5個time slot
            nownum222 += 1
            print("現在:", nownum222)
            NowIsEmpty = []  # 紀錄 那些life以扣光 位置要填補
            lifenum = 0  # 現有數量
            totalLife = 0
            lifenum2 = []
            for LTnum in range(LT+1):
                lifenum2.append(0)
            if (ii != 0 and i == 0) or (i != 0):  # 第二輪開始資料衰減
                for num in range(int(lifetimesum)):
                    if lifetime[num] == -1 or lifetime[num] == 0:
                        lifetime[num] = -1
                        OriginLifetime[num] = -1
                    elif lifetime[num] > 0:
                        lifetime[num] = lifetime[num] - 1
                        totalLife = totalLife + lifetime[num]
                        lifenum = lifenum + 1
                        if ii == (timeslot - 1):   # 4
                            for num2 in range(LT):
                                if num2 == 0:
                                    continue
                                elif num2 == lifetime[num]:
                                    lifenum2[num2] += 1

            needpartkrecord.append(round(needpartK, 2))
            if i == 0:
                if ii == 0:
                    coverageFirst.append(round(0, 5))
                else:
                    TheLife = 0
                    TheLifeNum = 0
                    for num in range(int(lifetimesum)):
                        if lifetime[num] > 0:
                            TheLife += 1 - lifetime[num] / OriginLifetime[num]
                            TheLifeNum += 1
                            if TheLifeNum == lifenum:
                                break

                    AllLife = 0
                    for iiii in range(len(AllLifeList)):
                        AllLife += AllLifeList[iiii]

                    if TheLifeNum <= originK:
                        TheLife += 1 * (originK - TheLifeNum)

                    coverage = (lifenum+count) / originK - ((TheLife / originK) / originK) * (1 / originK)  # (永遠0.01?) nope
                    print("Thelife:", TheLife)
                    coverageFirst.append(round(coverage, 5))

            if i != 0:
                TheLife = 0
                TheLifeNum = 0
                for num in range(int(lifetimesum)):
                    if lifetime[num] > 0:
                        TheLife += 1 - lifetime[num]/OriginLifetime[num]
                        TheLifeNum += 1
                        if TheLifeNum == lifenum:
                            break

                AllLife = 0
                for iiii in range(len(AllLifeList)):
                    AllLife += AllLifeList[iiii]

                if TheLifeNum <= originK:
                    TheLife += 1 * (originK - TheLifeNum)

                coverage = (lifenum+count) / originK - ((TheLife / originK) / originK) * (1 / originK)  # (永遠0.01?) nope
                print("Thelife:", TheLife)
                coveragelist.append(round(coverage, 5))
                coverageAll.append(round(coverage, 5))

            for iii in range(n):  # n=1000 有幾個人
                if random.randint(1, 10000) <= p:
                    count = count + 1
                    lifenum2[LT] += 1
                    for num in range(int(lifetimesum)):
                        if lifetime[num] == -1:
                            randomLife = random.randint(LT-LTrange, LT)
                            lifetime[num] = randomLife
                            OriginLifetime[num] = randomLife
                            AllLifeList.append(randomLife)
                            break

            partlist.append(count)
            countrecord.append(round(count - lastcount, 2))
            lastcount = count
            lifenumlist.append(lifenum+count)
            nowlifenumlist.append(lifenum)
            # 校正P
            nextP = 0
            if count == 0:
                nextP = 0
            elif count != 0:
                if coverage == 0:
                    coverage = 1
                if count >= needpartK * (ii+1) and i != 0:
                    nextP = needpartK*(ii+1) - count
                    # (1/ (5-ii) )
                elif count < needpartK * (ii+1) and i != 0:
                    nextP = needpartK*(ii+1) - count

                elif count >= needpartK * (ii+1):
                    nextP = needpartK*(ii+1) - count

                elif count < needpartK * (ii+1):
                    nextP = needpartK*(ii+1) - count

            print("nextP:", nextP)
            nextPlist.append(round(nextP/10000, 5))
            deltaP2 = 0
            if ii == (timeslot - 1):
                Newcoverage = newCoverageFC(lifenum2, totalLife)
                if count >= 1:
                    deltaP2 = (1/coverage) * deltaP
                    snlist.append(needK - count)  # sn 插植成常態分佈
                    kpp = 1/CollectDelay
                    CollectDelay = 1
                else:
                    deltaP2 = deltaP2
                    kpp = 1
                    CollectDelay += 1

                # if Newcoverage <= 0:
                #     k1 = originK * (1 - Newcoverage) * 1.03 + int(deltaP2) * kp * kpp
                # elif Newcoverage >= 1:
                #     # k1 = needK * (1 / Newcoverage) * (1/coverage) + int(deltaP2)
                #     k1 = 0
                # elif 0 < Newcoverage < 1:
                #     # k1 = originK * (1 / Newcoverage) * (1/coverage) + int(deltaP2)
                #     k1 = originK * (1 - Newcoverage) * 1.03 + int(deltaP2) * kp * kpp
                k1 = originK - (lifenum + count)
                #k1 = originK * (1 - Newcoverage)
                print("k1", k1)
                if k1 < 0:
                    k1 = 0
                needK = k1
                needpartK = needK/timeslot
                user, area = rw.rw(user, area)
                n = area[5]
                totaln += n
                p = poi.Pcal(k1, n)  # round 四捨五入
                print("newcoverage:", Newcoverage)
                print("deltaP2:", deltaP2)
                print("deltaP3:", originK * (1 - Newcoverage))
                print("deltaP4:", int(deltaP2) * kp)
                print("p:", p)
            elif ii < (timeslot - 1):
                if count == 0 and ii == 0:
                    deltaP = deltaP
                else:
                    deltaP = deltaP + nextP
                deltaPlist.append(deltaP)

            plist.append(round(p/10000, 5))

        if (lifenum+count) < originK :
            low = low + 1
            lowlist.append(originK - (lifenum+count))
        elif (lifenum+count) >= originK :
            largelist.append(count - (lifenum+count))

        print("partlist: ",partlist)
        print("nextPlist: ", nextPlist)
        print("plist", plist)
        # print("count", count)
        # print("lifenum:", lifenumlist)
        print("nowlifenum:", nowlifenumlist)
        print("coverage:", coveragelist)
        print("num:", nownum)
        nownum += 1
        lastcoverage = coverage
        print("deltaP:", deltaPlist)
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
    big98 = 0
    big95 = 0
    avoidcycle0 = 0
    for i in lifenumlist :
        if avoidcycle0 <= 4:
            avoidcycle0 += 1
            continue
        if i < originK:
            temp = temp + i
            lowlist.append(i)
            if i < originK*0.98:
                low98 += 1
            if i < originK*0.95:
                low95 += 1
            lowlistMinus.append(originK-i)
        elif i >= originK:
            temp1 = temp1 + i
            biglist.append(i)
            if i > originK*1.02:
                big98 += 1
            if i > originK*1.05:
                big95 += 1
            biglistMinus.append(i-originK)

    print("lowlist:", lowlist)
    if len(lowlist) != 0:
        print("lowave:", temp/len(lowlist))
    elif len(lowlist) == 0:
        print("lowave:", temp)
    print("lownum", len(lowlist))
    print("low than 98 >", low98)
    print("low than 95 >", low95)
    print("biglist:", biglist)
    if len(biglist) != 0:
        print("bigave:", temp1/len(biglist))
    elif len(biglist) == 0:
        print("bigave:", temp1)
    print("bignum", len(biglist))
    print("big than 102 >", big98)
    print("big than 105 >", big95)
    print("coverage:", coverageAll)
    coverageCycle = []
    jk = 0
    clow = []
    cloww = []
    for j in coverageAll:
        jk += 1
        if jk == 5:
            jk = 0
            coverageCycle.append(j)
            if j < 1:
                clow.append(j)
                if j < ((originK*0.98)/originK):
                    cloww.append(j)
    print("clow:", clow)
    print("cloww:", cloww)
    AllLife = 0
    for iiii in range(len(AllLifeList)):
        AllLife += AllLifeList[iiii]
    print("aveLifetime:", AllLife/iiii, iiii)
    print("coverageFirst:", coverageFirst)
    print("AllCoverage:", coverageFirst + coverageAll)
    print("平均人數:", totaln/totalcycle)
    print("持有量:", lifenumlist)
    print("每次獲得", countrecord)
    print("timeslot 需求:", needpartkrecord)
    a = plt.plot(np.arange(timeslot * totalcycle), lifenumlist, linewidth=1)
    # plt.xaxis.set_major_locator(ticker.MultipleLocator(100))
    plt.xticks(fontsize=9)
    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(50))
    plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(25))
    plt.show()
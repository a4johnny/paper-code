import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.style as style
import math
import random
from IPython.core.display import HTML

p = 4000
needK = 2000 # k=2000
needpartK = 2000/5
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
    p = 4000
    for ii in range(5) : #5個time slot
        for iii in range(1000) : # n=1000 有幾個人
            if random.randint(1, 10000) <= p :
                count = count + 1
        partlist.append(count)
        #校正P
        nextP = 0
        if count >= needpartK * (ii+1) :
            nextP = (needK / count) * (1/ (5-ii) ) * (count - needpartK*(ii+1) ) * -1 * kp
            # (1/ (5-ii) )
        elif count < needpartK * (ii+1) :
            nextP = 12 * (needK / count) * (1 / (5-ii) ) * (needpartK*(ii+1) - count ) * kp
        nextPlist.append(round(nextP/10000, 5))
        p = p + round(nextP, 0) #round 四捨五入
        plist.append(round(p/10000, 5))
    if count < 2000 :
        low = low + 1
        lowlist.append(2000 - count)
    elif count >= 2000 :
        largelist.append(count - 2000)

    print(partlist)
    print(nextPlist)
    print(plist)
    print(count)
print(low)
print(lowlist)
print(largelist)

temp = 0
for i in lowlist :
    temp = temp + i
ave = temp/len(lowlist)
print(ave)

temp = 0
for i in largelist :
    temp = temp + i
ave = temp/len(largelist)
print(ave)

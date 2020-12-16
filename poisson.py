import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.style as style
import math
from IPython.core.display import HTML
#from scipy.stats import poisson

# %matplotlib inline
style.use('fivethirtyeight')
#plt.rcParams['figure.figsize']=(14,7)
#plt.figure(dpi=100)

#left == x #pmf
#plt.bar(x=np.arange(100), height=(stats.poisson.pmf(np.arange(100), mu=20)), width=0.75, alpha=0.75)
#需要量
k = 100
n = 50
t = 5
p = k/n

count = 0
pp = []
for i in range(100) :
    count = count + 0.01
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
    ko = math.sqrt(k)
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

a = plt.bar(np.arange(100), bb)
plt.show()
aa = plt.bar(np.arange(100), bb2)
plt.show()
print("thePP : ", thePP)

b = stats.poisson.pmf(k, mu)
#x = np.arange(stats.poisson.ppf(0.01, mu), stats.poisson.ppf(0.99, mu))
c = stats.poisson.pmf(np.arange(k), mu)
## np.arange(k) 照k大小
#plt.bar(np.arange(k), stats.poisson.pmf(np.arange(k), mu)) # X,Y data type 要一樣

#cdf
#累加 1 - 10
#d = stats.poisson.cdf(10, mu)
#plt.plot(np.arange(20), stats.poisson.cdf(np.arange(20), mu=2), color="#fc4f30")
#plt.plot(np.arange(k), stats.poisson.cdf(np.arange(k), mu), color="#fc4f30")

#legend 圖例
#plt.text(x=8, y=0.45, s="pmf(poisson)", alpha=0.75, weight="bold", color="#008fd5")
#plt.text(x=8.5, y=0.9, s="cdf", rotation=.75, weight="bold", color="#fc4f30")

plt.show()

#a = plt.show()
#print(a)
#--------------------------------------------------------------------------------------------
# plt.figure(dpi=100)
# # PDF λ=1
# plt.scatter(np.arange(20),stats.poisson.pmf(np.arange(20),mu=1),alpha=0.75,s=100)
# plt.plot(np.arange(20),stats.poisson.pmf(np.arange(20),mu=1),alpha=0.75)
#
# #PDF λ=5
# plt.scatter(np.arange(20),stats.poisson.pmf(np.arange(20),mu=5),alpha=0.75,s=100)
# plt.plot(np.arange(20),stats.poisson.pmf(np.arange(20),mu=5),alpha=0.75)
#
# #PDF λ=10
# plt.scatter(np.arange(20),stats.poisson.pmf(np.arange(20),mu=10),alpha=0.75,s=100)
# plt.plot(np.arange(20),stats.poisson.pmf(np.arange(20),mu=10),alpha=0.75)
#
# #LEGEND 圖例
# plt.text(x=3,y=0.1,s="$λ=1$",alpha=0.75,weight="bold",color="#008fd5")
# plt.text(x=8.25,y=0.075,s="$λ=5$",rotation=.75,weight="bold",color="#fc4f30")
# plt.text(x=14.5,y=0.06,s="$λ=10$",rotation=.75,weight="bold",color="#fc4f30")
#
# plt.show()
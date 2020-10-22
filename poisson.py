import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.style as style
from IPython.core.display import HTML
#from scipy.stats import poisson

# %matplotlib inline
style.use('fivethirtyeight')
#plt.rcParams['figure.figsize']=(14,7)
#plt.figure(dpi=100)

#left == x #pmf
#plt.bar(x=np.arange(100), height=(stats.poisson.pmf(np.arange(100), mu=20)), width=0.75, alpha=0.75)
k = 1
n = 10
t = 1
p = k/n
mu= n * p *t
b = stats.poisson.pmf(k, mu)
#x = np.arange(stats.poisson.ppf(0.01, mu), stats.poisson.ppf(0.99, mu))
c = stats.poisson.pmf(np.arange(k), mu)
k2 = k
plt.bar(np.arange(k2), stats.poisson.pmf(np.arange(k2), mu))

#cdf
#plt.plot(np.arange(20), stats.poisson.cdf(np.arange(20), mu=2), color="#fc4f30")
#plt.plot(np.arange(k), stats.poisson.cdf(np.arange(k), mu), color="#fc4f30")

#legend 圖例
#plt.text(x=8, y=0.45, s="pmf(poisson)", alpha=0.75, weight="bold", color="#008fd5")
#plt.text(x=8.5, y=0.9, s="cdf", rotation=.75, weight="bold", color="#fc4f30")

a = plt.show()
print(a)
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
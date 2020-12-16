import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.style as style
import math
import random
from IPython.core.display import HTML

lifetime = {}
total = random.randint(80,120)
totalnum = 0
zeronum = 0
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0

for i in range(total):
    ii = i + 1
    lifetime[str(ii)] = random.randint(0,5)
    totalnum = totalnum + lifetime[str(ii)]
    if lifetime[str(ii)] == 0:
        zeronum = zeronum + 1
    elif lifetime[str(ii)] == 1 :
        num1 = num1 + 1
    elif lifetime[str(ii)] == 2:
        num2 = num2 + 1
    elif lifetime[str(ii)] == 3:
        num3 = num3 + 1
    elif lifetime[str(ii)] == 4:
        num4 = num4 + 1
    elif lifetime[str(ii)] == 5:
        num5 = num5 + 1

coverage = (total - zeronum)/100 - (1 - totalnum/(5*100))*0.01

print('total:', total)
print(zeronum)
print('num1:', num1)
print('num2:', num2)
print('num3:', num3)
print('num4:', num4)
print('num5:', num5)
print('coverage:', coverage)

for i in range(total):
    dictnum = i + 1
    lifetime[str(dictnum)] = lifetime[str(dictnum)] - 1

print(lifetime)

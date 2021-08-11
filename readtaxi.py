import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.style as style
import math
import random
import datetime
from IPython.core.display import HTML
import mplfinance as mpf

num = 105
turedata = -1
turedatalist = []
people = 0

for ii in range(100000):
    time = 0
    try:
        a = open('./Taxi/Taxi_' + str(num), mode='r')
        num += 1
        # a = open('./Taxi/Taxi_105', mode='r')
    except IOError:
        num += 1
        continue

    print(num)
    turedata += 1
    if turedata > 6000:
        continue

    for i in a.readlines():
        if time < 500:
            i2 = i.split(",")
            if 121.43 <= float(i2[2]) <= 121.493 and 31.19 <= float(i2[3]) <= 31.247:
                if turedata is 0:
                    turedatalist.append(1)
                else:
                    turedatalist[time] += 1
            else:
                if turedata is 0:
                    turedatalist.append(0)
                else:
                    turedatalist[time] += 0
            time += 1
        else:
            break
    a.close()

avep = sum(turedatalist)/len(turedatalist)
print(turedata)
print(turedatalist)
print(avep, max(turedatalist), min(turedatalist))

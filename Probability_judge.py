import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.style as style
import math
import random
from IPython.core.display import HTML

countlist = []
for i in range(20) :
    count = 0
    partlist = []
    for ii in range(5) :
        for iii in range(1000) :
            if random.randint(1, 100) <= 40 :
                count = count + 1
        partlist.append(count)
    print(partlist)
    print(count)

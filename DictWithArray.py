import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.style as style
import math
import random
from IPython.core.display import HTML
import poisson_oneTOmany2 as poi
import seaborn as sn


if __name__ == '__main__':
    hashmap1 = {}
    LTrange = 10
    for i in range(LTrange):
        stri = str(i + 1)
        array1 = []
        if (i + 1) == 3:
            for ii in range(15):
                num = random.randint(1, 10)

        hashmap1[stri] = array1

    print(hashmap1)
    # array1 = hashmap1['3']
    print(hashmap1['3'][1])
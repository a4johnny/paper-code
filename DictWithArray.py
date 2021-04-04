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


def hashmap():
    hashmap1 = {}
    LTrange = 10
    for i in range(LTrange):
        stri = str(i + 1)
        array1 = []
        if (i + 1) == 3:  # 到 dict = 3 的時候
            for ii in range(20):  # 20個數用2分插入
                num = random.randint(1, 30)
                j = 0  # 頭
                k = len(array1)-1  # 尾
                truek = k
                if k == -1:
                    array1.append(num)
                elif k == 0:
                    if num >= array1[k]:
                        array1.append(num)
                    else:
                        array1.insert(0, num)
                elif k != 0:
                    todo = 0
                    if array1[k] <= num:
                        array1.append(num)
                        todo = 1
                    while todo == 0:
                        lenk = int((k+j)/2)
                        if num == array1[lenk]:
                            array1.insert(lenk, num)
                            break
                        elif array1[lenk] < num:
                            if (lenk+1) > truek:
                                array1.append(num)
                            elif num <= array1[lenk + 1]:
                                array1.insert(lenk+1, num)
                                break
                            elif num > array1[lenk + 1]:
                                j = lenk
                        elif array1[lenk] > num:
                            if (lenk-1) < 0:
                                array1.insert(lenk, num)
                                break
                            elif num >= array1[lenk - 1]:
                                array1.insert(lenk, num)
                                break
                            elif num < array1[lenk - 1]:
                                k = lenk
        hashmap1[stri] = array1
    hashmap1['2'] = hashmap1['3']
    print(hashmap1)
    # array1 = hashmap1['3']
    print(hashmap1['3'][9])


if __name__ == '__main__':
    hashmap()
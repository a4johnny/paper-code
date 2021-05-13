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


def hashmapsort():
    hashmap1 = {}
    for i in range(LT-LTrange, LT+1, 1):  # 不包含最後的數字
        stri = str(i)
        array1 = []
        if i == LT-LTrange+6:  # 到 dict = 3 的時候
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
    hashmap1['25'] = hashmap1['26']
    print(hashmap1)
    # array1 = hashmap1['3']
    print(hashmap1['25'][9])
    return hashmap1


def hashmapdecay(hp):
    # global LT
    # LT = 20
    # print(LT, LTrange)
    for i in hp:
        i = []
        print(i)


if __name__ == '__main__':
    LT = 30
    LTrange = 10
    hp1 = hashmapsort()
    hashmapdecay(hp1)
    print(LT)
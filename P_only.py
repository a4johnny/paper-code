import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.style as style
import math
from IPython.core.display import HTML


def Pcal (delp, trueN):
    style.use('fivethirtyeight')
    k = int(delp)
    print("pppk", k)
    n = trueN

    if delp < 0:
        thePP = 0
    else:
        thePP = (k/5)/trueN
    print('TAAAAA:', k, trueN)

    print("thePP : ", thePP)
    return int(thePP*10000)

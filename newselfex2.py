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

dddd = []
b = 1364774700
b = datetime.datetime.fromtimestamp(b)
print(type(b))
dddd.append(b)
dddd.append(b)

dd = {'Open': [10,5], 'High': [10,5], 'Low': [0,1], 'Close': [0,1]}

a = pd.DataFrame(dd, index=[dddd])


mpf.plot(a)

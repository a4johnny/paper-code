import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
import matplotlib as mpl
from collections import Counter
import seaborn as sns; sns.set()
import pymc3

formula = columns[-1] + '~' + ('+'.join([col for col in columns[:-1]]))

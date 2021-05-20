import numpy as np

x = np.array([[11, 21, 41], [71, 1, 12], [33, 2, 13]])
z = np.diff(x, axis=-1)

print(z)
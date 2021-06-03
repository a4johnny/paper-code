import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.style as style
import math
import random
from IPython.core.display import HTML

# a -> pid (blue0
# b -> poisson (orange)
# c -> coverage (green)
a9000l = [131, 123, 151, 124, 116]
a9000l98 = [35, 25, 51, 24, 26]
a9000ln = [492.19, 492.82, 491.54, 493.08, 492.89]
a9000b = [364, 372, 344, 371, 379]
a9000b98 = [177, 169, 164, 157, 163]
a9000bn = [511.34, 511.02, 511.34, 510.61, 510.65]

b9000l = [432, 429, 441, 412, 422]
b9000l98 = [417, 421, 414, 404, 408]
b9000ln = [397.65, 395.19, 399.27, 394.98, 398.45]
b9000b = [63, 66, 54, 83, 73]
b9000b98 = [56, 46, 46, 55, 65]
b9000bn = [531.30, 530.63, 532.53, 527.21, 537.27]

c9000l = [285, 278, 252, 278, 265]
c9000l98 = [114, 111, 71, 121, 92]
c9000ln = [490.01, 489.93, 492.23, 498.69, 490.45]
c9000b = [210, 217, 243, 217, 230]
c9000b98 = [53, 49, 75, 60, 67]
c9000bn = [507.64, 509.09, 507.86, 507.76, 507.51]

a900l = [181, 171, 170, 161, 168]
a900l98 = [124, 102, 119, 113, 99]
a900ln = [47.54, 47.68, 47.30, 47.49, 47.72]
a900b = [314, 324, 325, 334, 327]
a900b98 = [195, 204, 184, 202, 203]
a900bn = [53.02, 52.69, 52.41, 52.65, 52.71]

b900l = [445, 444, 420, 424, 440]
b900l98 = [436, 435, 408, 410, 433]
b900ln = [39.45, 39.13, 38.87, 39.65, 38.92]
b900b = [50, 51, 75, 71, 55]
b900b98 = [37, 39, 56, 51, 43]
b900bn = [55.14, 55.49, 55.81, 57.15, 54.36]

c900l = [279, 282, 254, 264, 314]
c900l98 = [200, 230, 183, 226, 256]
c900ln = [47.16, 46.84, 51.42, 46.32, 46.21]
c900b = [216, 213, 241, 231, 181]
c900b98 = [107, 110, 87, 148, 82]
c900bn = [52.04, 52.07, 51.42, 52.69, 52.60]

a90l = [186, 179, 160, 202, 198]
a90l98 = [186, 179, 160, 202, 198]
a90ln = [3.58, 3.52, 3.57, 3.78, 3.60]
a90b = [309, 316, 335, 293, 297]
a90b98 = [175, 238, 190, 170, 197]
a90bn = [6.09, 6.19, 6.18, 6.03, 6.19]

b90l = [324, 392, 382, 410, 343]
b90l98 = [324, 392, 382, 410, 343]
b90ln = [2.60, 2.76, 2.88, 2.97, 2.75]
b90b = [171, 103, 113, 85, 152]
b90b98 = [78, 51, 27, 38, 124]
b90bn = [5.94, 6.41, 5.56, 5.70, 6.77]

c90l = [310, 275, 281, 308, 267]
c90l98 = [310, 275, 281, 308, 267]
c90ln = [3.31, 3.21, 3.46, 3.45, 3.24]
c90b = [185, 220, 214, 187, 228]
c90b98 = [102, 128, 84, 138, 140]
c90bn = [5.65, 5.89, 5.54, 6.21, 6.06]

a9000lave = [492.19, 492.82, 491.54, 493.08, 492.89]
a9000bave = [511.34, 511.02, 511.34, 510.61, 510.65]
b9000lave = [397.65, 395.19, 399.27, 394.98, 398.45]
b9000bave = [531.30, 530.63, 532.53, 527.21, 537.27]
c9000lave = [490.01, 489.93, 492.23, 489.69, 490.45]
c9000bave = [507.64, 509.09, 507.86, 507.76, 507.51]

a900lave = [47.54, 47.68, 47.30, 47.49, 47.72]
a900bave = [53.02, 52.69, 52.41, 52.65, 52.71]
b900lave = [39.45, 39.13, 38.87, 39.65, 38.92]
b900bave = [55.14, 55.49, 55.81, 57.15, 54.36]
c900lave = [47.16, 46.84, 46.91, 46.32, 46.21]
c900bave = [52.04, 52.07, 51.42, 52.69, 52.60]

a90lave = [3.58, 3.52, 3.57, 3.78, 3.60]
a90bave = [6.09, 6.19, 6.18, 6.03, 6.19]
b90lave = [2.60, 2.76, 2.88, 2.97, 2.75]
b90bave = [5.94, 6.41, 5.56, 5.70, 6.77]
c90lave = [3.31, 3.21, 3.46, 3.45, 3.24]
c90bave = [5.65, 5.89, 5.54, 6.21, 6.06]

getlt7 = [7.484115778326862, 7.484115778326862, 7.509608582881396, 7.514870881567231, 7.5203931493143426]
dblt7 = [3.407692307692308, 3.6755102040816327, 3.707692307692308, 3.6533333333333333, 3.3755102040816327]
getlt20 = [20.044568245125348, 20.083694978301303, 20.03818209924254, 19.952616909259834, 19.92716049382716]
dblt20 = [9.715953307392995, 10.67953667953668, 11.258823529411766, 9.841269841269842, 10.404494382022472]
getlt60 = [60.07193923145666, 59.981548154815485, 59.681697612732094, 60.01610738255034, 59.95058400718778]
dblt60 = [33.12301587301587, 32.242063492063494, 35.6, 34.38461538461539, 32.61960784313725]
getlt120 = [120.26344936708861, 120.2260659694288, 119.99518845228549, 120.42372881355932, 120.10952380952381]
dblt120 = [90.55094339622642, 90.96370967741936, 87.9563492063492, 88.66269841269842, 92.78571428571429]


xsign = ['9000', '900', '90']
xsign2 = ['500', '50']
x1 = [np.mean(a9000l), np.mean(a900l), np.mean(a90l)]
x2 = [np.mean(b9000l), np.mean(b900l), np.mean(b90l)]
x3 = [np.mean(c9000l), np.mean(c900l), np.mean(c90l)]
width = 0.2
xxx = np.arange(len(xsign))

# y1 = 平均得到 lt, y2 = db 平均 lt
y1 = [np.mean(getlt7), np.mean(getlt20), np.mean(getlt60), np.mean(getlt120)]
y2 = [np.mean(dblt7), np.mean(dblt20), np.mean(dblt60), np.mean(dblt120)]
yy1 = [round(a/b, 2) for a, b in zip(y2, y1)]

# low timeslot 2%外數量
xx1 = [np.mean(a9000l98), np.mean(a900l98), np.mean(a90l98)]
xx2 = [np.mean(b9000l98), np.mean(b900l98), np.mean(b90l98)]
xx3 = [np.mean(c9000l98), np.mean(c900l98), np.mean(c90l98)]

# 平均缺少筆數百分比
xxx1 = [(500 - np.mean(a9000ln))/500, (50 - np.mean(a900ln))/50, (5 - np.mean(a90ln))/5]
xxx2 = [(500 - np.mean(b9000ln))/500, (50 - np.mean(b900ln))/50, (5 - np.mean(b90ln))/5]
xxx3 = [(500 - np.mean(c9000ln))/500, (50 - np.mean(c900ln))/50, (5 - np.mean(c90ln))/5]

# 平均多餘
xxxx1 = [round(np.mean(a9000bn)-500, 1), round(np.mean(a900bn)-50, 1), round(np.mean(a90bn)-5, 1)]
xxxx2 = [round(np.mean(b9000bn)-500, 1), round(np.mean(b900bn)-50, 1), round(np.mean(b90bn)-5, 1)]
xxxx3 = [round(np.mean(c9000bn)-500, 1), round(np.mean(c900bn)-50, 1), round(np.mean(c90bn)-5, 1)]

# big timeslot 2%外數量
# xxxx1 = [np.mean(a9000b98), np.mean(a900b98), np.mean(a90b98)]
# xxxx2 = [np.mean(b9000b98), np.mean(b900b98), np.mean(b90b98)]
# xxxx3 = [np.mean(c9000b98), np.mean(c900b98), np.mean(c90b98)]

# 平均多餘筆數 百分比
xxxxx1 = [(np.mean(a9000bn)-500)/500, (np.mean(a900bn)-50)/50, (np.mean(a90bn)-5)/5]
xxxxx2 = [(np.mean(b9000bn)-500)/500, (np.mean(b900bn)-50)/50, (np.mean(b90bn)-5)/5]
xxxxx3 = [(np.mean(c9000bn)-500)/500, (np.mean(c900bn)-50)/50, (np.mean(c90bn)-5)/5]

h500 = [5, 6, 7, 5, 9]
h50 = [16, 5, 5, 5, 5]
l500 = [25, 26, 52, 36, 30]
l50 = [53, 67, 30, 39, 30]
p500 = [126, 44, 44]
p50 = [47, 125, 112]

h = [np.mean(h500), np.mean(h50)]
l = [np.mean(l500), np.mean(l50)]
p = [round(np.mean(p500), 1), round(np.mean(p50), 1)]

# 雙子圖
fig, ax1 = plt.subplots()
# ax2 = ax1.twinx()

# 長條圖數值
for x, y in enumerate(h):
    ax1.text(x, y+2, '%s'%y, ha='center')
for x, y in enumerate(l):
    ax1.text(x+width, y+2, '%s'%y, ha='center')
for x, y in enumerate(p):
    ax1.text(x+width*2, y+2, '%s'%y, ha='center')

# 長條圖
ax1.bar(np.arange(len(xsign2)), h, width, label='high', hatch='o', color='white', edgecolor='black')
ax1.bar(np.arange(len(xsign2)) + width, l, width, label='low', hatch='*', color='white', edgecolor='red')
ax1.bar(np.arange(len(xsign2)) + width*2, p, width, label='poisson', hatch='x', color='white', edgecolor='blue')

# 折線圖
# ax2.plot(xxx + width, xxxxx1, 'o--', label='PID')
# ax2.plot(xxx + width, xxxxx2, '*--', label='Poisson')
# ax2.plot(xxx + width, xxxxx3, 'x--', label='Coverage')

# x軸間隔 和 x 軸數字
plt.xticks(np.arange(len(xsign2)) + width, xsign2)

# 右上圖標
ax1.legend(bbox_to_anchor=(1, 1), loc='best', borderaxespad=1.5, handlelength=3, fontsize=15)
# ax2.legend(bbox_to_anchor=(0.5, 1), loc='best')

ax1.yaxis.set_major_locator(ticker.MultipleLocator(10))
ax1.set_ylim([0, 100])

# ax2.yaxis.set_major_locator(ticker.MultipleLocator(0.05))
# ax2.set_ylim([-0.5, 0.5])

ax1.grid()
# ax2.grid()
plt.show()

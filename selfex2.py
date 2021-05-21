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

xsign = ['9000', '900', '90']
x1 = [np.mean(a9000l), np.mean(a900l), np.mean(a90l)]
x2 = [np.mean(b9000l), np.mean(b900l), np.mean(b90l)]
x3 = [np.mean(c9000l), np.mean(c900l), np.mean(c90l)]
width = 0.2
xxx = np.arange(len(xsign))

# low timeslot 數量
# plt.bar(np.arange(len(xsign)), x1, width)
# plt.bar(np.arange(len(xsign)) + width, x2, width)
# plt.bar(np.arange(len(xsign)) + width*2, x3, width)
#
# plt.xticks(np.arange(len(xsign)) + width, xsign)
# plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(25))
# plt.show()

# -------------------------------------------------------------------------
# low timeslot 2%外數量
# xx1 = [np.mean(a9000l98), np.mean(a900l98), np.mean(a90l98)]
# xx2 = [np.mean(b9000l98), np.mean(b900l98), np.mean(b90l98)]
# xx3 = [np.mean(c9000l98), np.mean(c900l98), np.mean(c90l98)]
# 平均缺少筆數百分比
# xx1 = [(500 - np.mean(a9000ln))/500, (50 - np.mean(a900ln))/50, (5 - np.mean(a90ln))/5]
# xx2 = [(500 - np.mean(b9000ln))/500, (50 - np.mean(b900ln))/50, (5 - np.mean(b90ln))/5]
# xx3 = [(500 - np.mean(c9000ln))/500, (50 - np.mean(c900ln))/50, (5 - np.mean(c90ln))/5]
# 平均多餘筆數
# xx1 = [(np.mean(a9000bn)-500), (np.mean(a900bn)-50), (np.mean(a90bn)-5)]
# xx2 = [(np.mean(b9000bn)-500), (np.mean(b900bn)-50), (np.mean(b90bn)-5)]
# xx3 = [(np.mean(c9000bn)-500), (np.mean(c900bn)-50), (np.mean(c90bn)-5)]
# 平均獲得量
# xx1 = [500 + ((np.mean(a9000bave)-500) * np.mean(a9000b) - (500-np.mean(a9000lave)) * np.mean(a9000l))/500, 50 + ((np.mean(a900bave)-50) * np.mean(a900b) - (50-np.mean(a900lave)) * np.mean(a900l))/500, 5 + ((np.mean(a90bave)-5) * np.mean(a90b) - (5-np.mean(a90lave)) * np.mean(a90l))/500]
# xx2 = [500 + ((np.mean(b9000bave)-500) * np.mean(b9000b) - (500-np.mean(b9000lave)) * np.mean(b9000l))/500, 50 + ((np.mean(b900bave)-50) * np.mean(b900b) - (50-np.mean(b900lave)) * np.mean(b900l))/500, 5 + ((np.mean(b90bave)-5) * np.mean(b90b) - (5-np.mean(b90lave)) * np.mean(b90l))/500]
# xx3 = [500 + ((np.mean(c9000bave)-500) * np.mean(c9000b) - (500-np.mean(c9000lave)) * np.mean(c9000l))/500, 50 + ((np.mean(c900bave)-50) * np.mean(c900b) - (50-np.mean(c900lave)) * np.mean(c900l))/500, 5 + ((np.mean(c90bave)-5) * np.mean(c90b) - (5-np.mean(c90lave)) * np.mean(c90l))/500]
#
# for ii in xx1:
#     pos = xx1.index(ii)
#     print(pos)
#     ii = round(ii, 1)
#     xx1[pos] = ii
#
# for ii in xx2:
#     pos = xx2.index(ii)
#     print(pos)
#     ii = round(ii, 1)
#     xx2[pos] = ii
#
# for ii in xx3:
#     pos = xx3.index(ii)
#     print(pos)
#     ii = round(ii, 1)
#     xx3[pos] = ii

# 長條圖數值
# for x, y in enumerate(xx1):
#     plt.text(x, y+5, '%s'%y, ha='center')
# for x, y in enumerate(xx2):
#     plt.text(x+width, y+5, '%s'%y, ha='center')
# for x, y in enumerate(xx3):
#     plt.text(x+width*2, y+5, '%s'%y, ha='center')

# 長條圖
# plt.bar(np.arange(len(xsign)), xx1, width, label='PID', hatch='x')
# plt.bar(np.arange(len(xsign)) + width, xx2, width, label='Poisson', hatch='///')
# plt.bar(np.arange(len(xsign)) + width*2, xx3, width, label='Coverage', hatch='-')
# plt.xticks(np.arange(len(xsign)) + width, xsign)
# plt.xlabel("people")
# # plt.ylabel("num", rotation=0, loc='left')
# plt.ylabel("error")
# # plt.annotate("12333333333333333", (0, 0))

# # 折線圖 (雙子圖)
# x = np.arange(50)
# timeslotrecord = [50.0, 50.0, 50.0, 50.0, 50.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 11.49, 11.49, 11.49, 11.49, 11.49, 14.86, 14.86, 14.86, 14.86, 14.86, 17.16, 17.16, 17.16, 17.16, 17.16, 12.21, 12.21, 12.21, 12.21, 12.21, 4.82, 4.82, 4.82, 4.82, 4.82, 10.24, 10.24, 10.24, 10.24, 10.24, 16.08, 16.08, 16.08, 16.08, 16.08]
# countrecord = [65, 66, 79, 50, 48, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 12, 9, 10, 10, 17, 16, 18, 13, 16, 24, 18, 16, 15, 22, 11, 11, 21, 17, 18, 5, 3, 6, 7, 7, 10, 8, 11, 13, 8, 14, 17, 14, 10, 16]
# dif = np.array([timeslotrecord, countrecord])
# diff = np.diff(dif, axis=0)
# diff2 = diff.tolist()
#
# fig, ax1 = plt.subplots()
# ax2 = ax1.twinx()
#
# y1 = timeslotrecord
# ax2.plot(x, y1, label='timeslotrecord')
#
# y2 = countrecord
# ax2.plot(x, y2, '--', label='countrecord')
# # s>只有方塊 s->方塊+線 ^三角形
#
# y3 = diff2[0]
# minusy3 = []
# for i in range(len(y3)):
#     if y3[i] < 0:
#         y3[i] *= -1
#         minusy3.append(i)
#
# bars = ax1.bar(x, y3, label='diff', color='white', edgecolor='red', hatch='//')
# for i in range(len(y3)):
#     if (i in minusy3) is True:
#         bars[i].set_edgecolor('green')
#         bars[i].set_hatch('-')
#
# ax1.legend(bbox_to_anchor=(1, 0.95), loc='best')
# ax2.legend(bbox_to_anchor=(1, 0.85), loc='best')



# 右上圖例
# plt.legend(bbox_to_anchor=(0.9, 1), loc='upper left')
plt.legend(bbox_to_anchor=(0.9, 1), loc='best')
plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(10))
plt.show()
# ----------------------------------------------------------------------------



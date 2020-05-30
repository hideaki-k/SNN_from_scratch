# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

tc_m = 1e-2 # 膜時定数
R = 1 # 膜抵抗
tref = 5e-3 # 不応期
vthr = 1 # 閾値電圧
I_max = 3 # 最大電流
I = np.arange(0, I_max, 0.01) # 入力電流

fig = plt.figure(figsize = (4, 3))
ax = fig.add_subplot(111)

rate = 1 / (tref + tc_m * np.log(R*I/(R*I - vthr)))
rate[np.isnan(rate)] = 0 
ax.grid(which = "major", axis = "x", color = "blue", alpha = 0.8,
        linestyle = "--", linewidth = 0.5)

# y軸に目盛線を設定
ax.grid(which = "major", axis = "y", color = "green", alpha = 0.8,
        linestyle = "--", linewidth = 0.5)
# 描画

plt.plot(I, rate, color="r")
plt.xlabel('Input current(nA)')
plt.ylabel('Firing rate(Hz)')
plt.xlim(0, I_max)
plt.show()
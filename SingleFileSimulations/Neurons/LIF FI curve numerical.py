# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

dt = 5e-5; T = 1; nt = round(T/dt)
tref = 5e-3; tc_m = 1e-2; vrest = 0; vreset = 0; vthr = 1

I_max = 3 # (nA)
N = 100 # N 種類の入力電流
I = np.linspace(0, I_max, N) # 入力電流(pA)
spikes = np.zeros((N, nt)) # スパイクの記録変数

for i in tqdm(range(N)):
    v = vreset;tlast = 0 #初期化
    for t in range(nt):
        dv = (vrest - v + I[i]) / tc_m #膜電位の変化量
        update = 1 if((dt*t) > (tref+tlast)) else 0 #不応期でないかの確認
        v = v + update*dv*dt#膜電位の更新
        s = 1*(v>=vthr)     #発火の確認
        tlast = tlast*(1-s) + dt*t*s #スパイク時刻更新
        spikes[i, t] = s #保存
        v = v*(1-s) + vreset*s #発火している場合に膜電位をリセット

rate = np.sum(spikes, axis=1) / T # 発火率
plt.figure(figsize=(4, 3))
plt.plot(I, rate)
plt.xlabel("Input current(nA)")
plt.ylabel("Firing rate(Hz)")
plt.show()



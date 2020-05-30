  # -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

from Models.Neurons import CurrentBasedLIF
from Models.Synapses import DoubleExponentialSynapse

dt = 1e-4; T = 1; nt = round(T/dt) # シミュレーション時間
num_in = 10; num_out = 1 # 入力/出力のニューロンの数

#print(np.random.rand(nt, num_in).shape)
# 入力のポアソンスパイク
fr_in = 30 # 入力のポアソンスパイクの発火率(Hz)
x = np.where(np.random.rand(nt, num_in) < fr_in*dt, 1, 0)
W = 0.2*np.random.randn(num_out, num_in) # ランダムな結合重み
print("w",W.shape)
print("x",x.shape)
neurons = CurrentBasedLIF(N=num_out, dt=dt, tref=5e-3, tc_m=1e-2, vrest=-65, vreset=-60, vthr=-40, vpeak=30)

synapses = DoubleExponentialSynapse(N=num_out, dt=dt, td=1e-2, tr=1e-2)

#記録用配列
current = np.zeros((num_out, nt))
voltage = np.zeros((num_out, nt))

# シミュレーション
neurons.initialize_states() # 状態の初期化
for t in tqdm(range(nt)):  # ポアソンスパイク10000回に対して
    # 更新
    #print(np.dot(W, x[t]))
    I = synapses(np.dot(W, x[t]))
    s = neurons(I)

    # 記録
    current[: ,t] = I
    voltage[:, t] = neurons.v_
# 結果表示
t = np.arange(nt)*dt
plt.figure(figsize=(7, 6))
plt.subplot(3,1,1)
plt.plot(t, voltage[0], color="k")
plt.xlim(0, T)
plt.ylabel('Membrane potential (mV)')
plt.subplot(3,1,2)
plt.plot(t, current[0], color="k")
plt.xlim(0, T)
plt.ylabel('Synaptic current (pA)')
plt.subplot(3,1,3)
for i in range(num_in):
    plt.plot(t, x[:, i]*(i+1), 'ko', markersize=2)
plt.xlabel('Time (s)')
plt.ylabel('Neuron index')
plt.xlim(0, T)
plt.ylim(0.5, num_in+0.5)
plt.show()

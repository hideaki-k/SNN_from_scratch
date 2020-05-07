# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

dt = 1e-3; T = 1; nt = round(T/dt) # シミュレーション時間
n_neurons = 2 # ニューロンの数
fr = 30 # ポアソンスパイクの発火率(Hz)
isi = np.random.exponential(1/(fr*dt),size=(round(nt*1.5/fr),n_neurons))
spike_time = np.cumsum(isi, axis = 0) # isiを蓄積

spike_time[spike_time > nt -1] = 0 # nt を超える場合をゼロに
print(spike_time)
spike_time = spike_time.astype(np.int32) #float to int
spikes = np.zeros((nt,n_neurons)) # スパイク記録タプル1000*neuron数
print("spike_tume[1,1]",spike_time[:,1])
print(spike_time[:,0].shape)
for i in range(n_neurons):
    print(spike_time[:,i])
    spikes[spike_time[:,i], i] =1
#print(spikes) 
spikes[0] = 0 # (spike_time=0 の発火を除外)
print("Num. of spikes:",np.sum(spikes))
print("Firing rate:",np.sum(spikes)/(n_neurons*T))
#描画
t = np.arange(nt)*dt

plt.figure(figsize=(5, 4))
for i in range(n_neurons):
    plt.plot(t, spikes[:, i]*(i+1),"ko",markersize=2)
plt.xlabel("Time (s)");plt.ylabel("Neuron index")
plt.xlim(0, T);plt.ylim(0.5,n_neurons+0.5)
plt.show()



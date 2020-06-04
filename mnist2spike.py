# coding: utf-8
import sys, os
sys.path.append(r"C:\Users\hp731\Documents\GitHub\deep-learning-from-zero\deep-learning-from-scratch\dataset")
import numpy as np
import matplotlib.pyplot as plt
from mnist import load_mnist
import chainer
# データの読み込み
train, _ = chainer.datasets.get_mnist() # Chainer による MNIST データの読み込み

print(train[0][0].shape)
def online_load_and_encoding_dataset(dataset, i, dt, n_time, max_fr=32,norm=140):
    fr_tmp = max_fr*norm/np.sum(dataset[i][0])
    #print("fr_tmp",fr_tmp)
    fr = fr_tmp*np.repeat(np.expand_dims(dataset[i][0],
    axis=0), n_time, axis=0)
    #print(fr)
    input_spikes = np.where(np.random.rand(n_time, 784) < fr*dt, 1, 0)
    input_spikes = input_spikes.astype(np.uint8)
    return input_spikes

dt = 1e-3; t_inj = 0.350; nt_inj = round(t_inj/dt)

input_spikes = online_load_and_encoding_dataset(dataset=train, i=0,
dt=dt, n_time=nt_inj)
# 描画
plt.imshow(np.reshape(np.sum(input_spikes, axis=0), (28, 28)), cmap="gray")
plt.show()
  
# -*- coding: utf-8 -*-

import numpy as np

class fullConnection:
    def __init__(self, N_in, N_out, initW=None):
        if initW is not None:
            self.W = initW
        else:
            self.W = 0.1*np.random.rand(N_out, N_in)

    def backward(self, x):
        return np.dot(self.W.T, x)

    def __call__(self, x):
        return np.dot(self.W, x)

class DelayConnection:
    def __init__(self, N, delay, dt=1e-4):
        nt_delay = round(delay/dt) # 遅延のステップ幅
        self.state = np.zeros((N, nt_delay))

    def __call__(self, x):
        out = self.state[:, -1] # 出力
        self.state[:, 1:] = self.state[:, :-1] # 配列をずらす
        self.state[:, 0] = x # 入力
        return out
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

class CurrentBasedLIF:
    def __init__(self, N, dt=1e-4, tref=5e-3, tc_m=1e-2,
        vrest=-60, vreset=-60, vthr=-50, vpeak=20):
        self.N = N
        self.dt = dt
        self.tref = tref
        self.tc_m = tc_m
        self.vrest = vrest
        self.vreset = vreset
        self.vthr = vthr
        self.vpeak = vpeak

        self.v = self.vreset*np.ones(N)
        self.v = None
        self.tlast = 0
        self.tcount = 0


    def initialize_state(self, random_state = False):
        if random_state:
            self.v = self.vreset + np.random.rand(self.N)(self.vthr - self.vreset)

        else:
            self.v = self.vreset*np.ones(self.N)
        self.tlast = 0
        self.tcount = 0

    def __call_(self, I):
        dv = (self.vrest - self.v + I)/self.tc_m
        v = self.v + ((self.dt*self.tcount) > (self.tlast + self.tref))*dv*self.dt
        s = 1*(v>=self.vthr)
        self.tlast = self.tlast*(1-s) + self.dt*self.tcount*s # 発火時刻の更新

        v = v*(1-s) + self.vpeak*s       #発火している場合ピーク電位に更新
        self.v_ = v                      #発火時の電位も記録するための変数
        self.v = v*(1-s) + self.vreset*s #発火時に膜電位をリセット
        self.tcount += 1

        return s


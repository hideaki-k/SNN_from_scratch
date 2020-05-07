# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
spikes = np.zeros((10,10))
for i in range(10):
    for j in range(10):
        spikes[i,j] = i*j
print(spikes)
print(spikes[[3,4,5],2])
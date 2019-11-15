# -*- coding: utf-8 -*-
# @Author: abbenteprizer
# @Date:   2019-11-15 13:56:58
# @Last Modified by:   abbenteprizer
# @Last Modified time: 2019-11-15 14:38:33
'''
Humane schedules tasks following a distribution that mimics 
internet traffic. 

Example use:

sched(function, "dist", freq)

'''
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

### ###
# def distribution()
N = 100
np.random.seed(1)
dist = np.concatenate((np.random.normal(9, 3, int(0.3 * N)),
						np.random.normal(18, 2, int(0.3 * N))))[:, np.newaxis]

dist_plot = np.linspace(0, 24, 1000)[:, np.newaxis]

true_density = (0.3 * norm(9, 3).pdf(dist_plot[:, 0])
			  + 0.3 * norm(18,2).pdf(dist_plot[:, 0]))



fix, ax = plt.subplots()
ax.fill(dist_plot[:, 0], true_density, fc='black', alpha=0.2,
	label='input distribution')


ax.legend(loc='upper left')

plt.show()
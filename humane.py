# -*- coding: utf-8 -*-
# @Author: abbenteprizer
# @Date:   2019-11-15 13:56:58
# @Last Modified by:   abbenteprizer
# @Last Modified time: 2019-11-16 15:40:25
'''
Humane schedules tasks following a distribution that mimics 
internet traffic. 

Example use:

sched(function, "dist", freq)

'''
import numpy as np
from scipy.stats import norm
from scipy import stats
import matplotlib.pyplot as plt

### ###
### Printout of samples generated from the distributions ###
def print_samples_graph():
	np.random.seed()
	distributions = [
	    {"type": np.random.normal, "kwargs": {"loc": 10, "scale": 2}},
	    {"type": np.random.normal, "kwargs": {"loc": 18, "scale": 2}}
	]
	coefficients = np.array([0.4, 0.6])
	sample_size = 1000

	num_distr = len(distributions)
	data = np.zeros((sample_size, num_distr))
	for idx, distr in enumerate(distributions):
	    data[:, idx] = distr["type"](size=(sample_size,), **distr["kwargs"])
	random_idx = np.random.choice(np.arange(num_distr), size=(sample_size,), p=coefficients)
	sample = data[np.arange(sample_size), random_idx]
	print(sample)
	plt.hist(sample, bins=100, density=True)
	plt.show()


def generate_sample(num_samples):
	np.random.seed()
	distributions = [
	    {"type": np.random.normal, "kwargs": {"loc": 10, "scale": 2}},
	    {"type": np.random.normal, "kwargs": {"loc": 18, "scale": 2}}
	]
	coefficients = np.array([0.4, 0.6])

	num_distr = len(distributions)
	data = np.zeros((num_samples, num_distr))
	for idx, distr in enumerate(distributions):
	    data[:, idx] = distr["type"](size=(num_samples,), **distr["kwargs"])
	random_idx = np.random.choice(np.arange(num_distr), size=(num_samples,), p=coefficients)
	# print(random_idx)
	samples = data[np.arange(num_samples), random_idx]
	# plt.hist(sample, bins=100, density=True)
	# plt.show()
	### make sure that samples are within limits 7 - 24 ###
	for idx, sample in enumerate(samples):
		while (sample < 7 and sample > 1) or sample > 24:
			# data = 0 # this is a slow implementation
			if sample > 24:
				sample = sample -24
			print("sample was ", sample)
			# data = 0
			data = distr["type"](size=(1,), **distr["kwargs"])
			random_idx = np.random.choice(np.arange(num_distr), size=(1,), p=coefficients)
			sample = data[0]
			samples[idx] = data[0]
	return samples

# print_samples_graph()
samples = generate_sample(10000)
print(samples)
plt.hist(samples, bins=100, density=True)
plt.show()

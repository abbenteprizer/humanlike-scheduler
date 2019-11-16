# -*- coding: utf-8 -*-
# @Author: abbenteprizer
# @Date:   2019-11-15 13:56:58
# @Last Modified by:   abbenteprizer
# @Last Modified time: 2019-11-16 16:31:57
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
import datetime 
import schedule
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


def generate_samples(num_samples):
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
	samples = data[np.arange(num_samples), random_idx]
	### make sure that samples are within limits 7 - 24 ###
	for idx, sample in enumerate(samples):
		while (sample < 7 and sample > 1) or sample > 24:
			if sample > 24:
				sample = sample -24
			# print("sample was ", sample)
			data = distr["type"](size=(1,), **distr["kwargs"])
			random_idx = np.random.choice(np.arange(num_distr), size=(1,), p=coefficients)
			sample = data[0]
			samples[idx] = data[0]
	return samples

# print_samples_graph()
def print_lots_generated_samples():
	samples = generate_samples(10000)
	# print(samples)
	plt.hist(samples, bins=100, density=True)
	plt.show()

# print_lots_generated_samples()

### convert samples to dates ###
# hours are already good, lets convert number 100 to minutes and seconds
def sample_to_time(samples):
	date_list = []
	for number in samples:
		hours = int(number)
		minutes = int(((number % 1) * 100) * 60 / 100)
		seconds = int(((((number % 1) * 100) % 1) * 100) * 60 / 100)
		# print(number)
		# print("hours = ",hours)
		# print("minutes = ", minutes)
		# print("seoncdonds = ", seconds)
		# print()
		date_list.append(datetime.time(hours,minutes,seconds))
	return date_list

### Now we have a list of datetime object ( no year yet) ###
### lets fix the scheduling ###

date_list = sample_to_time(generate_samples(10))
print(date_list[0].hour)
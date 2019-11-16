# Human-like scheduler
This program is a human-like scheduler that schedules user-specified functions in a manner that mimics the distribution of internet traffic per day.

## Distribution
The distribution consists of two normal distributions and only times between 7am and 1am are accepted. As can be seen in the figure below, the probability of scheduling a task after 22pm is quite low (might add more distributions in the future). 

![Alt text](/distribution.png?raw=true "Distribution")

## How to use
The program is called "humane". 

In "humane" there is a function called "sched" that takes two arguments: \
A function you want to schedule and the frequency (given as number of times per day).

humane.sched(function, frequency)

## Example code

```
import humane

def hello():
	print("hey you")

humane.sched(hello, 10000)
```

Or if you are using a function with arguments.

```
import humane

def hello(name):
	print("hi", name)

humane.sched(lambda: hello("Dave"), 10000)
```


# Human-like scheduler
This program is a human-like scheduler that schedules user-specified functions in a manner that mimics the distribution of internet traffic per day.

## Distribution
The distribution consists of two normal distributions and only times between 7am and 1am are accepted. As can be seen in the figure below, the probability of scheduling a task after 22pm is quite low (might add more distributions in the future). 

![Alt text](/distribution.png?raw=true "Distribution")

## How to use
The program is called "humane". 

In "humane" there is a function called "sched" that takes two arguments namely: \
A function that you want to schedule and the frequency (given as number of times per day).
```
humane.sched(function, frequency)
```

This command is a blocking operation. 

## How it works
When starting the scheduler the program will generate a list of scheduling date which has the size of frequency. The scheduler will then continuously (every second) check if any task should be executed. Each day the scheduler recalculates the list of scheduling dates to avoid repetition of the same dates every day, this is done by default at 6am. The scheduler only guarantees that it will try to execute the user specified function with the number of times as specified in frequency over the lapse of one day. If you start the scheduler after 7am (or before 1am) there is no easy way of determining the exact number of times the scheduler will execute the program that day.

## Example code
The following programs will schedule the function "hello" 10000 times every day.
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


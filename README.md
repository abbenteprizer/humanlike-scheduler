# Humane scheduler
This program is a human-like scheduler that schedules user-specified functions in a manner that mimics the distribution of internet traffic per day.

## Example distribution

![Alt text](/distribution.png?raw=true "Title")

## How to use


## Example code

```
import humane

def hello():
	print("hey you")

humane.humane(hello, 10000)
```

Or if you are using a function with arguments.

```
import humane

def hello(name):
	print("hi", name)

humane.humane(lambda: hello("Dave"), 10000)
```


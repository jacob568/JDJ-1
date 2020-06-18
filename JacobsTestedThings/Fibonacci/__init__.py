def first10Fibonacci():
	currentValue = 0
	previousValue = 0
	nextValue = 1

	counter = 0
	output = ""
	while counter < 10:
		output += str(currentValue) + " "

		previousValue = currentValue
		currentValue = nextValue
		nextValue = previousValue + currentValue
		counter += 1

	return output

def getNthFibonacci(value):
	if value < 1:
		return "Please input a positive, non-zero value"
	currentValue = 0
	previousValue = 0
	nextValue = 1

	counter = 1
	while counter < value:
		previousValue = currentValue
		currentValue = nextValue
		nextValue = previousValue + currentValue
		counter += 1
	return currentValue





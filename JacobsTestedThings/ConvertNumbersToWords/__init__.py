#A dictionary of all the words required to write every number 1 to 9999
wordDict = {
	1 : "one",
	2 : "two",
	3 : "three",
	4 : "four",
	5 : "five",
	6 : "six",
	7 : "seven",
	8 : "eight",
	9 : "nine",
	10 : "ten",
	11 : "eleven",
	12 : "twelve",
	13 : "thirteen",
	14 : "fourteen",
	15 : "fifteen",
	16 : "sixteen",
	17 : "seventeen",
	18 : "eighteen",
	19 : "nineteen",
	20 : "twenty",
	30 : "thirty",
	40 : "forty",
	50 : "fifty",
	60 : "sixty",
	70 : "seventy",
	80 : "eighty",
	90 : "ninety",
	100 : "hundred",
	1000 : "thousand",
}

#When given an value 1 <= x <= 9999, prints out the english for said value
def convertToWords(inputValue):
	output = ""
	splitNumber = splitEveryCharacter(str(inputValue))

	if len(splitNumber) == 4:
		output = get4Digit(splitNumber, output)
	elif len(splitNumber) == 3:
		output = get3Digit(splitNumber, output)
	elif len(splitNumber) == 2:
		output = get2Digit(splitNumber, output)
	elif len(splitNumber) == 1:
		output = get1Digit(splitNumber, output)

	return output


#Splits the number into a list, the length of which is determined by the size of the number
def splitEveryCharacter(word):
	word = str(word)
	return [char for char in word]

def get4Digit(number, output):
	if int(number[0]) > 0:
		output = wordDict[int(number[0])] + " " + wordDict[1000]
	number.pop(0)
	return get3Digit(number, output)

def get3Digit(number, output):
	if int(number[0]) > 0:
		#If the output isn't empty, then a space is added
		if output:
			output += " "
		output += wordDict[int(number[0])] + " " + wordDict[100]

	number.pop(0)
	return get2Digit(number, output)

def get2Digit(number, output):
	#if the first number if 2 or more
	if int(number[0]) > 1:
		if output:
			output += " "
		#times the number by 10 and grab the word for that number. if 3, 3 * 10 = 30.
		output += wordDict[int(number[0]) * 10]
		number.pop(0)
		return get1Digit(number, output)
	#if the first number is 1, it in the teens, this requires the second number.
	elif int(number[0]) == 1:
		if output:
			output += " "
		output += wordDict[int(number[0] + number[1])]
		return output

def get1Digit(number, output):
	if int(number[0]) > 0:
		if output:
			output += " "
		output += wordDict[int(number[0])]
	elif int(number[0]) == 0:
		output = "zero"
	return output

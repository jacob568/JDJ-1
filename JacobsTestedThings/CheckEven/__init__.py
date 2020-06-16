from CmToFtIn import is_number

#Returns true if number is even
def CheckEven(number):
	if is_number(number) == False:
		return "Please input a number!"
	if number % 2 != 0:
		return False
	else:
		return True
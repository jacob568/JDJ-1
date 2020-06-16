#Converts cm reading to feet and inches
def ConvertToFeetAndInch(cm):
	if is_number(cm) == False:
		return "Incorrect input type, please enter a number"
	inches = float(cm) / 2.54
	feet = 0

	working = True
	while working:
		if inches >= 12.0:
			feet += 1;
			inches -= 12.0;
		else:
			return (str(feet) + "ft " + str(round(inches, 1)) + "in")
			working = False

#Checks if the input is a number value
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
import unittest
from CmToFtIn import ConvertToFeetAndInch

class TestThingyMethods(unittest.TestCase):
	def test_correct_conversion(self):
		testInput = 180
		result = ConvertToFeetAndInch(180)
		self.assertEqual(result, "5ft 10.9in")
	def test_correct_conversion2(self):
		testInput = 180
		result = ConvertToFeetAndInch(0)
		self.assertEqual(result, "0ft 0.0in")
	def test_correct_conversion3(self):
		testInput = 180
		result = ConvertToFeetAndInch(1892093)
		self.assertEqual(result, "62076ft 6.5in")
	def test_correct_conversion4(self):
		testInput = 180
		result = ConvertToFeetAndInch(11)
		self.assertEqual(result, "0ft 4.3in")
	def test_incorrect_input(self):
		testInput = "fods"
		result = ConvertToFeetAndInch(testInput)
		self.assertEqual(result, "Incorrect input type, please enter a number")
	def test_incorrect_input2(self):
		testInput = "    "
		result = ConvertToFeetAndInch(testInput)
		self.assertEqual(result, "Incorrect input type, please enter a number")
	def test_incorrect_input3(self):
		testInput = "<sdijs>323231ds'#["
		result = ConvertToFeetAndInch(testInput)
		self.assertEqual(result, "Incorrect input type, please enter a number")

if __name__ == '__main__':
    unittest.main()
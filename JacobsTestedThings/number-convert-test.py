import unittest
from ConvertNumbersToWords import convertToWords, splitEveryCharacter

class TestThingyMethods(unittest.TestCase):
	def test_correct_result(self):
		result = convertToWords(345)
		self.assertEqual(result, "three hundred forty five")
	def test_correct_result2(self):
		result = convertToWords(4923)
		self.assertEqual(result, "four thousand nine hundred twenty three")
	def test_correct_result3(self):
		result = convertToWords(12)
		self.assertEqual(result, "twelve")
	def test_correct_result4(self):
		result = convertToWords(0)
		self.assertEqual(result, "zero")
	def test_correct_result5(self):
		result = convertToWords(9999)
		self.assertEqual(result, "nine thousand nine hundred ninety nine")
	def test_correct_result6(self):
		result = convertToWords(87)
		self.assertEqual(result, "eighty seven")
	def test_correct_result7(self):
		result = convertToWords(17)
		self.assertEqual(result, "seventeen")
	def test_correct_result17(self):
		result = convertToWords(0)
		self.assertEqual(result, "zero")
	def test_correct_result18(self):
		result = convertToWords(2)
		self.assertEqual(result, "two")
	def test_correct_result19(self):
		result = convertToWords(13)
		self.assertEqual(result, "thirteen")
	def test_correct_result111(self):
		result = convertToWords(133)
		self.assertEqual(result, "one hundred thirty three")
	def test_correct_result8(self):
		result = convertToWords(821)
		self.assertEqual(result, "eight hundred twenty one")
	def test_correct_result9(self):
		result = convertToWords(7238)
		self.assertEqual(result, "seven thousand two hundred thirty eight")
	def test_correct_result10(self):
		result = convertToWords(555)
		self.assertEqual(result, "five hundred fifty five")
	def test_split_word(self):
		result = splitEveryCharacter(1314)
		self.assertEqual(result, ['1', '3', '1', '4'])
	def test_split_word2(self):
		result = splitEveryCharacter(1435)
		self.assertEqual(result[3], '5')

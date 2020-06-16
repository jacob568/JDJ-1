import unittest
from CheckEven import CheckEven

class TestCheckEvenMethods(unittest.TestCase):
	def test_correct_result(self):
		result = CheckEven(2)
		self.assertTrue(result)

	def test_false(self):
		result = CheckEven (11)
		self.assertFalse(result)

	def test_incorrect_input(self):
		result = CheckEven("hfioaho")
		self.assertEqual(result, "Please input a number!")
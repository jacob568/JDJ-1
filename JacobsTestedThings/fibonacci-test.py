import unittest
from Fibonacci import first10Fibonacci

class TestThingyMethods(unittest.TestCase):
	def test_correct_result(self):
		result = first10Fibonacci()
		self.assertEqual(result, "0 1 1 2 3 5 8 13 21 34 ")


if __name__ == '__main__':
    unittest.main()
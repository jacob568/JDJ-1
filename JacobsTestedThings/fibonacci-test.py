import unittest
from Fibonacci import first10Fibonacci, getNthFibonacci

class TestThingyMethods(unittest.TestCase):
	def test_correct_result(self):
		result = first10Fibonacci()
		self.assertEqual(result, "0 1 1 2 3 5 8 13 21 34 ") # 55 89 144 233 377 610 987 1597 2584 4181 6765 10946

	def test_correct_result1(self):
		result = getNthFibonacci(0);
		self.assertEqual(result, "Please input a positive, non-zero value")

	def test_correct_result2(self):
		result = getNthFibonacci(9)
		self.assertEqual(result, 21)
	def test_correct_result3(self):
		result = getNthFibonacci(1)
		self.assertEqual(result, 0)
	def test_correct_result4(self):
		result = getNthFibonacci(22)
		self.assertEqual(result, 10946)
	def test_correct_result5(self):
		result = getNthFibonacci(20)
		self.assertEqual(result, 4181)
	def test_correct_result6(self):
		result = getNthFibonacci(100)
		self.assertEqual(result, 218922995834555169026)
	def test_correct_result7(self):
		result = getNthFibonacci(73)
		self.assertEqual(result, 498454011879264)


if __name__ == '__main__':
    unittest.main()
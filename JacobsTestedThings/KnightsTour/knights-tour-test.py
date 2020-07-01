import unittest
from KnightsTour import MoveDirection, CheckComplete, createGrid, GetNewPosition, GetPossibleMovesForLocation

class TestThingyMethods(unittest.TestCase):
	def test_move_direction_correct_result(self):
		result = MoveDirection(0)
		self.assertEqual(result, [2, 1])
	def test_move_direction_correct_result2(self):
		result = MoveDirection(1)
		self.assertEqual(result, [1, 2])
	def test_move_direction_correct_result3(self):
		result = MoveDirection(2)
		self.assertEqual(result, [-1, 2])
	def test_move_direction_correct_result4(self):
		result = MoveDirection(3)
		self.assertEqual(result, [-2, 1])
	def test_move_direction_correct_result5(self):
		result = MoveDirection(4)
		self.assertEqual(result, [-2,-1])
	def test_move_direction_correct_result6(self):
		result = MoveDirection(5)
		self.assertEqual(result, [-1, -2])
	def test_move_direction_correct_result7(self):
		result = MoveDirection(6)
		self.assertEqual(result, [1, -2])
	def test_move_direction_correct_result8(self):
		result = MoveDirection(7)
		self.assertEqual(result, [2, -1])

	def test_create_grid_correct_result(self):
		result = createGrid()
		expected = [["e", "e", "e", "e", "e", "e", "e", "e"], ["e", "e", "e", "e", "e", "e", "e", "e"], ["e", "e", "e", "e", "e", "e", "e", "e"], ["e", "e", "e", "e", "e", "e", "e", "e"], ["e", "e", "e", "e", "e", "e", "e", "e"], ["e", "e", "e", "e", "e", "e", "e", "e"], ["e", "e", "e", "e", "e", "e", "e", "e"], ["e", "e", "e", "e", "e", "e", "e", "e"]]
		self.assertEqual(result, expected)

	def test_check_complete_correct_test(self):
		input = [["1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1"]]
		result = CheckComplete(input, 8)
		self.assertEqual(result, True)
	def test_check_complete_incorrect_test(self):
		input = [["e", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1", "1", "1", "1"]]
		result = CheckComplete(input, 8)
		self.assertEqual(result, False)

	def test_check_new_position_correct(self):
		param1 = [3, 4]
		param2 = [-1, 2]
		result = GetNewPosition(param1, param2)
		self.assertEqual(result, [2, 6])

	def test_check_new_position_correct2(self):
		param1 = [0, 0]
		param2 = [1, 2]
		result = GetNewPosition(param1, param2)
		self.assertEqual(result, [1, 2])

	def test_check_new_position_correct3(self):
		param1 = [7, 3]
		param2 = [1, -2]
		result = GetNewPosition(param1, param2)
		self.assertEqual(result, [8, 1])

	def test_get_possible_moves(self):
		board = [
		["0", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"]]
		result = GetPossibleMovesForLocation([0, 0], board)
		self.assertEqual(result, [0, 1])

	def test_get_possible_moves2(self):
		board = [
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "0"]]
		result = GetPossibleMovesForLocation([7, 7], board)
		self.assertEqual(result, [4, 5])

	def test_get_possible_moves3(self):
		board = [
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "3", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "0", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "4", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"]]
		result = GetPossibleMovesForLocation([4, 4], board)
		self.assertEqual(result, [0, 1, 2, 3, 4, 6])

	def test_get_possible_moves4(self):
		board = [
		["e", "e", "e", "e", "e", "0", "e", "e"], 
		["e", "e", "e", "4", "e", "e", "e", "5"], 
		["e", "e", "e", "e", "e", "e", "3", "e"], 
		["e", "3", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["5", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "5", "e", "e", "e", "e", "e"], 
		["e", "4", "e", "e", "e", "e", "e", "e"]]
		result = GetPossibleMovesForLocation([5, 0], board)
		self.assertEqual(result, [2])

	def test_get_possible_moves5(self):
		board = [
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "0", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"]]
		result = GetPossibleMovesForLocation([6, 2], board)
		self.assertEqual(result, [1, 2, 3, 4, 5, 6])

	def test_get_possible_moves6(self):
		board = [
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "0", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"]]
		result = GetPossibleMovesForLocation([3, 6], board)
		self.assertEqual(result, [0, 3, 4, 5, 6, 7])
	def test_get_possible_moves7(self):
		board = [
		["e", "e", "e", "e", "e", "e", "e", "0"], 
		["e", "e", "e", "e", "e", "3", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "3", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"], 
		["e", "e", "e", "e", "e", "e", "e", "e"]]
		result = GetPossibleMovesForLocation([0, 7], board)
		self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()

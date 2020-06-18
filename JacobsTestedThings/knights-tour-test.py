import unittest
from KnightsTour import MoveDirection, CheckComplete, createGrid, GetNewPosition, AddAttemptToList, GetPossibleMovesForLocation

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

	def test_add_attempts_to_attempted_actions_list(self):
		param1 = [[1, 4, 5, 7], [0, 1, 2, 3, 4, 5, 6, 7], [2, 4]]
		param2 = [1, 3, 5, 7]
		result = AddAttemptToList(param1, param2)
		self.assertEqual(result, [[1, 4, 5, 7], [0, 1, 2, 3, 4, 5, 6, 7], [2, 4], [1, 3, 5, 7]])

	def test_get_possible_moves(self):
		result = GetPossibleMovesForLocation([0, 0])
		self.assertEqual(result, [0, 1])

	def test_get_possible_moves2(self):
		result = GetPossibleMovesForLocation([7, 7])
		self.assertEqual(result, [4, 5])

	def test_get_possible_moves3(self):
		result = GetPossibleMovesForLocation([4, 4])
		self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7])

	def test_get_possible_moves4(self):
		result = GetPossibleMovesForLocation([0, 5])
		self.assertEqual(result, [0, 1, 6, 7])
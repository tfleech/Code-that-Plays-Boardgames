from Base_Classes import *
import numpy as np

class TicTacToe_Player(Player):
	def __init__(self, W, B, Wins=0, Losses=0, name="Player"):
		super().__init__(Wins, Losses, name, game_type="TicTacToe")
		self.W = W
		self.B = B

	def next_move(self, game):
		x = np.array(game.board)
		if sum(x) == 1:
			x = x*-1

		y = np.matmul(self.W, x) + self.B
		poss_moves = np.argsort(y)
		for i in poss_moves:
			if game.board[i] == 0:
				return i
		print("Error: No moves possible")
		return None

class rand_TicTacToe_Player(Player):
	def __init__(self, Wins=0, Losses=0, name="Player"):
		super().__init__(Wins, Losses, name, game_type="TicTacToe")

	def next_move(self, game):
		if not game.is_available_move():
			print("ERROR: There is no valid move")
			return None

		moves = list(range(9))
		np.random.shuffle(moves)
		for m in moves:
			if game.is_move_valid(m):
				return m

		return None

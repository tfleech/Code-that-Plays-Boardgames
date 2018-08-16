from Base_Classes import *
import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/..")


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
			if game.is_move_valid(i):
				return i
		print("Error: No moves possible")
		return None

class rand_TicTacToe_Player(Player):
	def __init__(self, Wins=0, Losses=0, name="Player"):
		super().__init__(Wins, Losses, name, game_type="TicTacToe")
		rand_W = np.random.rand(9,9)*2 - np.ones((9,9))
		rand_B = np.random.rand(9)*2 - np.ones(9)
		self.W = rand_W
		self.B = rand_B

	def next_move(self, game):
		x = np.array(game.board)
		if sum(x) == 1:
			x = x*-1

		y = np.matmul(self.W, x) + self.B
		poss_moves = np.argsort(y)
		for i in poss_moves:
			if game.is_move_valid(i):
				return i
		print("Error: No moves possible")
		return None

class human_TicTacToe_Player(Player):
	def __init__(self, Wins=0, Losses=0, name = "Player"):
		super().__init__(Wins, Losses, name, game_type="TicTacToe")

	def next_move(self, game):
		game.print_board()
		move = None
		while not game.is_move_valid(move):
			move = input("Enter a move: ")
		return int(move)
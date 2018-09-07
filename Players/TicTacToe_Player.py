from Base_Classes import *
import numpy as np
import sys, os
from datetime import datetime
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../minimax")
from TicTacToe_Minimax import TicTacToe_Minimax as Tmm


class TicTacToe_Player(Player):
	def __init__(self, W, B, Wins=0, Losses=0, name="Player"):
		super().__init__(Wins, Losses, name, game_type="TicTacToe")
		self.W = W
		self.B = B

	def next_move(self, game, board):
		x = np.array(board)
		if sum(x) == 1:
			x = x*-1

		y = np.matmul(self.W, x) + self.B
		poss_moves = np.argsort(y)
		for i in poss_moves:
			if game.is_move_valid(i, board):
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

	def next_move(self, game, board):
		x = np.array(board)
		if sum(x) == 1:
			x = x*-1

		y = np.matmul(self.W, x) + self.B
		poss_moves = np.argsort(y)
		for i in poss_moves:
			if game.is_move_valid(i, board):
				return i
		print("Error: No moves possible")
		return None

class human_TicTacToe_Player(Player):
	def __init__(self, Wins=0, Losses=0, name = "Player"):
		super().__init__(Wins, Losses, name, game_type="TicTacToe")

	def next_move(self, game, board):
		game.print_board(board)
		move = None
		while not game.is_move_valid(move, board):
			move = input("Enter a move: ")
		return int(move)

class minimax_TicTacToe_Player(Player):
	def __init__(self, Wins=0, Losses=0, name="Player", time_limit = 1000000):
		super().__init__(Wins, Losses, name, game_type="TicTacToe")
		self.time_limit = time_limit

	def next_move(self, game, board):
		best_move = None
		depth = 1

		start_time = datetime.now()
		current_time = start_time

		while (current_time - start_time).microseconds <= 0.25*self.time_limit:
			m = Tmm(game, depth)
			best_move = m.get_next_move(board, game.turn)

			depth += 1
			if depth > 9:
				break
			current_time = datetime.now()

#		print(depth)
		return best_move
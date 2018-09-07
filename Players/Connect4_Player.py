from Base_Classes import *
import numpy as np
import sys, os
from datetime import datetime
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../minimax")
from Connect4_Minimax import Connect4_Minimax as C4mm

class rand_Connect4_Player(Player):
	def __init__(self, Wins=0, Losses=0, name="Player"):
		super().__init__(Wins, Losses, name, game_type="Connect4")

	def next_move(self, game, board):
		if not game.is_available_move(board):
			print("ERROR: There is no valid move")
			return None

		moves = list(range(board.shape[1]))
		np.random.shuffle(moves)
		for m in moves:
			if game.is_move_valid(m, board):
				return m

		return None

class human_Connect4_Player(Player):
	def __init__(self, Wins=0, Losses=0, name = "Player"):
		super().__init__(Wins, Losses, name, game_type="Connect4")

	def next_move(self, game, board):
		game.print_board(board)
		print("0|1|2|3|4|5|6")
		move = None
		while not game.is_move_valid(move, board):
			move = input("Enter a move: ")
		return int(move)

class minimax_Connect4_Player(Player):
	def __init__(self, Wins=0, Losses=0, name="Player", time_limit = 1000000):
		super().__init__(Wins, Losses, name, game_type="Connect4")
		self.time_limit = time_limit

	def next_move(self, game, board):
		best_move = None
		depth = 1

		start_time = datetime.now()
		current_time = start_time

		while (current_time - start_time).microseconds <= 0.25*self.time_limit:
			m = C4mm(game, depth)
			best_move = m.get_next_move(board, game.turn)

			depth += 1
			if depth > 9:
				break
			current_time = datetime.now()

		print(depth)
		return best_move
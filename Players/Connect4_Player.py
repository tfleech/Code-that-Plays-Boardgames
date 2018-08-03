from Base_Classes import *
import numpy as np

class rand_Connect4_Player(Player):
	def __init__(self, Wins=0, Losses=0, name="Player"):
		super().__init__(Wins, Losses, name, game_type="Connect4")

	def next_move(self, game):
		if not game.is_available_move():
			print("ERROR: There is no valid move")
			return None

		moves = list(range(game.board.shape[1]))
		np.random.shuffle(moves)
		for m in moves:
			if game.is_move_valid(m):
				return m

		return None
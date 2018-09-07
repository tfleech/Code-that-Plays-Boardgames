from Minimax_Base_Class import *

class TicTacToe_Minimax(Minimax):
	def __init__(self, game, max_depth = 4):
		super().__init__(max_depth)
		self.game = game

	def evaluate_state(self, board, player):
		game_over = self.game.is_gameover(board)
		if game_over[0]:
			if game_over[1]==player:
				return 999
			elif game_over[1]==None:
				return 0
			else:
				return -999

		return 0

	def get_next_states(self, board, player):
		return self.game.available_moves(board)

	def make_move(self, board, player, move):
		return self.game.update_board(move, board, player)

	def is_game_over(self, board):
		return self.game.is_gameover(board)[0]

	def next_player(self, player):
		if player == self.game.player1:
			return self.game.player2
		return self.game.player1

	def undo_move(self, board, player, move):
		board[move] = 0
		return board
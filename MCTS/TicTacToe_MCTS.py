from MCTS_Base_Class import *

class TicTacToe_MCTS(MCTS):
	def __init__(self, game, board):
		super().__init__(board, game.turn)
		self.game = game

	def get_next_states(self, board, player):
		return self.game.available_moves(board)

	def make_move(self, board, player, move):
		return self.game.update_board_copy(move, board, player)

	def is_game_over(self, board):
		return self.game.is_gameover(board)

	def next_player(self, player):
		if player == self.game.player1:
			return self.game.player2
		return self.game.player1

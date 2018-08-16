import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/..")

from Minimax_Base_Class import *
from Players import TicTacToe_Player as T
from Games import TicTacToe_Game as G
from Base_Classes import *

class TicTacToe_Minimax(Minimax):
	def __init__(self, game):
		super().__init__()
		self.game = game

	def evaluate_state(self, board, player):
		game_over = self.game.is_gameover(update=False, board=board)
		if game_over[0]:
			if game_over[1]==player:
				return 999
			elif game_over[1]==None:
				return 0
			else:
				return -999

		return 0

	def get_next_states(self, board, player):
		return self.game.available_moves(board=board)

	def make_move(self, board, player, move):
		return self.game.update_board(move, update=False, board=board, player=player)

	def is_game_over(self, board):
		return self.game.is_gameover(update=False, board=board)[0]

	def next_player(self, player):
		if player == self.game.player1:
			return self.game.player2
		return self.game.player1

class minimax_TicTacToe_Player(Player):
	def __init__(self, Wins=0, Losses=0, name="Player"):
		super().__init__(Wins, Losses, name, game_type="TicTacToe")

	def next_move(self, game):
		m = TicTacToe_Minimax(game)
		return m.get_next_move(game.board, game.turn)

p1 = T.rand_TicTacToe_Player(name="Player1")
p2 = minimax_TicTacToe_Player(name="Player2")

g = G.TicTacToe()
D = Driver(game=g)
print(D.single_game(p2, p1, print_game=True))

#g = G.TicTacToe()
#p1 = TicTacToe_Minimax(g)
#print(p1.get_next_move([0,0,0,0,0,0,0,0,0], g.turn))
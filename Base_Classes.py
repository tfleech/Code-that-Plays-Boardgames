class Game:
	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2
		self.board = None
		self.turn = player1
		self.gameover = False
		self.winner = 0

	def is_gameover(self):
		"""
		Set self.gameover and return answer
		"""
		pass

	def make_move(self, move):
		"""
		Update self.board with new move
		"""

		if(self.turn == self.player1):
			self.turn = self.player2
		else:
			self.turn = self.player1
		self.is_gameover()

	def is_move_valid(self, move):
		pass

	def print_board(self):
		pass

class Player:
	def __init__(self, Wins=0, Losses=0, name="Player"):
		self.Wins = Wins
		self.Losses = Losses
		self.name = name

	def next_move(self, game):
		pass

	def print_stats(self):
		print(self.name + " Stats: Wins: " + str(self.Wins) + "  Losses: " + str(self.Losses))
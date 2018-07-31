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
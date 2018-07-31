class Game:
	def __init__(self, player1=1, player2=-1):
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

class Driver:
	def __init__(self, player1, player2, game=Game()):
		self.p1 = player1
		self.p2 = player2
		self.game = game

	def run_game(self, print_game=False):
		while(not self.game.is_gameover()):
			if self.game.turn == self.game.player1:
				n = self.p1.next_move(self.game)
				self.game.make_move(n)
			else:
				n = self.p2.next_move(self.game)
				self.game.make_move(n)

			if print_game:
				self.game.print_board()

		if self.game.winner == self.game.player1:
			self.p1.Wins += 1
			self.p2.Losses += 1
		elif self.game.winner == self.game.player2:
			self.p1.Losses += 1
			self.p2.Wins += 1
		return self.game.winner
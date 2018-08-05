import numpy as np

class Game:
	def __init__(self, player1=1, player2=-1, game_type = None):
		self.player1 = player1
		self.player2 = player2
		self.board = None
		self.turn = player1
		self.gameover = False
		self.winner = 0
		self.game_type = game_type

	def is_gameover(self):
		"""
		Set self.gameover and return answer
		"""
		raise NotImplementedError

	def update_board(self, move):

		raise NotImplementedError

	def is_available_move(self):
		
		raise NotImplementedError


	def make_move(self, move):
		"""
		Update self.board with new move
		"""

		if self.is_move_valid(move):
			try:
				self.update_board(move)
			except Exception as e:
				print("ERROR: Board update failed")
				raise e
			
		else:
			print("ERROR: invalid move")
			#TODO:
			#Return error code
			return

		if(self.turn == self.player1):
			self.turn = self.player2
		else:
			self.turn = self.player1
		self.is_gameover()

	def is_move_valid(self, move):
		return True

	def new_game(self):
		pass

	def print_board(self):
		pass

class Player:
	def __init__(self, Wins=0, Losses=0, name="Player", game_type = None):
		self.Wins = Wins
		self.Losses = Losses
		self.name = name
		self.game_type = game_type

	def next_move(self, game):
		raise NotImplementedError

	def print_stats(self):
		print(self.name + " Stats: Wins: " + str(self.Wins) + "  Losses: " + str(self.Losses))

class Driver:
	def __init__(self, players = [], game = Game()):
		self.players = players
		self.game = game

	def single_game(self, player1, player2, print_game=False):

		self.game.new_game()
		
		if player1.game_type != self.game.game_type:
			print("ERROR: Player1 is playing " + str(player1.game_type) + " but the game is " + str(self.game.game_type))
			return
		if player2.game_type != self.game.game_type:
			print("ERROR: Player2 is playing " + str(player2.game_type) + " but the game is " + str(self.game.game_type))
			return

		while(not self.game.is_gameover()):
			n = None
			if self.game.turn == self.game.player1:

				try:
					n = player1.next_move(self.game)
				except Exception as e:
					print("ERROR: Player1's next_move function failed")
					raise e

				if not self.game.is_move_valid(n):
					print("ERROR: Player1 returned an invalid move")
					return

			else:

				try:
					n = player2.next_move(self.game)
				except Exception as e:
					print("ERROR: Player2's next_move function failed")
					raise e

				if not self.game.is_move_valid(n):
					print("ERROR: Player2 returned an invalid move")
					return

			#TODO:
			#catch return error codes
			self.game.make_move(n)

			if print_game:
				self.game.print_board()

		if self.game.winner == self.game.player1:
			player1.Wins += 1
			player2.Losses += 1
			return player1.name
		elif self.game.winner == self.game.player2:
			player1.Losses += 1
			player2.Wins += 1
			return player2.name
		return "Draw"

	def many_games(self, num_games, players=[], print_results=False):

		if len(players)==0:
			if len(self.players)==0:
				print("ERROR: There are no players")
				return
			else:
				players = self.players

		for p in players:
			if self.game.game_type != p.game_type:
				print("ERROR: Not all players are playing " + str(self.game.game_type))
				return

		for i in range(num_games):
			p1 = np.random.choice(players)
			p2 = np.random.choice(players)
			winner = self.single_game(p1, p2)

			if print_results:
				print("The winner of game " + str(i) + " is " + str(winner))

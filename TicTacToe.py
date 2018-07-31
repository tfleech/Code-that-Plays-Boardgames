from Base_Classes import *
import numpy as np

class TicTacToe(Game):
	def __init__(self, board=np.zeros(9)):
		super().__init__(player1 = 1, player2 = -1)
		self.board = board

	def is_gameover(self):
		test = (self.board[0] + self.board[1] + self.board[2]) == 3
		test |= (self.board[3] + self.board[4] + self.board[5]) == 3
		test |= (self.board[6] + self.board[7] + self.board[8]) == 3
		test |= (self.board[0] + self.board[3] + self.board[6]) == 3
		test |= (self.board[1] + self.board[4] + self.board[7]) == 3
		test |= (self.board[2] + self.board[5] + self.board[8]) == 3
		test |= (self.board[0] + self.board[4] + self.board[8]) == 3
		test |= (self.board[2] + self.board[4] + self.board[6]) == 3
		if test:
			self.winner = self.player1
			self.gameover = True
			return True

		#test = (self.board[0] + self.board[1] + self.board[2]) == 12
		#test |= (self.board[3] + self.board[4] + self.board[5]) == 12
		#test |= (self.board[6] + self.board[7] + self.board[8]) == 12
		#test |= (self.board[0] + self.board[3] + self.board[6]) == 12
		#test |= (self.board[1] + self.board[4] + self.board[7]) == 12
		#test |= (self.board[2] + self.board[5] + self.board[8]) == 12
		#test |= (self.board[0] + self.board[4] + self.board[8]) == 12
		#test |= (self.board[2] + self.board[4] + self.board[6]) == 12
		test = (self.board[0] + self.board[1] + self.board[2]) == -3
		test |= (self.board[3] + self.board[4] + self.board[5]) == -3
		test |= (self.board[6] + self.board[7] + self.board[8]) == -3
		test |= (self.board[0] + self.board[3] + self.board[6]) == -3
		test |= (self.board[1] + self.board[4] + self.board[7]) == -3
		test |= (self.board[2] + self.board[5] + self.board[8]) == -3
		test |= (self.board[0] + self.board[4] + self.board[8]) == -3
		test |= (self.board[2] + self.board[4] + self.board[6]) == -3
		if test:
			self.winner = self.player2
			self.gameover = True
			return True

		for i in range(9):
			if self.board[i] == 0:
				return False
		self.gameover = True
		self.winner = None
		return True

	def is_move_valid(self, move):
		return self.board[move] == 0

	def make_move(self, move):
		if self.is_move_valid(move):
			self.board[move] = self.turn

		if (self.turn == self.player1):
			self.turn = self.player2
		else:
			self.turn = self.player1

		self.is_gameover()

	def print_board(self):
		for i in range(3):
			s = ""
			for j in range(3):
				if self.board[j+3*i] == 0:
					s+="_"
				elif self.board[j+3*i] == self.player1:
					s+="X"
				else:
					s+="O"
			print(s)
		print('\n')

class TicTacToe_Player(Player):
	def __init__(self, W, B, Wins=0, Losses=0, name="Player"):
		super().__init__(Wins, Losses, name)
		self.W = W
		self.B = B

	def next_move(self, game):
		x = np.array(game.board)
		if sum(x) == 1:
			x = x*-1

		y = np.matmul(self.W, x) + self.B
		poss_moves = np.argsort(y)
		for i in poss_moves:
			if game.board[i] == 0:
				return i
		print("Error: No moves possible")
		return None

	#TODO
	#perc_against_random
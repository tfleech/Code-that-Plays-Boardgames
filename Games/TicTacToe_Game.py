from Base_Classes import *
import numpy as np

class TicTacToe(Game):
	def __init__(self, board=np.zeros(9)):
		super().__init__(game_type="TicTacToe")
		self.board = board
		self.X = 1
		self.O = -1

	def new_game(self):
		self.board = np.zeros(9)
		self.gameover = False
		self.winner = None

	def is_gameover(self):
		test = (self.board[0] + self.board[1] + self.board[2]) == 3*self.X
		test |= (self.board[3] + self.board[4] + self.board[5]) == 3*self.X
		test |= (self.board[6] + self.board[7] + self.board[8]) == 3*self.X
		test |= (self.board[0] + self.board[3] + self.board[6]) == 3*self.X
		test |= (self.board[1] + self.board[4] + self.board[7]) == 3*self.X
		test |= (self.board[2] + self.board[5] + self.board[8]) == 3*self.X
		test |= (self.board[0] + self.board[4] + self.board[8]) == 3*self.X
		test |= (self.board[2] + self.board[4] + self.board[6]) == 3*self.X
		if test:
			self.winner = self.player1
			self.gameover = True
			return True

		test = (self.board[0] + self.board[1] + self.board[2]) == 3*self.O
		test |= (self.board[3] + self.board[4] + self.board[5]) == 3*self.O
		test |= (self.board[6] + self.board[7] + self.board[8]) == 3*self.O
		test |= (self.board[0] + self.board[3] + self.board[6]) == 3*self.O
		test |= (self.board[1] + self.board[4] + self.board[7]) == 3*self.O
		test |= (self.board[2] + self.board[5] + self.board[8]) == 3*self.O
		test |= (self.board[0] + self.board[4] + self.board[8]) == 3*self.O
		test |= (self.board[2] + self.board[4] + self.board[6]) == 3*self.O
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

	def is_available_move(self):
		for i in self.board.flatten():
			if i == 0:
				return True
		return False

	def update_board(self, move):
		self.board[move] = self.turn

	def print_board(self):
		for i in range(3):
			s = ""
			for j in range(3):
				if self.board[j+3*i] == 0:
					s+="_"
				elif self.board[j+3*i] == self.X:
					s+="X"
				else:
					s+="O"
			print(s)
		print('\n')
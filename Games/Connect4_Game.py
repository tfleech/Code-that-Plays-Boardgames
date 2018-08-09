import numpy as np
from Base_Classes import *

class Connect4(Game):
	def __init__(self, board = np.zeros((6,7))):
		super().__init__(game_type="Connect4")
		self.board = board
		self.Red = 1
		self.Black = -1

	def new_game(self):
		self.board = np.zeros((6,7))
		self.gameover = False
		self.winner = 0

	def check_column(self, player):
		for i in range(self.board.shape[1] - 1):
			for j in range(self.board.shape[0] - 3):
				test = self.board[j][i] + self.board[j+1][i] + self.board[j+2][i] + self.board[j+3][i]
				if test == 4*player:
					return True
		return False

	def check_row(self, player):
		for i in range(self.board.shape[1] - 3):
			for j in range(self.board.shape[0] - 1):
				test = self.board[j][i] + self.board[j][i+1] + self.board[j][i+2] + self.board[j][i+3]
				if test == 4*player:
					return True
		return False

	def check_forward_diag(self, player):
		for j in range(self.board.shape[0] - 3):
			for i in range(self.board.shape[1] - 3):
				test = self.board[j][i+3] + self.board[j+1][i+2] + self.board[j+2][i+1] + self.board[j+3][i]
				if test == 4*player:
					return True
		return False

	def check_backward_diag(self, player):
		for j in range(self.board.shape[0] - 3):
			for i in range(self.board.shape[1] - 3):
				test = self.board[j][i] + self.board[j+1][i+1] + self.board[j+2][i+2] + self.board[j+3][i+3]
				if test == 4*player:
					return True
		return False


	def is_gameover(self):
		if self.check_column(self.Red) or self.check_row(self.Red) or self.check_forward_diag(self.Red) or self.check_backward_diag(self.Red):
			self.winner = self.player1
			self.gameover = True
			return True
		if self.check_column(self.Black) or self.check_row(self.Black) or self.check_forward_diag(self.Black) or self.check_backward_diag(self.Black):
			self.winner = self.player2
			self.gameover = True
			return True

		if not self.is_available_move():
			self.gameover = True
			return True

		return False

	def is_available_move(self):
		for i in self.board.flatten():
			if i == 0:
				return True
		return False

	def is_move_valid(self, move):
		if move == None:
			return False
		move = int(move)
		if move < 0 or move > 6:
			print("out of range")
			return False
		return self.board[0][move] == 0

	def update_board(self, move):
		for i in range(self.board.shape[0]):
			if self.board[self.board.shape[0]-1-i][move] == 0:
				self.board[self.board.shape[0]-1-i][move] = self.turn
				break

	def print_board(self):
		for i in range(self.board.shape[0]):
			s = ""
			for j in range(self.board.shape[1]):
				if self.board[i][j] == 0:
					s+=" "
				elif self.board[i][j] == self.Red:
					s+="X"
				else:
					s+="O"
				s+="|"
			print(s[:-1])
			if i != self.board.shape[0]-1:
				print("---------------")
		print('\n')
import numpy as np
from Base_Classes import *

class Connect4(Game):
	def __init__(self, board = np.zeros((6,7))):
		super().__init__(game_type="Connect4")
		self.Red = 1
		self.Black = -1

	def new_board(self):
		return np.zeros((6,7))

	def check_column(self, player, board):
		for i in range(board.shape[1] - 1):
			for j in range(board.shape[0] - 3):
				test = board[j][i] + board[j+1][i] + board[j+2][i] + board[j+3][i]
				if test == 4*player:
					return True
		return False

	def check_row(self, player, board):
		for i in range(board.shape[1] - 3):
			for j in range(board.shape[0] - 1):
				test = board[j][i] + board[j][i+1] + board[j][i+2] + board[j][i+3]
				if test == 4*player:
					return True
		return False

	def check_forward_diag(self, player, board):
		for j in range(board.shape[0] - 3):
			for i in range(board.shape[1] - 3):
				test = board[j][i+3] + board[j+1][i+2] + board[j+2][i+1] + board[j+3][i]
				if test == 4*player:
					return True
		return False

	def check_backward_diag(self, player, board):
		for j in range(board.shape[0] - 3):
			for i in range(board.shape[1] - 3):
				test = board[j][i] + board[j+1][i+1] + board[j+2][i+2] + board[j+3][i+3]
				if test == 4*player:
					return True
		return False


	def is_gameover(self, board):
		if self.check_column(self.Red, board) or self.check_row(self.Red, board) or self.check_forward_diag(self.Red, board) or self.check_backward_diag(self.Red, board):
			return (True, self.player1)
		if self.check_column(self.Black, board) or self.check_row(self.Black, board) or self.check_forward_diag(self.Black, board) or self.check_backward_diag(self.Black, board):
			return (True, self.player2)

		if not self.is_available_move(board):
			return (True, None)

		return (False, None)

	def is_available_move(self, board):
		for i in board.flatten():
			if i == 0:
				return True
		return False

	def is_move_valid(self, move, board):
		if move == None:
			return False
		move = int(move)
		if move < 0 or move > 6:
			print("out of range")
			return False
		return board[0][move] == 0

	def update_board(self, move, board, player):
		for i in range(board.shape[0]):
			if board[board.shape[0]-1-i][move] == 0:
				board[board.shape[0]-1-i][move] = player
				return board

	def print_board(self, board):
		for i in range(board.shape[0]):
			s = ""
			for j in range(board.shape[1]):
				if board[i][j] == 0:
					s+=" "
				elif board[i][j] == self.Red:
					s+="X"
				else:
					s+="O"
				s+="|"
			print(s[:-1])
			if i != board.shape[0]-1:
				print("---------------")
		print('\n')
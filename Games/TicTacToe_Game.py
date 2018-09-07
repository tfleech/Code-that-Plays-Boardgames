from Base_Classes import *
import numpy as np

class TicTacToe(Game):
	def __init__(self, board=np.zeros(9)):
		super().__init__(game_type="TicTacToe")
		self.X = 1
		self.O = -1

	def new_board(self):
		return np.zeros(9)

	def is_gameover(self, board):

		test = (board[0] + board[1] + board[2]) == 3*self.X
		test |= (board[3] + board[4] + board[5]) == 3*self.X
		test |= (board[6] + board[7] + board[8]) == 3*self.X
		test |= (board[0] + board[3] + board[6]) == 3*self.X
		test |= (board[1] + board[4] + board[7]) == 3*self.X
		test |= (board[2] + board[5] + board[8]) == 3*self.X
		test |= (board[0] + board[4] + board[8]) == 3*self.X
		test |= (board[2] + board[4] + board[6]) == 3*self.X
		if test:
			return (True, self.player1)

		test = (board[0] + board[1] + board[2]) == 3*self.O
		test |= (board[3] + board[4] + board[5]) == 3*self.O
		test |= (board[6] + board[7] + board[8]) == 3*self.O
		test |= (board[0] + board[3] + board[6]) == 3*self.O
		test |= (board[1] + board[4] + board[7]) == 3*self.O
		test |= (board[2] + board[5] + board[8]) == 3*self.O
		test |= (board[0] + board[4] + board[8]) == 3*self.O
		test |= (board[2] + board[4] + board[6]) == 3*self.O
		if test:
			return (True, self.player2)

		for i in range(9):
			if board[i] == 0:
				return (False, None)
		return (True, None)

	def is_move_valid(self, move, board):
		if move == None:
			return False
		move = int(move)
		if move < 0 or move > 8:
			print("out of range")
			return False
		return board[move] == 0

	def is_available_move(self, board):
		for i in board.flatten():
			if i == 0:
				return True
		return False

	def available_moves(self, board):
		res = []

		for i in range(len(board)):
			if board[i] == 0:
				res.append(i)
		return res

	def update_board(self, move, board, player=None):
		if board==[] or player==None:
			print("Asked for make_move without update but did not supply board and player")
			return None
		else:
			board[move] = player
			return board

	def print_board(self, board):
		for i in range(3):
			s = ""
			for j in range(3):
				if board[j+3*i] == 0:
					s+="_"
				elif board[j+3*i] == self.X:
					s+="X"
				else:
					s+="O"
			print(s)
		print('\n')
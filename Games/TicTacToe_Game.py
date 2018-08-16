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

	def is_gameover(self, update=True, board=[]):
		if update:
			board = self.board
		else:
			if board==[]:
				print("No update but did not provide a board")
				return

		test = (board[0] + board[1] + board[2]) == 3*self.X
		test |= (board[3] + board[4] + board[5]) == 3*self.X
		test |= (board[6] + board[7] + board[8]) == 3*self.X
		test |= (board[0] + board[3] + board[6]) == 3*self.X
		test |= (board[1] + board[4] + board[7]) == 3*self.X
		test |= (board[2] + board[5] + board[8]) == 3*self.X
		test |= (board[0] + board[4] + board[8]) == 3*self.X
		test |= (board[2] + board[4] + board[6]) == 3*self.X
		if test:
			if update:
				self.winner = self.player1
				self.gameover = True
				return True
			else:
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
			if update:
				self.winner = self.player2
				self.gameover = True
				return True
			else:
				return (True, self.player2)

		for i in range(9):
			if board[i] == 0:
				if update:
					return False
				else:
					return (False, None)
		if update:
			self.gameover = True
			self.winner = None
			return True
		else:
			return (True, None)

	def is_move_valid(self, move):
		if move == None:
			return False
		move = int(move)
		if move < 0 or move > 8:
			print("out of range")
			return False
		return self.board[move] == 0

	def is_available_move(self):
		for i in self.board.flatten():
			if i == 0:
				return True
		return False

	def available_moves(self, board=[]):
		res = []
		if board == []:
			board = self.board.flatten()

		for i in range(len(board)):
			if board[i] == 0:
				res.append(i)
		return res

	def update_board(self, move, update=True, board=[], player=None):
		if update:
			self.board[move] = self.turn
			return
		else:
			if board==[] or player==None:
				print("Asked for make_move without update but did not supply board and player")
				return
			else:
				board[move] = player
				return board

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
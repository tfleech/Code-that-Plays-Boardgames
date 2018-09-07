import numpy as np
import sys, os

class Minimax():
	def __init__(self, max_depth = 4):
		self.max_depth = max_depth

	def evaluate_state(self, board, player):
		pass

	def get_next_states(self, board, player):
		pass

	def make_move(self, board, move):
		pass

	def is_game_over(self, board):
		pass

	def next_player(self, player):
		pass

	def get_next_move(self, board, player):
		best_move = None
		best_score = -9999
		alpha = -9999
		beta = 9999

		for m in self.get_next_states(board, player):
			board = self.make_move(board, player, m)
			#print(board)
			#print("<<<<<<<<<<<<<<<<<<<<<<<<<<")

			move_score = self.MIN(board, player, self.next_player(player), 0, alpha, beta)

			#print(">>>>>>>>>>>>>>>>>>>>>>>>>>")

			if move_score > best_score:
				best_move = m
				best_score = move_score
			board = self.undo_move(board, player, m)

			alpha = max(alpha, best_score)
			if (beta <= alpha):
				break
				#pass

			#print(m)
			#print(move_score)
		return best_move

	def MIN(self, board, player, turn, depth, alpha, beta):
		#print("MIN")
		if self.is_game_over(board):
			#print("gameover")
			return self.evaluate_state(board, player)
		if depth >= self.max_depth:
			#print("max_depth")
			return self.evaluate_state(board, player)

		best_score = 9999
		for m in self.get_next_states(board, turn):
			if (type(board) == type(None)):
				print("Board None in for")
			board = self.make_move(board, turn, m)
			#print(board)
			#print("<<<<<<<<<<<<<<<<<<<<<<<<<<")
			score = self.MAX(board, player, self.next_player(turn), depth+1, alpha, beta)
			#print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
			if (score < best_score):
				best_score = score
			board = self.undo_move(board, turn, m)

			beta = min(beta, best_score)
			if (beta <= alpha):
				break
				#pass

			#print(m)
			#print(score)
		return best_score

	def MAX(self, board, player, turn, depth, alpha, beta):
		#print("MAX")
		if self.is_game_over(board):
			#print("gameover")
			return self.evaluate_state(board, player)
		if depth >= self.max_depth:
			#print("max_depth")
			return self.evaluate_state(board, player)

		best_score = -9999
		for m in self.get_next_states(board, turn):
			board = self.make_move(board, turn, m)
			#print(board)
			#print("<<<<<<<<<<<<<<<<<<<<<<<<<<")
			score = self.MIN(board, player, self.next_player(turn), depth+1, alpha, beta)
			#print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
			if (score > best_score):
				best_score = score
			board = self.undo_move(board, turn, m)

			alpha = max(alpha, best_score)
			if (beta <= alpha):
				#break
				pass

			#print(m)
			#print(score)
		return best_score
import numpy as np
import sys, os

class Minimax():
	def __init__(self):
		self.max_depth = 4

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
		evaluated_moves = {}

		for m in self.get_next_states(board, player):
			board = self.make_move(board, player, m)
			evaluated_moves[tuple(board)] = self.MIN(board, player, self.next_player(player), 0)
			if evaluated_moves[tuple(board)] > best_score:
				best_move = m
				best_score = evaluated_moves[tuple(board)]
				#print("New Best Score")
				#print(best_score)
			board[m] = 0
		return best_move

	def MIN(self, board, player, turn, depth):
		#print("MIN")
		#print(depth)
		#print(board)
		if self.is_game_over(board):
			return self.evaluate_state(board, player)
		if depth >= self.max_depth:
			return self.evaluate_state(board, player)

		best_score = 9999
		for m in self.get_next_states(board, turn):
			#print("min board")
			#print(board)
			board = self.make_move(board, turn, m)
			score = self.MAX(board, player, self.next_player(turn), depth+1)
			if (score < best_score):
				#print("New Min")
				#print(board)
				#print(score)
				best_score = score
			board[m] = 0
		return best_score

	def MAX(self, board, player, turn, depth):
		#print("MAX")
		#print(depth)
		#print(board)
		if self.is_game_over(board):
			return self.evaluate_state(board, player)
		if depth >= self.max_depth:
			return self.evaluate_state(board, player)

		best_score = -9999
		for m in self.get_next_states(board, turn):
			#print("max board")
			#print(board)
			board = self.make_move(board, turn, m)
			score = self.MIN(board, player, self.next_player(turn), depth+1)
			if (score > best_score):
				#print("New Max")
				#print(board)
				#print(score)
				best_score = score
			board[m] = 0
		return best_score
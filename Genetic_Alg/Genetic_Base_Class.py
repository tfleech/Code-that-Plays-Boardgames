import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/..")

from Base_Classes import *
from Games import TicTacToe_Game

class Generation:
	def __init__(self, Members):
		self.members = Members
		self.num_members = len(Members)

	def evaluate_members(self, num_games):
		g = TicTacToe_Game.TicTacToe()
		D = Driver(game=g)
		D.many_games(num_games, self.members)

	def print_members(self):
		for player in self.members:
			player.print_stats()

	def new_generation(self, num_offspring, dropout_rate = 0.1, rand_rate = 0.5, keep_perc = 0.25):
		self.members.sort(key=lambda x: x.Losses)
		member_size = len(self.members)
		self.members = self.members[:int(keep_perc*member_size)]

		win_sum = sum([x.Wins for x in self.members])
		if (win_sum == 0):
			win_dist=[1.0/len(self.members) for x in self.members]
		else:
			win_dist=[x.Wins/(1.0*win_sum) for x in self.members]
		offspring = []
		for i in range(member_size - len(self.members)):
			parent_one = np.random.choice(self.members, p=win_dist)
			parent_two = np.random.choice(self.members, p=win_dist)

			child = self.mate(parent_one, parent_two)

			offspring.append(child)
		self.members.extend(offspring)

		return self

	def mate(self, parent_one, parent_two):
		raise NotImplementedError

	def print_stats(self):
		sum_total = 0
		sum_wins = 0
		for i in self.members:
			sum_total += i.Wins + i.Losses
			sum_wins = i.Wins
		print("win perc: " + str(sum_wins/sum_total) + '\n')

	def print_best_members(self, num_members=1):
		s = sorted(self.members, key=lambda x: x.Losses)
		for i in range(num_members):
			print(i)
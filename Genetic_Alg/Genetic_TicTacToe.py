import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/..")

from Players import TicTacToe_Player as T
from Games import TicTacToe_Game as G
from Genetic_Base_Class import *
from Base_Classes import *


# class TicTacToe_Generation(Generation):
# 	def __init__(self, num_members=0, Members=[]):
# 		if len(Members)==0:
# 			for i in range(num_members):
# 				new_player = T.rand_TicTacToe_Player()
# 				Members.append(new_player)

# 		super().__init__(Members)

# 	def mate(self, parent_one, parent_two, rand_rate=0.5):
# 			W1 = parent_one.W.flatten()
# 			W2 = parent_two.W.flatten()
# 			cross_over_point_W = int(np.random.rand()*80)
# 			cross_over_point_B = int(np.random.rand()*8)
# 			child_W = np.concatenate((W1[:cross_over_point_W], W2[cross_over_point_W:]))
# 			child_W = child_W.reshape((9,9))
# 			child_B = np.concatenate((parent_one.B[:cross_over_point_B], parent_two.B[cross_over_point_B:]))

# 			if (np.random.rand() > 0.7):
# 				rand_W = np.random.rand(9,9)*rand_rate - (rand_rate/2.0)*np.ones((9,9))
# 				rand_B = np.random.rand(9)*rand_rate - (rand_rate/2.0)*np.ones(9)
# 				child_W += rand_W
# 				child_B += rand_B

# 			child = T.TicTacToe_Player(child_W, child_B)
# 			return child

# 	def perc_against_random(self, p, num_games):
# 		random = T.rand_TicTacToe_Player()
# 		g = G.TicTacToe()
# 		d = Driver(game=g)
# 		d.many_games(num_games, [p, random])
# 		return float(p.Wins)/num_games

# 	def print_stats(self, num_samples):
# 		avg_win_against_random = 0

# 		samples = np.random.choice(self.members, num_samples)
# 		for m in samples:
# 			avg_win_against_random += self.perc_against_random(m, 100)
# 		avg_win_against_random /= len(samples)

# 		print("win perc agains random: " + str(avg_win_against_random) + '\n')

class TicTacToe_Member(Member):
	def __init__(self, player, fitness_score=0, other_players = []):
		self.player = player
		self.other_players = other_players
		gene = list(player.W.flatten())
		gene.extend(list(player.B))
		super().__init__(gene, fitness_score)

	def evaluate(self):
		g = G.TicTacToe()
		d = Driver(game=g)
		prev_wins = self.player.Wins

		if len(self.other_players)==0:
			random = T.rand_TicTacToe_Player()
			d.many_games(100, [self.player, random])
			self.fitness_score = (self.player.Wins-prev_wins)/100.0
		else:
			for i in range(50):
				opp = np.random.choice(self.other_players)
				d.single_game(self.player, opp)
			for i in range(50):
				opp = np.random.choice(self.other_players)
				d.single_game(opp, self.player)
			self.fitness_score = (self.player.Wins-prev_wins)/100.0

	def new_member(self, gene):
		W = np.array(gene[:81])
		B = np.array(gene[81:])
		W = W.reshape((9,9))
		new_player = T.TicTacToe_Player(W,B)
		return TicTacToe_Member(new_player)

	@staticmethod
	def get_random_member(fitness_score=0):
		new_player = T.rand_TicTacToe_Player()
		return TicTacToe_Member(new_player, fitness_score)

	def print_member(self):
		print("W: " + str(self.player.W))
		print("B: " + str(self.player.B))


# G1 = TicTacToe_Generation(num_members=500)
# for i in range(100):
# 	G1.evaluate_members(500)
# 	G1 = G1.new_generation(500)
# 	if i%10==0:
# 		G1.print_stats(100)

def perc_vs_rand(members):
	win_perc = []
	g = G.TicTacToe()
	d = Driver(game=g)
	for m in members:
		random = T.rand_TicTacToe_Player()
		prev_wins = m.player.Wins
		d.many_games(100, [m.player, random])
		win_perc.append(m.player.Wins - prev_wins)
	print(np.mean(win_perc))

members = []
for i in range(200):
	members.append(TicTacToe_Member.get_random_member())

#for m in members:
#	m.other_players = [x.player for x in members]

perc_vs_rand(members)

Gen = Generation(members)
for i in range(1000):
	Gen.evaluate_members()
	Gen.print_stats()
	if i%25==0:
		perc_vs_rand(Gen.members)
	Gen = Gen.next_generation(200, mutation_rate=0.7, mutation_breadth=5)
#	for m in Gen.members:
#		m.other_players = [x.player for x in members]

perc_vs_rand(Gen.members)
Gen.members[0].print_member()

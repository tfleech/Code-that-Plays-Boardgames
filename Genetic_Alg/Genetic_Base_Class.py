import numpy as np
import sys, os
#sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/..")

#from Base_Classes import *
#from Games import TicTacToe_Game

class Member:
	def __init__(self, gene, fitness_score=0):
		self.gene = gene
		self.fitness_score = fitness_score

	def evaluate(self):
		'''
		Update the members fitness score.
		'''
		raise NotImplementedError

	def new_member(self, gene):
		'''
		return a new instance of the same member type
		'''
		raise NotImplementedError

class Generation:
	def __init__(self, Members):
		self.members = Members

	def evaluate_members(self):
		for m in self.members:
			m.evaluate()

	def next_generation(self, num_offspring, keep_perc = 0.25, mutation_rate = 0.5, mutation_breadth = 1.0):
		self.members.sort(key=lambda x: x.fitness_score, reverse=True)
		new_members = self.members[:int(keep_perc*len(self.members))]

		total_fitness = sum([x.fitness_score for x in self.members])
		if (total_fitness == 0):
			fitness_dist = [1.0/len(self.members) for x in self.members]
		else:
			fitness_dist = [float(x.fitness_score)/total_fitness for x in self.members]

		if len(new_members) < num_offspring:
			offspring = []
			for i in range(num_offspring - len(new_members)):
				parent_one = np.random.choice(self.members, p=fitness_dist, replace=False)
				parent_two = np.random.choice(self.members, p=fitness_dist, replace=False)

				cross_over_point = int(np.random.rand()*len(parent_one.gene))

				child_gene = np.concatenate((parent_one.gene[:cross_over_point], parent_two.gene[cross_over_point:]))

				if np.random.rand() < mutation_rate:
					mutation = (np.random.rand(len(child_gene)) - 0.5)*np.std(child_gene)*mutation_breadth
					child_gene = np.add(child_gene, mutation)

				offspring.append(self.members[0].new_member(child_gene))
			new_members.extend(offspring)

		new_generation = Generation(new_members[:num_offspring])
		return new_generation

	def print_stats(self):
		avg_fitness = sum([m.fitness_score/len(self.members) for m in self.members])
		print("The average fitness is: " + str(avg_fitness))


# class Generation:
# 	def __init__(self, Members):
# 		self.members = Members
# 		self.num_members = len(Members)

# 	def evaluate_members(self, num_games):
# 		g = TicTacToe_Game.TicTacToe()
# 		D = Driver(game=g)
# 		D.many_games(num_games, self.members)

# 	def print_members(self):
# 		for player in self.members:
# 			player.print_stats()

# 	def new_generation(self, num_offspring, dropout_rate = 0.1, rand_rate = 0.5, keep_perc = 0.25):
# 		self.members.sort(key=lambda x: x.Losses)
# 		member_size = len(self.members)
# 		self.members = self.members[:int(keep_perc*member_size)]

# 		win_sum = sum([x.Wins for x in self.members])
# 		if (win_sum == 0):
# 			win_dist=[1.0/len(self.members) for x in self.members]
# 		else:
# 			win_dist=[x.Wins/(1.0*win_sum) for x in self.members]
# 		offspring = []
# 		for i in range(member_size - len(self.members)):
# 			parent_one = np.random.choice(self.members, p=win_dist)
# 			parent_two = np.random.choice(self.members, p=win_dist)

# 			child = self.mate(parent_one, parent_two)

# 			offspring.append(child)
# 		self.members.extend(offspring)

# 		return self

# 	def mate(self, parent_one, parent_two):
# 		raise NotImplementedError

# 	def print_stats(self):
# 		sum_total = 0
# 		sum_wins = 0
# 		for i in self.members:
# 			sum_total += i.Wins + i.Losses
# 			sum_wins = i.Wins
# 		print("win perc: " + str(sum_wins/sum_total) + '\n')

# 	def print_best_members(self, num_members=1):
# 		s = sorted(self.members, key=lambda x: x.Losses)
# 		for i in range(num_members):
# 			print(i)
import numpy as np
from Genetic_Base_Class import *

class Lin_Reg_Member(Member):
	def __init__(self, W, B, points, labels, fitness_score=0):
		self.W = W
		self.B = B
		self.points = points
		self.labels = labels
		gene = list(W.flatten())
		gene.extend(list(B))
		super().__init__(gene, fitness_score)

	def evaluate(self):
		error = 0
		for i in range(len(self.points)):
			point = self.points[i]
			y = np.tanh(np.matmul(self.W,point) + self.B)
			error += float(y-self.labels[i])**2
		if error!=0:
			self.fitness_score = 1.0/error
		else:
			self.fitness_score = 9999

	def new_member(self, gene):
		W = np.array(gene[:2])
		B = np.array([gene[2]])
		return Lin_Reg_Member(W, B, self.points, self.labels)

	@staticmethod
	def get_random_member(points, labels, fitness_score=0):
		W = np.random.rand(1,2)
		B = np.random.rand(1)
		return Lin_Reg_Member(W, B, points, labels, fitness_score)


points = np.array([[1,2],[2,1]])
labels = np.array([1,-1])

members = []
for i in range(100):
	members.append(Lin_Reg_Member.get_random_member(points, labels))

G = Generation(members)
for i in range(30):
	G.evaluate_members()
	print(len(G.members))
	G.print_stats()
	G = G.next_generation(100)
#print(m.fitness_score)
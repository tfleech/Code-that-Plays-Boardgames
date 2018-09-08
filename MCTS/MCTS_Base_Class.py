import numpy as np

class Node():
	def __init__(self, parent, board, player, prev_move, is_leaf=True, visits=0, wins=0):
		self.board = board
		self.visits = visits
		self.wins = wins
		self.parent = parent
		self.children = []
		self.is_leaf = is_leaf
		self.player = player
		self.prev_move = prev_move


class MCTS():
	def __init__(self, board, player, time_limit=1000000):
		self.board = np.copy(board)
		self.time_limit = time_limit
		n = Node(None, self.board, player, None)
		self.root = n
	
	def select_node(self, root):
		if root.is_leaf:
			return root

		#TODO: replace with UCB
		i = np.random.randint(len(root.children))

		return self.select_node(root.children[i])

	def expand_node(self, node):

		if self.is_game_over(node.board)[0]:
			return node

		for m in self.get_next_states(node.board, node.player):
			new_board = self.make_move(node.board, node.player, m)
			new_player = self.next_player(node.player)
			prev_move = m
			new_node = Node(node, new_board, new_player, prev_move)
			node.children.append(new_node)

		i = np.random.randint(len(node.children))

		return node.children[i]

	def simulation(self, node):
		node.visits += 1

		current_board = node.board
		current_player = node.player

		winner = self.is_game_over(current_board)[1]
		while not self.is_game_over(current_board)[0]:
			poss_moves = self.get_next_states(current_board, current_player)
			m = np.random.choice(poss_moves)
			current_board = self.make_move(current_board, current_player, m)
			current_player = self.next_player(current_player)
			winner = self.is_game_over(current_board)[1]

		if winner==node.player:
			node.wins += 1
			return True
		return False

	def backpropagation(self, node, win):
		if node.parent == None:
			return

		node.parent.visits += 1
		if win:
			node.parent.wins += 1

		self.backpropagation(node.parent, win)


	def get_next_move(self):

		for i in range(10):
			node_to_expand = self.select_node(self.root)
			node_to_evaluate = self.expand_node(node_to_expand)
			node_win = self.simulation(node_to_evaluate)
			self.backpropagation(node_to_evaluate, node_win)

		max_visits = max(self.root.children, key=lambda n: n.visits)
		max_wins = max(self.root.children, key=lambda n: n.wins)

		return max_wins.prev_move


	def get_next_states(self, board, player):
		pass

	def make_move(self, board, move):
		pass

	def next_player(self, player):
		pass

	def is_game_over(self, board):
		pass
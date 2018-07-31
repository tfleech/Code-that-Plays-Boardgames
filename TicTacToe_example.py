from TicTacToe import *


#Init 2 random policy matrices
rand_W_1 = np.random.rand(9,9)*2 - np.ones((9,9))
rand_B_1 = np.random.rand(9)*2 - np.ones(9)
rand_W_2 = np.random.rand(9,9)*2 - np.ones((9,9))
rand_B_2 = np.random.rand(9)*2 - np.ones(9)

#Create 2 players and a game
p1 = TicTacToe_Player(rand_W, rand_B)
p2 = TicTacToe_Player(rand_W, rand_B)
g = TicTacToe()

#Instantiate a driver and run a game
D = Driver(p1, p2, game=g)
D.run_game(print_game=True)
from TicTacToe import *


#Init 2 random policy matrices
rand_W_1 = np.random.rand(9,9)*2 - np.ones((9,9))
rand_B_1 = np.random.rand(9)*2 - np.ones(9)
rand_W_2 = np.random.rand(9,9)*2 - np.ones((9,9))
rand_B_2 = np.random.rand(9)*2 - np.ones(9)

#Create 2 players and a game
p1 = TicTacToe_Player(rand_W_1, rand_B_1, name="Player1")
p2 = TicTacToe_Player(rand_W_2, rand_B_2, name="Player2")
g = TicTacToe()

#Instantiate a driver and run a game
D = Driver(game=g)
D.single_game(p1, p2, print_game=True)

#D.many_games(5, players=[p1, p2], print_results=True)
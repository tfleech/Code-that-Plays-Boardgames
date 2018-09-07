from Games import TicTacToe_Game
from Players import TicTacToe_Player as T
from Base_Classes import *
import numpy as np


#Init 2 random policy matrices
rand_W_1 = np.random.rand(9,9)*2 - np.ones((9,9))
rand_B_1 = np.random.rand(9)*2 - np.ones(9)
rand_W_2 = np.random.rand(9,9)*2 - np.ones((9,9))
rand_B_2 = np.random.rand(9)*2 - np.ones(9)

#Create 2 players and a game
p1 = T.TicTacToe_Player(rand_W_1, rand_B_1, name="Player1")
p2 = T.rand_TicTacToe_Player(name="Player2")
p3 = T.human_TicTacToe_Player(name="Player3")
p4 = T.minimax_TicTacToe_Player(name="Player4")
p5 = T.minimax_TicTacToe_Player(name="Player5")

g = TicTacToe_Game.TicTacToe()

#Instantiate a driver and run a game
D = Driver(game=g)
print(D.single_game(p4, p5, print_game=True))

#D.many_games(5, players=[p1, p2], print_results=True)

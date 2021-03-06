from Games import Connect4_Game
from Players import Connect4_Player as C
from Base_Classes import *

#Create two random players
p1 = C.rand_Connect4_Player(name="Player1")
p2 = C.rand_Connect4_Player(name="Player2")
p3 = C.human_Connect4_Player(name="Player3")
p4 = C.minimax_Connect4_Player(name="Player4")
p5 = C.minimax_Connect4_Player(name="Player5")


#Start a game
g = Connect4_Game.Connect4()

#Start the driver and play a game
D = Driver(game=g)
print(D.single_game(p4, p5, print_game=True))

#D.many_games(5, players=[p1, p2], print_results=True)
from Connect4 import *

#Create two random players
p1 = rand_Connect4_Player(name="Player1")
p2 = rand_Connect4_Player(name="Player2")

#Start a game
g = Connect4()

#Start the driver and play a game
D = Driver(game=g)
D.single_game(p1, p2, print_game=True)
print(g.winner)

#D.many_games(5, players=[p1, p2], print_results=True)
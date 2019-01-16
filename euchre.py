#THis python 2 program is meant to play a game of euchre, for reasons I can't understand

import random
from collections import Counter
from itertools import cycle
from round import *
from player import *
from misc import *

################################################################################

player1 = player('Liz')
player2 = player('Bingham')
player3 = player('Darcy')
player4 = player('Jane')
player1.toLeftOf = player4
player2.toLeftOf = player1
player3.toLeftOf = player2
player4.toLeftOf = player3
players = [player1, player2, player3, player4]
kitten = kitty()

player1.lead = True
player4.dealer = True

Team1Score = 0
Team2Score = 0

round1 = Round(players, kitten)
for i in range(10):
        round1.deal()

        print("Player's Hands:")
        for player in players:
                print(player.name)
                for card in player.hand:
		
                        print(card)
                print("\n")


        round1.determineTrump()
        round1.playRound()

if player1.points > player2.points:
        print(player1.name +" and "+ player3.name + " take the game")
elif player1.points < player2.points:
        print(player2.name +" and "+ player4.name + " take the game")
else:
        print("It's a fucking tie")

#for player in players:
#	for card in player.hand:
#		print("%s of %s" %(card.value, card.suit))
#	print("\n")

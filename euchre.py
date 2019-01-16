#THis python 2 program is meant to play a game of euchre, for reasons I can't understand

import random
from collections import Counter
from itertools import cycle
from round import *
from player import *
from misc import *

################################################################################

player1 = player('Liz', 'Jane')
player2 = player('Bingham', 'Liz')
player3 = player('Darcy', 'Bingham')
player4 = player('Jane', 'Darcy')
player1.toLeftOf = player4
player2.toLeftOf = player1
player3.toLeftOf = player2
player4.toLeftOf = player3
players = [player1, player2, player3, player4]
kitten = kitty()

player1.lead = True
player4.dealer = True

#while (score < 10):
round1 = Round(players, kitten)
round1.deal()

print("Player's Hands:")
for player in players:
	print(player.name)
	for card in player.hand:
		
		print(card)
	print("\n")


round1.determineTrump()
round1.playRound()

#for player in players:
#	for card in player.hand:
#		print("%s of %s" %(card.value, card.suit))
#	print("\n")

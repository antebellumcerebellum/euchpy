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
players = [player1, player2, player3, player4]
kitten = kitty()

player1.lead = True
player4.dealer = True

#while (score < 10):
round1 = round(players, kitten)
round1.deal()

print("Player's Hands:")
for player in players:
	print(player.name)
	for card in player.hand:
		
		print("%s of %s" %(card.value, card.suit))
	print("\n")


round1.determineTrump()
round1.playTrick()

#for player in players:
#	for card in player.hand:
#		print("%s of %s" %(card.value, card.suit))
#	print("\n")
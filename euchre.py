import random

class card:
	# A class to represent a single card
	
	def __init__(self, newSuit, newValue):
		self.suit = newSuit #Suit
		self.value = newValue #Value, 9-A
		self.trump = False

class player:
	# A class for the players
	
	def __init__(self):
		self.hand = []
		self.lead = False
	
	def callTrump(self, topOfKitty):
		pass
	
	def playCard(self, leadSuit, trump, cardsPlayed):
		pass

class kitty:
	def __init__(self):
		self.cards = []
		
	def getTop(self):
		return self.cards[0]
		
class round:
	
	def __init__(self, playerList, kitten):
		self.players = playerList
		self.kitty = kitten

	def deal(self, deck, kitty): # Function to deal cards to players
		random.seed
		random.shuffle(deck)
		
		for i, person in enumerate(self.players):
			person.hand = deck[0 + 4*i:5 + 4*i]
			kitty.cards = [deck[-1], deck[-2], deck[-3], deck[-4]]
		
		return
		
	def determineTrump(self):
		pass
	def playRound(playerList):
	
		for i, player in enumerate(playerList):
			if player.lead:
				leaderIndex = i

################################################################################

deck = []
for suit in ['clubs', 'spades', 'hearts', 'diamonds']:
	for value in ['9', '10', 'J', 'Q', 'K', 'A']:
		newCard = card(suit, value)
		deck.append(newCard)

player1 = player()
player2 = player()
player3 = player()
player4 = player()
players = [player1, player2, player3, player4]
kitten = kitty()

player1.lead = True

#while (score < 10):
round1 = round(players, kitten)
round1.deal(deck)

for player in players:
	for card in player.hand:
		print("%s of %s" %(card.value, card.suit))
	print("\n")
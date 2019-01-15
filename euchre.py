import random
from collections import Counter

class card:
	# A class to represent a single card
	
	def __init__(self, newSuit, newValue):
		self.suit = newSuit #Suit
		self.value = newValue #Value, 9-A
		self.trump = False
		if newValue == 11:
			if (newSuit == 'diamonds' or newSuit == 'hearts'):
				self.color = 'red'
			else:
				self.color = 'black'

class player:
	# A class for the players
	
	def __init__(self):
		self.hand = []
		self.lead = False
		self.dealer = False
		self.called = False
		self.desiredTrump = 'squares'
	
	def callTrump(self, topOfKitty, iter):
		suits = []
		for card in self.hand:
			suits.append(card.suit)
		sortedSuits = Counter(suits).most_common()
		
		if sortedSuits[0][1] > 3: #call Trump
			self.desiredTrump = sortedSuits[0][0]
			call = True
		else:
			self.desiredTrump = sortedSuits[0][0]
			call = False
		
		if self.desiredTrump == topOfKitty.suit:
			return True
		elif (iter == 2 and call is True):
			return True
		elif (iter ==2 and self.dealer):
			return True
		else:
			return False
			
	def lowestCard(self):
		lowestValue = self.hand[0].value
		lowest = self.hand[0]
		for i, card in enumerate(self.hand):
			if card.value < lowestValue and not card.trump:
				lowestValue = card.value
				lowest = card
				print("Lowest Card:")
				print("%d of %s" %(card.value, card.suit))
		return lowest
    
	def playCard(self, leadCard, cardsPlayed):
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
		
		self.deck = []
		for suit in ['clubs', 'spades', 'hearts', 'diamonds']:
			for value in [9, 10, 11, 12, 13, 14]: #11=J, 12=Q, 13=K, 14=A
				self.deck.append(card(suit, value))
		print(len(self.deck))
		for car in self.deck:
			print("%d of %s" %(car.value, car.suit))
		print("\n")

	def deal(self): # Function to deal cards to players
		random.seed()
		random.shuffle(self.deck)
		
		for i, person in enumerate(self.players):
			person.hand = self.deck[0 + 5*i:5 + 5*i]
			self.kitty.cards = [self.deck[-1], self.deck[-2], self.deck[-3], self.deck[-4]]
		
		print("Kitty cards: ")
		for card in self.kitty.cards:
			print("%s of %s" %(card.value, card.suit))
		print("\n")
		
		return
		
	def determineTrump(self):
		trumpCalled = False
		kittySwitch = False
		for player in self.players:
			if player.callTrump(self.kitty.getTop(), 1):
				self.trump = player.desiredTrump
				
				kittySwitch = True
				trumpCalled = True
				player.called = True
		
		if not trumpCalled:
			for player in self.players:
				if player.callTrump(self.kitty.getTop(), 2):
					self.trump = player.desiredTrump
					trumpCalled = True
					player.called = True
		
		for player in self.players:
			for card in player.hand:
				if card.suit == self.trump: 
					card.trump = True
		
		# do the kitty switching thing
		if kittySwitch:
			for player in self.players: 
				if player.dealer:
					player.hand.remove(player.lowestCard())
					player.hand.append(self.kitty.getTop())
					print("Modified hand")
					for car in player.hand:
						print("%d of %s" %(car.value, car.suit))
					print("\n")
		print(self.trump)
	
	def playRound(playerList):
	
		for i, player in enumerate(playerList):
			if player.lead:
				leaderIndex = i

################################################################################

player1 = player()
player2 = player()
player3 = player()
player4 = player()
players = [player1, player2, player3, player4]
kitten = kitty()

player1.lead = True
player4.dealer = True

#while (score < 10):
round1 = round(players, kitten)
round1.deal()

print("Player's Hands:")
for player in players:
	for card in player.hand:
		print("%s of %s" %(card.value, card.suit))
	print("\n")


round1.determineTrump()

#for player in players:
#	for card in player.hand:
#		print("%s of %s" %(card.value, card.suit))
#	print("\n")
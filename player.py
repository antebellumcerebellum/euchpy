from collections import Counter
from misc import *
class player:
	# A class for the players
	
	def __init__(self, name, nextTo):
		self.name = name
		self.hand = []
		self.lead = False
		self.dealer = False
		self.called = False
		self.toLeftOf = nextTo
		self.desiredTrump = 'squares'
	
	def callTrump(self, topOfKitty, iter):
		suits = []
		for card in self.hand:
			suits.append(card.suit)
		sortedSuits = Counter(suits).most_common()
		
		print(self.name)
		print(sortedSuits)
		print("\n")
		
		if sortedSuits[0][1] > 2: #call Trump
			self.desiredTrump = sortedSuits[0][0]
			call = True
		else:
			self.desiredTrump = sortedSuits[0][0]
			call = False
		
		if self.desiredTrump == topOfKitty.suit and call:
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
		return lowest
    
	def highestOffsuit(self):
		highestValue = self.hand[0].value
		highest = self.hand[0]
		for i, card in enumerate(self.hand):
			if card.value > highestValue and not card.trump:
				highestValue = card.value
				highest = card
		return highest
	
	def highestCard(self):
		highestValue = self.hand[0].value
		highest = self.hand[0]
		for i, card in enumerate(self.hand):
			if card.value > highestValue and card.trump:
				highestValue = card.value
				highest = card
				haveTrump = True
		if not haveTrump:
			highest = highestOffSuit
		return highest
	
	def playCard(self, leadCard, cardsPlayed):
		onSuit = leadCard.suit
		playable = []
		for card in self.hand:
			if card.suit == leadCard.suit:
				playable.append(card)
		if not playable:
			for card in self.hand:
				if card.trump:
					playable.append(card)
			if not playable:
				playable.append(self.lowestCard())
		
		if len(playable) > 1:
			trumper = card(0, 'squares')
			for card in cardsPlayed:
				if card.trump and card.value > trumper.value:
					trumper = card
			for card in playable:
				if card.trump:
					if card.value > trumper.value:
						return card
		else:
			return playable[0]

import random
from misc import *
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
					break
		
		print("We're playing %s" %self.trump)
		for player in self.players:
			if player.called: print("-%s\n" %player.name)
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
	
	def playTrick(playerList):
		pass
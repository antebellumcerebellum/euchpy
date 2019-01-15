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


class kitty:
	def __init__(self):
		self.cards = []
		
	def getTop(self):
		return self.cards[0]
		
		
def findLowest(cards):
	for card in cards:
		if not card.trump:
			lowest = card
			break
	if not lowest:
		allTrump = True
		lowest = cards[0]
	if not allTrump:
		for card in cards:
			if (card.value < lowest.value and not card.trump):
				lowest = card
	else:
		for card in cards:
			if (card.value < lowest.value):
				lowest = card
	return lowest
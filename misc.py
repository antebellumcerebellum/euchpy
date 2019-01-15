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
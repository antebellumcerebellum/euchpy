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


class bCard:
        #bCard for better card.
        #like card, but with more variables to work with
        def __init__(self, suit, rank):
                self.suit = suit #'c', 's', 'h', 'd'
                if suit == 'c' or suit == 's':
                        self.family = 'b'
                else:
                        self.family = 'r'
                self.rank = rank #9-14, 11-J, 12-Q, 13-K, 14-A
                self.trump = False

        #determines the score of the card
        #trump - suit of trump
        #trumpFamily - family of suit that trump belongs to
        #all cards should have this method run once the kitty card has been revealed.
        #should be rerun if everyone disses the kitty card.
        def score(self, trump, trumpFamily):
                self.score = self.rank
                if trump == self.suit:
                        self.trump = True
                        if 9>=self.rank<=10:
                                self.score+=6
                        else:
                                self.score+=7
                elif trumpFamily == self.family and self.rank == 11:
                        self.score+=6

        #to sort in player's hand, use hand.sort(key = lambda x: x.score, reverse=True)
                        

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

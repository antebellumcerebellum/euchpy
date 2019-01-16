rankNameDict = {'9':'9', '10':'10', '11':'Jack', '12':'Queen', '13':'King', '14':'Ace'}
suitNameDict = {'c':'clubs', 's':'spades', 'h':'hearts', 'd':'diamonds'}

class Card:
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
        def scoreIt(self, trump, trumpFamily):
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

        def __repr__(self):
                return rankNameDict[str(self.rank)]+" of "+suitNameDict[self.suit]

class kitty:
	def __init__(self):
		self.cards = []
		
	def getTop(self):
		return self.cards[0]

from collections import Counter
import misc
class player:
	# A class for the players
	
	def __init__(self, name, hand=[]):
		self.name = name
		self.hand = hand
		self.lead = False
		self.dealer = False
		self.called = False
		self.toLeftOf = 0
		self.desiredTrump = 'squares'
		self.score = 0
	
       #with bCard
        def callTrump(self, topOfKitty, iteration):
                self.sortHand()

                #if there are more than 2 trump (or 2nd trump jack) in hand, then call
                if len(list(filter(lambda x: x.score>14, self.hand))) > 2:
                        return True
                if iteration == 2 and self.dealer:
                        return True
                return False                       
       
        def sortHand(self):
                #to be run before each round, each time a card is added
                self.hand.sort(key = lambda x: x.score, reverse=True)

        def lowestCard(self):
                return hand[-1]

        def highestOffSuit(self):
                trumpless = list(filter(lambda x: not(x.trump), self.hand))
                return trumpless[0]

        def highestCard(self):
                return hand[0]

        def playCard(self, card):
                try:
                        self.hand.remove(card)
                except:
                        print("tried to remove card tht was not in hand")
                return card

        #I didn't feel like reading throughout the whole playCard method because I am
        #lazy, so here's a algorithm I didn't even write down first to heck if it made sense
        def turn(self, cardsPlayed, deck):#cardsPlayed is cards played for THIS trick only, deck is list of bCards remaining in deck
                self.sortHand()
                order = len(cardsPlayed)

                #if you are first to play, avoid trump but aim high.
                if order == 0:
                        try:
                                return self.playCard(self.highestOffSuit())
                        except: #if it's all trumps, oh well.
                                return self.playCard(self.hand[0])
                        
                
                sortedCardsPlayed = cardsPlayed[:]
                sortedCardsPlayed.sort(key = lambda x: x.score, reverse = True)

                while True:
                        #first, see if we can play anything
                        playable = list(filter(lambda x: x.suit == cardsPlayed[0].suit, self.hand))
                        #add the trumps
                        #(I forget if trumplet jacks count, so I'm putting them in anyway)
                        playable = playable + list(filter(lambda x: not(x in playable) and (x.score>14), self.hand))
                        #sort it for good measure
                        playable.sort(key = lambda x: x.score, reverse = True)
                        #is something can't be played, draw and try again
                        if len(playable) == 0:
                                if len(deck) == 0:
                                        print("Fuck, I forgot what happens in this case. Probs not important lol")
                                        break
                                self.hand.append(deck.pop())#remove card from deck, add it to hand
                                continue
                        if playable[0].score < sortedCardsPlayed[0].score:
                                #if the cards out so far are all too good, there's no point in wasting a good card. Play a bad card
                                return self.playCard(playable[-1])
                        if playable[0].score >= sortedCardsPlayed[0].score:
                                if order >= 2 and sortedCardsPlayed[0] == cardsPlayed[-2]:#if your partner is winning don't sabotage
                                        return self.playCard(playable[-1])
                                #else, it could be worth playing something higher.
                                #it could be worth playing higher, but the level of conservativeness you should play with should be weighted by how many more people have to take their turns, and how many cards you have that are high
                                neoPlayable = list(filter(lambda x: x.score >= sortedCardsPlayed[0].score, playable))
                                #numNeoPlay = len(neoPlayable)
                                #conservatism = 4 - order
                                #if numNeoPlay 
                                return self.playCard(neoPlayable[0])# eh, screw the math. Play defensively.

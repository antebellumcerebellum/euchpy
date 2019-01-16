import random
from misc import *
class Round:
	
	def __init__(self, playerList, kitten):
		self.players = playerList
		self.kitty = kitten
		
		self.deck = []
		for suit in ['c', 's', 'h', 'd']:
			for value in [9, 10, 11, 12, 13, 14]: #11=J, 12=Q, 13=K, 14=A
				self.deck.append(Card(suit, value))
		print(len(self.deck))
		for car in self.deck:
			print(car)
		print("\n")

	def deal(self): # Function to deal cards to players
		random.seed()
		random.shuffle(self.deck)
		
		for i, person in enumerate(self.players):
			person.hand = self.deck[0 + 5*i:5 + 5*i]
			self.kitty.cards = [self.deck[-1], self.deck[-2], self.deck[-3], self.deck[-4]]
		
		print("Kitty cards: ")
		for card in self.kitty.cards:
			print(card)
		print("\n")
		
		return
		
	def determineTrump(self):
                #go around and see if the card to trump is liked by someone
                #if so, we proceed to play the game.
                trumpPicked = False
                iteration = 1
                while True:
                        possiTrump = self.kitty.cards[iteration-1]
                        if iteration == 3:
                                break
                        for card in self.deck:
                                card.scoreIt(possiTrump.suit, possiTrump.family)
                        for player in self.players:
                                if player.callTrump(possiTrump, iteration):
                                        trumpPicked = True
                                        break
                        if trumpPicked:
                                break
                        print("iteration ",iteration," passed")
                        iteration += 1
                print("trump selected: "+str(possiTrump.suit))
                return possiTrump
                
	
	def playRound(self):
                leadPlayer = list(filter(lambda x: x.lead, self.players))
                leadPlayer = leadPlayer[0]


		count = 0
		firstPlayer = leadPlayer #current player
		secondPlayer = firstPlayer.toLeftOf
		thirdPlayer = secondPlayer.toLeftOf
		fourthPlayer = thirdPlayer.toLeftOf
		playedCards = []
		
		while firstPlayer.score+thirdPlayer.score != 3 and secondPlayer.score+fourthPlayer.score != 3:
                        playedCards = []
                        print(firstPlayer.name + " to start next round")
                        playedCards.append(firstPlayer.turn(playedCards, self.deck))
                        print(firstPlayer.name+" played "+str(playedCards[-1])+" ("+str(playedCards[-1].score)+")")
                        secondPlayer = firstPlayer.toLeftOf
                        playedCards.append(secondPlayer.turn(playedCards, self.deck))
                        print(secondPlayer.name+" played "+str(playedCards[-1])+" ("+str(playedCards[-1].score)+")")
                        thirdPlayer = secondPlayer.toLeftOf
                        playedCards.append(thirdPlayer.turn(playedCards, self.deck))
                        print(thirdPlayer.name+" played "+str(playedCards[-1])+" ("+str(playedCards[-1].score)+")")
                        fourthPlayer = thirdPlayer.toLeftOf
                        playedCards.append(fourthPlayer.turn(playedCards, self.deck))
                        print(fourthPlayer.name+" played "+str(playedCards[-1])+" ("+str(playedCards[-1].score)+")")

                        maxIndex = 0
                        for i, card in enumerate(playedCards):
                                if card.score > playedCards[maxIndex].score:
                                        maxIndex = i

                        print(playedCards[maxIndex],"wins!")
                        players = [firstPlayer, secondPlayer, thirdPlayer, fourthPlayer]
                        players[maxIndex].score += 1

                        firstPlayer = players[maxIndex]
                        

                if firstPlayer.score+thirdPlayer.score == 3:
                        print(firstPlayer.name + " and " + thirdPlayer.name + " win!" )
                else:
                        print(secondPlayer.name + " and " + fourthPlayer.name + " win." )

			


from arm_kinematics import *

#dictionary of card names to values
card_values = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9,
'ten':10, 'jack':10, 'queen':10, 'king':10, 'ace' = [1, 11]} 

class Player:
	#position, hand, offset, gameOver?
	def __init__(self, isDealer, position):
		self.hand = [] #keeps track of the player's hand
		self.isDealer = isDealer #if the player is a dealer
		self.gameOver = False #if the player has lost
		self.isBusted = False #if the player has busted
		self.blackjack = False #if the player has blackjack initially
		self.offset = 0 #measures how far over the cards need to be dealt each time
		self.position = position #position of where the player's are physically

#this will deal a card to player. it appends the card to the player's hand and then checks if they have busted
#this involves picking up a card, reading it, and placing it by the player
def deal(player, orientation = 'up', fromTable = False):
	player.offset += 1

	#DO KINEMATICS HERE <-------------
	#pick up card from physical deck
	#right arm hover over deck
	#right arm go down to pick up card
	#succ
	#right arm comes up with card
	#get cardValue from computer vision
	#right arm moves to present card to camera
	#place down at player + offset
	#flip card - right and left arms touch tips
	#left succ
	#right unsucc
	#right arm away
	#left arm moves to some destination and unsucc's
	cardValue = 0 #replace later with computer vision value
	player.hand.append(cardValue)
	checkBust(player)

def dealHand(player): #deals 
    if player.isDealer:
    	deal(player, 'down')
	else:
		deal(player)
	deal(player)	    

def total(player): #add up all cards in player's hand and return value
    total = 0
    aceCount = 0 	
    for card in player.hand:
    	if card != 'ace':
    		total += cardValues[card]
		else:
			aceCount += 1
	#run through twice
	totalLow = total
	totalHigh = total
	if aceCount >= 1:
		totalHigh += 11 + (aceCount - 1)
		totalLow += aceCount
	if totalHigh > 21:
		return totalLow
	else:
		return totalHigh

def checkBust(player):
	if total(player) > 21:
		player.isBusted = True
		player.gameOver = True

def blackJack(player):
	if ace in player.hand:
		if faceCard or 10 in player.hand:
			return True

def game():
	numPlayers = raw_input("Enter how many players are playing: ")
	dealer = Player(True)
	players = []
	for i in range(numPlayers):
		players.append(Player(False, i)) #add a new player to players array

	#setup board
	dealHand(dealer)
	for player in players:
		dealHand(player) 

	if blackJack(dealer): #CORNER CASE: if dealer has blackjack immediately
		#check if players have blackjack
	
	for player in players:
		if blackJack(player):
			player.blackJack = True
			player.gameOver = True
		while !player.gameOver #while the player hasnt either busted or quit
			choice = raw_input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower() #convert to computer vision
			if choice == "hit":
				deal(player)
			elif choice == "stay":
				player.gameOver = True

	#now all the player turns are over so we can deal for dealer
	#flip over face down card
	#right arm hover over face down card
	#right arm move down
	#right succ
	#right arm up
	#right left touch tips
	#swap succ
	#right arm away
	#left arm place card down
	deal(dealer, 'up', True)
	while total(dealer) < 17 and !dealer.isBusted:
		deal(dealer)

	#now dealer has been dealed we check win conditions on each player
	if dealer.isBusted:
		#everyone that has not busted wins
		for player in players:
			if !player.isBusted:
				#player wins
				print("Congratulations player " + str(player.position))
			else:
				#player loses
				print("You lost " + str(player.position))
	else:
		#everyone that has not busted and has a value greater than the dealer's wins 
		for player in players:
			if (!player.isBusted and total(player) > total(dealer)) or player.blackjack:
				#player wins
			else:
				#player loses

	
if __name__ == "__main__":
   game()
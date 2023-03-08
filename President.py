#22/01/2023#
import random
starting_hand = 5

class Card:
    def __init__(self,suit,num):
        self.suit = suit
        self.num = num
        
    def show(self):
        print("{} of {}".format(self.num,self.suit))

      
class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        for suit in ["Spades","Clubs","Diamonds","Hearts"]:
            for num in range(1,14):                
                if (num == 1):
                    self.cards.append(Card(suit,"Ace"))
                elif (num == 12):
                    self.cards.append(Card(suit,"Jack"))
                elif (num == 13):
                    self.cards.append(Card(suit,"Queen"))
                elif (num == 14):
                    self.cards.append(Card(suit,"King"))
                else:
                    self.cards.append(Card(suit,num))
                
    def show(self):
        for card in self.cards:
            card.show()
        print("\n")

    def shuffle(self):
        print("Shuffling Deck...")
        random.shuffle(self.cards)        
        print("Done!\n")
        
    def draw(self):
        return self.cards.pop()
    
    def discard(self,player):
        self.cards.insert(0,player.discard())


class Player:
    def __init__(self,name,ai):
        self.name = name
        self.hand = []
        self.ai = ai
        self.winner = False
        
    def draw(self,deck):
        self.hand.append(deck.draw())
        return self
    
    def show(self):
        print("{}'s hand:".format(self.name))
        for card in self.hand:
            card.show()
        print("\n")
        
    def play(self,card):
        return self.hand.pop(card)
        

class Pile:
    def __init__(self):
        self.cards = []
        
    def show(self):
        for card in self.cards:
            card.show()
            
    def place(self,player,card):
        newCard = player.play(card)
        print("{} has placed a {} of {}".format(player.name,newCard.num,newCard.suit))
        self.cards.insert(0,newCard)
        print("\n")

    def topCard(self):
        if (self.cards != []):
            (self.cards[0]).show()
            print("Showing Card: {} of {}".format((self.cards[0]).num,(self.cards[0]).suit))
        else:
            print("Discard pile is currently empty.")


def Turn(player):
    if not player.ai:
        #Print the top card of the discard pile
        pile.topCard()
        #Show the current player's hand
        player.show()
        #Get card player wants to play and place it on the discard pile
        card = int(input("Choose a card to play: "))
        pile.place(player,card)
        if player.hand == []:
            playing = False
            player.winner = True
            return
    else:
        '''
        run external code for AI?
        maybe turns should be processed in a seperate file that interacts with the main file
        seperate shell that asks for input that AI can interact with
        '''
def TurnEnum(num):
    match num:
        case 1:
            num = 2
        case 2:
            num = 3
        case 3:
            num = 4
        case 4:
            num = 1
    return num
    
#init deck
deck = Deck()
#init discard pile
global pile
pile = Pile()
#shuffle deck
deck.shuffle()
deck.show()
#get player names
names = ["Chris","Matt","Peter","Jodie"]
#init players
player1 = Player(names[0],False)
player2 = Player(names[1],False)
player3 = Player(names[2],False)
player4 = Player(names[3],False)
#draw player starting hands
for i in range(starting_hand):
    player1.draw(deck)
    player2.draw(deck)
    player3.draw(deck)
    player4.draw(deck)
#start game
playing = True
turn = 1
#Play through turns
while playing:
    match turn:
        case 1:
            Turn(player1)
        case 2:
            Turn(player2)
        case 3:
            Turn(player3)
        case 4:
            Turn(player4)
    turn = TurnEnum(turn)
        
#show hands, for debugging purposes
'''player1.show()
player2.show()
player3.show()
player4.show()'''

#
'''pile.place(player1)
pile.place(player2)
pile.place(player3)
pile.place(player4)'''
#pile.show()
#pile.topCard()

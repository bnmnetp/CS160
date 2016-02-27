import random
import collections

Card = collections.namedtuple('Card',['rank','suit'])

def card_str(self):
    return self.rank + " of " + self.suit

Card.__str__ = card_str

c = Card('A','spades')
print("c = ",c)
d = Card('J','Diamonds')
print(d)

def test_newcard():
    c = Card('A','spades')


class Deck:
    def __init__(self):
        self.cardList = []
        for rank in "23456789TJQKA":
            for suit in ['spades','clubs','diamonds','hearts']:
                newCard = Card(rank,suit)
                self.cardList.append(newCard)

        #self.cardList = [Card(r,s,0) for r in "23456789TJQKA" for s in "spade clubs diamonds hearts".split()]
    
    def shuffle(self):
        for i in range(100):
            pos1 = random.randrange(len(self.cardList))
            pos2 = random.randrange(len(self.cardList))
            temp = self.cardList[pos1]
            self.cardList[pos1] = self.cardList[pos2]
            self.cardList[pos2] = temp
            
    def draw(self):
        return self.cardList.pop()


class Player:
    def __init__(self,name):
        self.hand = []
        self.score = 0
        self.name = name

    def drawCard(self,deck):
        newCard = deck.draw()
        self.score = self.score + newCard.getValue()
        self.hand.append(newCard)
        
    def showHand(self):
        print("Cards for ", self.name)
        for c in self.hand:
            print(c)
        print("-----")

    def getValue(self):
        return self.score
        


# def blackjack():
#     d = Deck()
#     d.shuffle()
#     dealer = Player('dealer')
#     player1 = Player('player1')
#     for i in range(2):
#         dealer.drawCard(d)
#         player1.drawCard(d)
# 
#     done = False
#     while not done:
#         player1.showHand()
#         move = input("h for hit or s to stand")
#         if move == 'h':
#             player1.drawCard(d)
#             player1.showHand()
#             if player1.getValue() > 21:
#                 print('you bust')
#                 done = True
#         else:
#             done = True
#     
#     dealer.showHand()
#     while dealer.getValue() <= 16:
#         dealer.drawCard(d)
#         dealer.showHand()
#     
#     if player1.getValue() > 21:
#         print('player loses')
#     elif player1.getValue() > 21:
#         print('dealer busts')
#     elif dealer.getValue() <= 21 and dealer.getValue() > playerTot:
#         print('dealer wins')
#     else:
#         print('you win')
#     
# blackjack()
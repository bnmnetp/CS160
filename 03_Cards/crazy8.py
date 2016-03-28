#!/usr/bin/python
#  Card
#
#  Created by Brad Miller on 2005-02-10.
#  Copyright (c) 2005 Luther College. All rights reserved.
#

import sys
import os
import random


class Card:
    def __init__(self, suit, rank):
        self.__suit = suit
        self.__rank = rank

    def getSuit(self):
        return self.__suit

    def getRank(self):
        return self.__rank

    suit = property(getSuit)
    rank = property(getRank)

    def __str__(self):
        return self.rank + self.suit

    def __cmp__(self, other):
        suitRank = "hdcs"
        cardRank = "23456789tjqka"
        suitComp = suitRank.find(self.suit) - suitRank.find(other.suit)
        rankComp = cardRank.find(self.rank) - cardRank.find(other.rank)
        if suitComp != 0:
            return suitComp
        else:
            return rankComp

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __lt__(self, other):
        if self.__cmp__(other) < 0:
            return True
        return False

    def __gt__(self, other):
        if self.__cmp__(other) > 0:
            return True
        return False

class Hand:
    def __init__(self):
        self.myCards = []

    def size(self):
        return len(self.myCards)

    def add(self, newCard):
        self.myCards.append(newCard)
        self.myCards.sort()

    def remove(self, cardNo):
        return self.myCards.pop(cardNo)

    def __getitem__(self, cardNo):
        return self.myCards[cardNo]

    def __str__(self):
        return str(self.myCards)

    def __iter__(self):
        return iter(self.myCards)

    def numInSuit(self,suit):
        return len([c for c in self.myCards if c.suit == suit])

    def numInRank(self,rank):
        return len([c for c in self.myCards if c.rank == rank])

    def findRank(self,rank):
        return [i for i in range(len(self.myCards)) if self.myCards[i].rank == rank]

    def findSuit(self,suit):
        return [i for i in range(len(self.myCards)) if self.myCards[i].suit == suit]

    def cardAt(self,pos):
        return self.myCards[pos]

    def __str__(self):
        return str([str(x) for x in self.myCards])


class Deck:
    def __init__(self):
        self.myCards = []
        for i in ['h', 'd', 'c', 's']:
            for j in ['2', '3', '4', '5', '6', '7', '8', '9', 't', 'j', 'q', 'k', 'a']:
                self.myCards.append(Card(i, j))

    def draw(self):
        return self.myCards.pop()

    def shuffle(self):
        random.shuffle(self.myCards)

    def size(self):
        return len(self.myCards)

    def restock(self, discardPile):
        saveTop = discardPile.remove()
        self.myCards = self.myCards + discardPile.getAll()
        discardPile.clearPile()
        discardPile.add(saveTop)
        random.shuffle(self.myCards)


class Pile:
    def __init__(self):
        self.myCards = []
        self.crazySuit = ""

    def remove(self):
        if self.myCards:
            return self.myCards.pop()
        else:
            return None

    def add(self, tCard):
        self.myCards.append(tCard)

    def topRank(self):
        return self.myCards[-1].rank

    def topSuit(self):
        return self.myCards[-1].suit

    def getAll(self):
        return self.myCards[:]

    def lookAtTop(self):
        return self.myCards[-1]

    def clearPile(self):
        self.myCards = []

    def size(self):
        return len(self.myCards)

    def __str__(self):
        return str([str(x) for x in self.myCards])


class CrazyPile(Pile):

    def __init__(self):
        super().__init__()
        self.crazySuit = ""

    def add(self,newCard):
        if self.myCards:
            if self.isLegal(newCard):
                self.myCards.append(newCard)
            else:
                raise Exception("Illegal Play")
        else:
            self.myCards.append(newCard)


    def isLegal(self,newCard):
        if self.hasCrazySuit():
            return newCard.suit == self.getCrazySuit() or newCard.rank == '8'
        else:
            if newCard.suit == self.topSuit() or \
                            newCard.rank == self.topRank() or \
                            newCard.rank == '8':
                return True
            else:
                return False

    def hasCrazySuit(self):
        if self.crazySuit == "":
            return False
        else:
            return True

    def getCrazySuit(self):
        return self.crazySuit

    def setCrazySuit(self, s):
        self.crazySuit = s

    def clearCrazySuit(self):
        self.crazySuit = ""


class Player:
    def __init__(self, name):
        self.isDealer = False
        self.myHand = Hand()
        self.myName = name

    def findCardToPlay(self, currentPile):
        cix = input('enter number of card to play (-1 to draw): ')
        while cix < -1 or cix > self.myHand.size():
            print('Not a legal selection')
            cix = input('enter number of card to play (-1 to draw): ')
        return cix

    def printMyHand(self):
        n = 0
        for i in range(self.myHand.size()):
            print(n, self.myHand[i])
            n += 1

    def chooseCrazySuit(self):
        s = str(input("Name a suit (hcsd)"))
        while s not in "hcsd":
            print("suit must be one of h,c,s,d")
            s = str(input("Name a suit (hcsd)"))

    def playOneTurn(self, currentDeck, currentPile):
        self.printMyHand()
        cardIdx = self.findCardToPlay(currentPile)
        isLegal = False
        while cardIdx >= 0 and not isLegal:
            play = self.myHand.remove(cardIdx)
            if self.isLegalPlay(currentPile, play):
                currentPile.add(play)
                isLegal = True
            else:
                self.myHand.add(play)
                print("That is not a legal play.")
                self.printMyHand()
                cardIdx = self.findCardToPlay(currentPile)

        if cardIdx < 0:
            self.drawOneCard(currentDeck)
            return

        if play.rank == '8':
            crazySuit = self.chooseCrazySuit()
            currentPile.setCrazySuit(crazySuit)
        else:
            currentPile.clearCrazySuit()

        if self.myHand.size() > 0:
            return False
        else:
            return True

    def isLegalPlay(self, currentPile, play):
        if currentPile.hasCrazySuit():
            return play.suit == currentPile.getCrazySuit() or play.rank == '8'
        else:
            if play.suit == currentPile.lookAtTop().suit or \
                            play.rank == currentPile.lookAtTop().rank or \
                            play.rank == '8':
                return True
            else:
                return False

    def drawOneCard(self, theDeck):
        self.myHand.add(theDeck.draw())

    def getName(self):
        return self.myName


class Computer(Player):
    def findCardToPlay(self, currentPile):
        if currentPile.hasCrazySuit():
            playSuit = currentPile.getCrazySuit()
        else:
            playSuit = currentPile.lookAtTop().suit
        playRank = currentPile.lookAtTop().rank
        numCards = self.myHand.size()
        found = False
        c = 0
        while c < numCards and not found:
            if (playSuit == self.myHand[c].suit or
                        playRank == self.myHand[c].rank) and \
                            self.myHand[c].rank != '8':
                found = True
            c += 1

        # if not found check for an 8
        if not found:
            c = 0
            while c < numCards and not found:
                if (self.myHand[c].rank[0]) == '8':
                    found = True
                c += 1
        if found:
            return c - 1
        else:
            return -1

    def chooseCrazySuit(self):
        sd = {}
        for c in self.myHand.myCards:
            sd[c.suit] = sd.get(c.suit, 0) + 1

        best = 0
        suit = ''
        for k in sd:
            if sd[k] > best:
                best = sd[k]
                suit = k
        return suit


class BetterComputer(Computer):
    def findCardToPlay(self, currentPile):
        if currentPile.hasCrazySuit():
            playSuit = currentPile.getCrazySuit()
        else:
            playSuit = currentPile.lookAtTop().suit
        playRank = currentPile.lookAtTop().rank
        legalCards = []
        for c in self.myHand:
            if c.suit == playSuit:
                legalCards.append(c)
            elif c.rank == playRank:
                legalCards.append(c)

        sd = {}
        for c in legalCards:
            sd[c.suit] = sd.get(c.suit, 0) + 1

        best = 0
        suit = ''
        for k in sd:
            if sd[k] > best:
                best = sd[k]
                suit = k

        longSuit = [x for x in legalCards if x.suit == suit]
        longSuit2 = []
        if len(longSuit) > 1:
            longSuit2 = [x for x in longSuit if x.rank != 8]
        if len(longSuit2) > 0:
            idx = self.myHand.myCards.index(longSuit2[0])
        elif len(longSuit) > 0:
            idx = self.myHand.myCards.index(longSuit[0])
        else:
            idx = -1
        return idx


def playOneGame():
    theDeck = Deck()
    theDeck.shuffle()
    discardPile = CrazyPile()

    p1 = Computer('Computer')
    p2 = BetterComputer('Computer2')
    #    p2 = Player('Player')

    # Deal 7 cards to each player
    # TODO: try this with 3 or four players
    for i in range(7):
        p1.drawOneCard(theDeck)
        p2.drawOneCard(theDeck)
        print(p2.myHand)
        print(p1.myHand)

    discardPile.add(theDeck.draw())

    done = False
    players = [p2, p1]
    turn = 0
    plays = 0
    while not done:
        print(players[turn].myHand)
        print("top of deck = ", discardPile.lookAtTop())
        if theDeck.size() == 0:
            theDeck.restock(discardPile)
        done = players[turn].playOneTurn(theDeck, discardPile)
        plays += 1
        if done:
            print("Player ", players[turn].getName(), " Wins! after ", plays, " plays. ")
            return players[turn].getName()
        turn = (turn + 1) % 2


def main():
    scores = {'Computer': 0, 'Computer2': 0}
    for i in range(10000):
        winner = playOneGame()
        scores[winner] += 1
    print(scores)


if __name__ == '__main__':
    #    unittest.main()
    main()

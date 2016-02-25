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
        self.suit = suit
        self.rank = rank

    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank

    def getImageFile(self):
        return self.imFile

    def __str__(self):
        return self.rank + self.suit

    def __repr__(self):
        return 'Card(' + self.rank + ',' + self.suit + ')'

    def __cmp__(self, other):
        suitRank = "dhcs"
        cardRank = "23456789tjqka"
        suitComp = suitRank.find(self.suit) - suitRank.find(other.getSuit())
        rankComp = cardRank.find(self.rank) - cardRank.find(other.getRank())
        if suitComp != 0:
            return suitComp
        else:
            return rankComp

    def __eq__(self, other):
        return self.rank == other.getRank() and self.suit == other.getSuit()

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

    def getNumCards(self):
        return len(self.myCards)

    def addCard(self, newCard):
        self.myCards.append(newCard)
        self.myCards.sort()

    def removeCard(self, cardNo):
        return self.myCards.pop(cardNo)

    def __getitem__(self, cardNo):
        return self.myCards[cardNo]

    def __str__(self):
        return str(self.myCards)

    def __iter__(self):
        return iter(self.myCards)


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

    def getNumCards(self):
        return len(self.myCards)

    def restock(self, discardPile):
        saveTop = discardPile.getTop()
        self.myCards = self.myCards + discardPile.getAll()
        discardPile.clearPile()
        discardPile.putOnTop(saveTop)
        random.shuffle(self.myCards)


class Pile:
    def __init__(self):
        self.myCards = []
        self.crazySuit = ""

    def getTop(self):
        if self.myCards:
            return self.myCards.pop()
        else:
            return None

    def putOnTop(self, tCard):
        self.myCards.append(tCard)

    def getAll(self):
        return self.myCards[:]

    def lookAtTop(self):
        return self.myCards[-1]

    def clearPile(self):
        self.myCards = []

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
        while cix < -1 or cix > self.myHand.getNumCards():
            print('Not a legal selection')
            cix = input('enter number of card to play (-1 to draw): ')
        return cix

    def printMyHand(self):
        n = 0
        for i in range(self.myHand.getNumCards()):
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
            play = self.myHand.removeCard(cardIdx)
            if self.isLegalPlay(currentPile, play):
                currentPile.putOnTop(play)
                isLegal = True
            else:
                self.myHand.addCard(play)
                print("That is not a legal play.")
                self.printMyHand()
                cardIdx = self.findCardToPlay(currentPile)

        if cardIdx < 0:
            self.drawOneCard(currentDeck)
            return

        if play.getRank() == '8':
            crazySuit = self.chooseCrazySuit()
            currentPile.setCrazySuit(crazySuit)
        else:
            currentPile.clearCrazySuit()

        if self.myHand.getNumCards() > 0:
            return False
        else:
            return True

    def isLegalPlay(self, currentPile, play):
        if currentPile.hasCrazySuit():
            return play.getSuit() == currentPile.getCrazySuit() or play.getRank() == '8'
        else:
            if play.getSuit() == currentPile.lookAtTop().getSuit() or \
                            play.getRank() == currentPile.lookAtTop().getRank() or \
                            play.getRank() == '8':
                return True
            else:
                return False

    def drawOneCard(self, theDeck):
        self.myHand.addCard(theDeck.draw())

    def getName(self):
        return self.myName


class Computer(Player):
    def findCardToPlay(self, currentPile):
        if currentPile.hasCrazySuit():
            playSuit = currentPile.getCrazySuit()
        else:
            playSuit = currentPile.lookAtTop().getSuit()
        playRank = currentPile.lookAtTop().getRank()
        numCards = self.myHand.getNumCards()
        found = False
        c = 0
        while c < numCards and not found:
            if (playSuit == self.myHand[c].getSuit() or
                        playRank == self.myHand[c].getRank()) and \
                            self.myHand[c].getRank() != '8':
                found = True
            c += 1

        # if not found check for an 8
        if not found:
            c = 0
            while c < numCards and not found:
                if (self.myHand[c].getRank()[0]) == '8':
                    found = True
                c += 1
        if found:
            return c - 1
        else:
            return -1

    def chooseCrazySuit(self):
        sd = {}
        for c in self.myHand.myCards:
            sd[c.getSuit()] = sd.get(c.getSuit(), 0) + 1

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
            playSuit = currentPile.lookAtTop().getSuit()
        playRank = currentPile.lookAtTop().getRank()
        legalCards = []
        for c in self.myHand:
            if c.getSuit() == playSuit:
                legalCards.append(c)
            elif c.getRank() == playRank:
                legalCards.append(c)

        sd = {}
        for c in legalCards:
            sd[c.getSuit()] = sd.get(c.getSuit(), 0) + 1

        best = 0
        suit = ''
        for k in sd:
            if sd[k] > best:
                best = sd[k]
                suit = k

        longSuit = [x for x in legalCards if x.getSuit() == suit]
        longSuit2 = []
        if len(longSuit) > 1:
            longSuit2 = [x for x in longSuit if x.getRank() != 8]
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
    discardPile = Pile()

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

    discardPile.putOnTop(theDeck.draw())

    done = False
    players = [p2, p1]
    turn = 0
    plays = 0
    while not done:
        print(players[turn].myHand)
        print("top of deck = ", discardPile.lookAtTop())
        if theDeck.getNumCards() == 0:
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

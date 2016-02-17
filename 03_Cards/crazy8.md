# Crazy Eights - Part 1

We are aiming for a "smart" card playing program that can take on other card playing intelligent agents in a Crazy 8's tournament.  But we will get there one step at a time.  The first part of this program is to create and test the building blocks that could form the basis for any card playing game.  Those building blocks include:

* Card
* Deck
* Hand
* Pile

### Card

The Card class is quite simple.  It is just a Python object that has read only property for the `rank` and the `suit` of the card.  For example:

```
>>> myCard = Card('Ace','Spades')
>>> print(myCard.suit)
'Spades'
>>> print(myCard.rank)
'Ace'
>>> myCard.rank = '2'
Error!!
```

### Deck

The `Deck` class is a bit more complicated, but like the Cup for the dice its main function is to act as a container for the cards.  When a Deck is first created it should contain 52 cards 2 through Ace of each suit, Spades, Clubs, Diamonds, and Hearts.  A deck should also support the following methods:

* `shuffle()` This method should mix up the deck so that the cards are not in a predictable order.  Use Python's built in random module to help with this, do not use your own Rand class.
* `draw()` This method should take the top Card from the deck and return it, removing it from the Deck.
* `restock(cardlist)` This method should take a list of Cards and add them back into the Deck.  The restocked cards should come after any few cards that might be remaining in the original deck.
* `size()` returns an int with the number of cards left in the deck.

You will need to write a  Deck class including each of these methods using the API that I have described above.

When a deck is first created the cards should be in the following starting with the top card (first card drawn) on the deck:   2 of Hearts -- Ace of Hearts, 2 of Diamonds -- Ace of Diamonds,  2 of Clubs -- Ace of Clubs, 2 of Spades -- Ace of Spades

There are two other Card containers for you to write:  Pile and Hand

### Pile

The Pile class is used mainly for the discard pile, when first created a pile has no cards in it, but your program can add and remove cards from a pile as follows:

* `add(card)` -- add the card to the top of the pile
* `remove()` -- take the top card off of the pile and return the card
* `topRank()` -- return the rank of the card on the top of the pile without removing it from the pile
* `topSuit()` -- return the suit of the card on the top of the pile without removing it from the pile
* `__str__()` -- return the string representing the top card on the deck in the form of 'rank of suit'
* `size()` -- returns the number of cards in the pile.

### Hand

The Hand class is similar to Pile, but it should allow you to remove any card from the hand rather than just the card on the top of the pile.

* `add(card)` -- add the card to the hand
* `remove(position)` -- remove the card at position where position is an integer describing the index of the card in your hand.  Because most people do not start counting at zero, the index of the card should start with for the first card in your hand.
* `numInSuit(aSuit)` -- returns an integer representing the number of cards in the hand with the given suit.
* `numInRank(aRank)` -- returns an integer representing the number of cards in the hand with a given rank.
* `findCard(rank, suit)` -- returns the position (as an integer) of the card having rank and suit or -1 if the card is not found
* `findRank(rank)` -- returns a list of the  positions of the cards that have the given rank
* `findSuit(suit)` -- returns a list of the positions of the cards that have the given suit
* `cardAt(pos)` -- returns the card at the given position.
* `size()` -- returns the number of cards in your hand
* Bonus:  -- can you implement your Hand so that myHand[i] behaves just like myHand.cardAt(i)

Of course you may think, "I could just do all of this stuff with a list!"  But, the point of this part of the assignment is to think about abstractions.   Yes, we could do this with simple lists, but the abstractions that these classes provide will make it much easier for your program to work with, and make your end code much easier to read and understand.

### Due

These classes are due on Monday February 22 at 11:59PM.  You should try to have most of it done before class on Monday in case you have questions.  

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
* `removeAll()` -- method returns a list of all of the cards in the pile, and resets the Pile to be empty.

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

### example

The following is an example of how some of the methods of the differnt object interact.

```python
d = Deck()
myHand = Hand()
discardPile = Pile()
d.shuffle()

# deal
for i in range(7):
    c = d.draw()
    myHand.add(c)

# Play a card
c = myHand.remove(5)
discardPile.add(c)

# deck is empty, time to restock
if d.size() == 0:
    d.restock(discardPile.removeAll())

```

### Due Date for Part I

These classes are due on Monday February 22 at 11:59PM.  You should try to have most of it done before class on Monday in case you have questions.  

# Part II  A Special Pile (CrazyPile)

In this second part of the assignment we will create a CrazyPile class that is a subclass of the Pile class.  We need this class because we want the pile for crazy 8's to behave a little bit different than a generic pile.  Specifically it must handle the following requirements:

* When a card is put on the pile it must follow the rules of Crazy 8's. ([See here for Basic Rules](https://www.pagat.com/eights/crazy8s.html) )  If the card is not a legal play then the deck should cause the program to end by creating an error. You should modify the `add` method to enforce the rules so that an illegal card is not actually added to the top of the pile. Legal plays include:

   * Any card who's suit matches the suit on top of the pile
   * Any card who's rank matches the rank of the card on top of the pile
   * An 8
   * Any card who's suit matches the crazy_suit immediately after an 8 is played

* The pile must also handle the case of an 8 being played.  If an 8 is played on top of the pile no other card may be played until a crazy suit is named. using the method:  `setCrazySuit(suit_name)`  In order for a player to find out the crazy suit we also need a method called `getCrazySuit()`  The `getCrazySuit` method should return the suit set by the player who played the 8, or None if an 8 is not on top of the pile.

Once you have built your CrazyPile class then you should write a small program that demonstrates that it is working correctly.

* It must allow a legal play
* It must raise an exception for an illegal play
* It must allow a crazy suit to be set and enforce the legal play after a crazy suit is set, or raise an exception if an illegal play is made following a crazy suit.
* It must follow the rules for the play after a card has been played on an 8.

### Due Date for Part II

The CrazyPile is due Friday February 26.


# Part III  Players play the game

In this final part of the assignment you will write a ``Player`` class.  Your instance of a player class can play against a player class written by one of your classmates.  the player class must properly play the game of crazy 8's or you will be disqualified.

Your class must implement the following methods:  (it may also implement others, so make your code nicer, but these must be available to participate in the tournament)

* `drawOneCard(theDeck)`   -- Draw a card from theDeck and add it to the players hand.  Used for dealing the initial hand.
* `playOneTurn(theDeck, theDiscardPile)` -- This method is really the heart of the game.  It must make a legal play from the player's hand.  If the play results in the players hand being empty it should return True to indicate that it has finished the game.  Otherwise it should return false.
* `getName()` -- every player should have a name.  This simply returns a string representing the name of the player.  This is used for showing who won.
* `myHand` This should be a property of the Player to hold the Hand object.

Simple Testing

You can test your program initially by just having a single player try to play some turns.  For example

```python
theDeck = Deck()
theDeck.shuffle()
discardPile = CrazyPile()

p1 = Computer('Computer')


# Deal 7 cards to each player
for i in range(7):
    p1.drawOneCard(theDeck)
    print(p1.myHand)

discardPile.add(theDeck.draw())

# have the player try to play 5 turns against itself
for i in range(5):
     print(p1.myHand)  
     print("top of deck = %s of %s" % (discardPile.topRank(), discardPile.topSuit()))
     if theDeck.size() == 0:
            saveTop = theDiscardPile.remove()
            theDeck.restock(discardPile.removeAll())
            theDiscardPile.add(saveTop)
     done = p1.playOneTurn(theDeck, discardPile)
```

Once you have this working well, you can modify the for loop to a `while not done` loop and allow the player to play until the end.  If you add some judicious print statements to your player class, you can watch what the player does to make certain it is making legal/good plays, and that the hand and pile is being managed correctly.

It is also quite easy to make two players and modify the loop so that they alternate.

For extra credit you can make a player class that prompts you (a real person) for what card should be played.  Then you can play against the computer.

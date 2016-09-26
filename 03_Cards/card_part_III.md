So far you have implemented a Card class and a Deck class.

With two different classes this project is already starting to get a little large for an in-textbook project.  So we are going to move this to PyCharm or whatever your favorite IDE might be.

### Preparing the project

1. You can put your card class definition is card.py
2. You can put your deck definition in deck.py
3. You will also put the next two classes in their own files pile.py and hand.py

We will talk about unit testing in class, but here are the test cases I created for the Card class and the Deck class.

### Tests for Card

```
import unittest

class MyClass(unittest.TestCase):
    def test_constructor(self):
        c = Card('A', 'Spades')
        self.assertEqual(c.suit, 'Spades')
        self.assertEqual(c.rank, 'Ace')

        def foo(x):
            c.suit = 'Hearts'

        self.assertRaises(AttributeError, foo, 'Should raise an AttributeError')
        c = Card(2, 'Hearts')
        self.assertEqual(c.rank, '2')
        self.assertEqual(str(c), '2 of Hearts')
        c = Card(10, 'Spades')
        self.assertEqual(c.rank, '10')
        self.assertEqual(str(c), '10 of Spades', "Testing String Representation of Card(10,'Spades')")
        c = Card(14, 'Diamonds')
        self.assertEqual(str(c), 'Ace of Diamonds', "Testing String Representation of Card(14,'Diamonds')")
        c = Card(13, 'Clubs')
        self.assertEqual(c.rank, 'King', "Testing c.rank of Card(13, 'Clubs')")
        self.assertEqual(str(c), 'King of Clubs', "Testing String Representation of Card(13, 'Clubs')")

    def test_equality(self):
        c1 = Card(14, 'Spades')
        c2 = Card(14, 'Spades')
        self.assertEqual(c1, c2, "Ace of Spades == Ace of Spades")
        c3 = Card(13, 'Spades')
        self.assertNotEqual(c1, c3, "Ace of Spades != King of Spades")
        c3 = Card(7, 'Hearts')
        self.assertNotEqual(c1, c3, "Ace of Spades != 7 of Hearts")
        c4 = Card(14, 'Clubs')
        self.assertNotEqual(c1, c4, "Ace of Spades != Ace of Clubs")
        self.assertLess(c1, c4, "Ace of Spades < Ace of Clubs")
        self.assertLess(c3, c1, "7 of Hearts < Ace of Spades")
        cl = [Card(i, 'Hearts') for i in range(14,1,-1)]
        cl.sort()
        self.assertEqual(cl[0],Card(2,'Hearts'), "Testing a sorted list of cards")
        self.assertEqual(cl[-1],Card('A','Hearts'))


    def test_matches(self):
        c1 = Card(14, 'Spades')
        c2 = Card(14, 'Hearts')
        c3 = Card(13, 'Spades')
        self.assertTrue(c1.match_rank(c2), "Ace of Spades matches rank with Ace of Hearts")
        self.assertFalse(c1.match_rank(c3), "Ace of Spades does not match rank with King of Spades")
        self.assertTrue(c1.match_suit(c3), "Ace of Spades matches suit of King of Spades")
        self.assertFalse(c1.match_suit(c2), "Ace of Spades does not match suit of Ace of Hearts")

if __name__ == '__main__':
    unittest.main()
```

### Tests for Deck

```
import unittest
import random
random.seed(42)
class MyTest(unittest.TestCase):
    def test_basics(self):
        print("testing basic Deck construction")
        d = Deck()
        self.assertEqual(len(d),52,"len(d) should be 52")
        self.assertEqual(d.draw(),Card(2,'Spades'), "First card should be 2 of Spades")
        for i in range(12):
            d.draw()
        self.assertEqual(d.draw(),Card(2,'Clubs'), "After 12 more draws the next card should be 2 of Clubs")
        for i in range(12):
            d.draw()
        self.assertEqual(d.draw(),Card(2,'Diamonds'), "After 12 more draws the next card should be 2 of Diamonds")
        for i in range(12):
            d.draw()
        self.assertEqual(d.draw(),Card(2,'Hearts'), "After 12 more draws the next card should be 2 of Hearts")

    def test_iteration(self):
        print("Testing iteration over a deck should be in same order as drawing")
        d = Deck()
        r = 2
        suit = 'Spades'
        for card in d:
            self.assertEqual(card,Card(r,suit),"iteration test")
            r += 1
            if r > 14:
                break

    def test_shuffle(self):
        print("Testing shuffling")
        d = Deck()
        d.shuffle()
        self.assertEqual(d.draw(), Card(11, 'Spades'), "After shuffle")

if __name__ == '__main__':
    unittest.main()
```

Your first task is to get these tests to run outside of the textbook.  **NOTE**
In your deck.py file you can add from card import Card at the top to get your card class included.

For Wed

### Pile

The Pile class is used mainly for the discard pile, when first created a pile has no cards in it, but your program can add and remove cards from a pile as follows:

* `add(card)` -- add the card to the top of the pile
* `remove()` -- take the top card off of the pile and return the card
* `top_rank()` -- return the rank of the card on the top of the pile without removing it from the pile
* `top_suit()` -- return the suit of the card on the top of the pile without removing it from the pile
* `__str__()` -- return the string representing the top card on the deck in the form of 'rank of suit'
* `__len__` -- returns the number of cards in the pile.
* `remove_all()` -- method returns a list of all of the cards in the pile, and resets the Pile to be empty.

### Hand

The Hand class is similar to Pile, but it should allow you to remove any card from the hand rather than just the card on the top of the pile.

* `add(card)` -- add the card to the hand
* `remove(position)` -- remove the card at position where position is an integer describing the index of the card in your hand.
* `num_in_suit(aSuit)` -- returns an integer representing the number of cards in the hand with the given suit.
* `num_in_rank(aRank)` -- returns an integer representing the number of cards in the hand with a given rank.
* `find_card(rank, suit)` -- returns the position (as an integer) of the card having rank and suit or -1 if the card is not found
* `find_rank(rank)` -- returns a list of the  positions of the cards that have the given rank
* `find_suit(suit)` -- returns a list of the positions of the cards that have the given suit
* `__getitem__` -- returns the card at the given position using the index [] notation.
* `__len__` -- returns the number of cards in your hand


### Your assignment

You must work with a partner (or one group of 3). For this part.

1. By Wednesday you will write a set of unittests for either Hand or Pile
2. By Friday you will write the class definition for the class that your partner wrote the tests for.

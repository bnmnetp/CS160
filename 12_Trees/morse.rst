Encoding and Decoding a Message with Morse Code
===============================================

Beginning in 1836, the American artist Samuel F. B. Morse, the American physicist Joseph Henry, and Alfred Vail developed an electrical telegraph system. This system sent pulses of electric current along wires which controlled an electromagnet that was located at the receiving end of the telegraph system. A code was needed to transmit natural language using only these pulses, and the silence between them.  The pules, often called dots and dashes represent a *binary code*.  Rather than 1's and 0's we have .'s and -'s.


A binary tree makes a good partner to a binary code.   A left child of a node leads to a letter that has a dot as its next symbol, and a right child leads to a letter that has a dash as its next symbol.  The partial tree below shows the first three levels of the tree.

.. image:: morse.png

If you are decoding a message and have the string following sequence of dots dashes and spaces you can translate to more code by traversing the tree from the root downward for each letter.

::

  -- . .- -
  m  e a  t


You can use the same tree to encode a message by using a *recursive* tree search to find the node corresponding to the letter you want to encode.  If you keep track of the search path you will know the proper encoding for the letter.  For example the search path from the root to the node containing the letter n is right child, followed by left child, or -.

I will provide you with a file called ``morse.dat`` which contains the letters, numbers, and punctionation along with the morse code for each symbol.  You must build a binary tree for all of those symbols.  Do Not rename the file, that makes grading a pain.

Next you must write a decode function that accepts a string like the example above, and returns the text corresponding to the morse code.

Finally you must write an encode function that takes a string of letters and returns the morse code for those characters.


All of your code should be encapsulated inside a class called Morse.  I will have a test program that looks something like this::

    # test file
    from yourfile import Morse
    m = Morse('morse.dat')
    print(m.decode("... --- ..."))
    # Should print "sos"
    print(m.encode("meat"))
    # should print "-- . .- -"

As a reminder, any test code you include in your solution should be inside an if statement like this one::

  if __name__ == '__main__':
      # my test code here

This will prevent your own test code from running when I import your program for grading.

As usual, you should work on this in stages.

1.  Get your tree built properly.  You can use either the list of lists representation or the nodes and references representation and the corresponding code from the book.

2.  Then get the decode method working.  This one is easier than the encode method, and will be very easy to write if your tree is built correctly.

3.  Finally write the encode method.  Lots of things with trees can be done recursively so this is really good practice.

Due
---

Monday May 2nd by 11:59pm.

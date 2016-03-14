Problem Solving with Algorithms and Data Structures
===================================================


Setting up Your Environment
---------------------------

* Since we are in Olin 112 please bring  your laptops to class
* Make sure you register for cs160spring16 at http://interactivepython.org
* Download and install the latest `PyCharm <https://www.jetbrains.com/pycharm/download/>`_ on your computer

Weekly Goals
------------

* Week of February 7

  * A pythonic way of protecting data ``properties``
  * Write a new MSDie class which can represent more than numbers on each side.  *Hint:* The constructor should take a list of values as a parameter.
  * Add a Cup Class that can roll multiple dice.
  * Algorithms for Random Numbers

    * algorithm 1: middle-Square
    * algorithm 2: Multiplicative Linear Congruential Generators
    * algorithm 3: Fibbonacci

  * What makes for a good pseudorandom number generator?

* Week of February 14

  * Discussion and finishing up Random lab -- Hand in on Wednesday
  * Crazy 8's Project  -- Card, Deck, Hand, and Player classes
  * Introduce Algorithm Analysis ideas

* Week of February 20

  * Questions on part 1 of the crazy 8 assignment

    * Making attributes read only
    * See here for `visualization:  <http://www.pythontutor.com/visualize.html#code=import+random%0Aimport+collections%0A%0Arandom.seed(42%29%0A%0Aclass+MSDie%3A%0A++++def+__init__(self,+num_sides%29%3A%0A++++++++self.num_sides+%3D+num_sides%0A++++++++self.__value+%3D+random.randrange(num_sides%29+%2B+1%0A%0A++++def+getValue(self%29%3A%0A++++++++return+self.__value%0A%0A++++def+roll(self%29%3A%0A++++++++self.__value+%3D+random.randrange(self.num_sides%29+%2B+1%0A++++++++return+self.__value%0A%0A%0AmyDie+%3D+MSDie(6%29%0A%23print(myDie.__value%29%0Aprint(myDie.getValue(%29%29%0AmyDie.__value+%3D+9%0Aprint(myDie.__value%29%0A%23print(myDie.getValue(%29%29&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&textReferences=false&py=3&rawInputLstJSON=%5B%5D&curInstr=15>`_
    * A "Fancy" python trick for making simple read only classes

  * Finish up finding the longest sequence
  * Inheritance
  * Discuss and start part 2 of Crazy 8's
  * More on Big-O analysis  -- Read Chapter on Analysis

* Week of February 29

  * Anagram Detection Algorithms And Big-O
  * Stacks -- Read Stacks, Queues and Lists
  * Friday - Brad is at SIGCSE in Memphis
  * Be ready to try your Player classes Monday March 7


* Week of March 7

  * Introducing the Queue
  * Airplane boarding simulator
  * Crazy 8's Tournament?
  * Project 2:  Word Ladders  (Queues of Stacks!!?!)
  * Lists and their implementation

* Week of March 14

  * Finish linked list implementation
  * Compare our implementation with Python's implementation
  * Wednesday exam

    * Chapters 1 - 3
    * Classes - implementing a simple class
    * Big O notation and algorithm analysis
    * Queues
    * Stacks
    * Linked lists

In this assignment you are going to create word ladders.  The user will type in a beginning word, and an ending word. Your program must find the series of words that differ by only a single letter that lead from the beginning word to the ending word. For example, to turn the word STONE into WATER, one series of words is:

``` literal-block
STONE
SHONE
SHINE
SHINS
SHIES
SHYER
SAYER
HAYER
HATER
WATER
```

Word Ladder Algorithm
=====================

We will use an algorithm that employs both a Stack and a Queue. Here's how the algorithm works:

1.  Add the starting word to a set of used words -- Use Python's `set` instead of list for speed.

2.  Get the starting word and search through the source of new words to find all words that are one letter different, and have not already been used. For example suppose the current word is bend the word send and band would qualify because they all the letters are the same in 3 of the four places only one letter has changed. The word ends would not qualify even though it has three letters that are the same, but they are in different positions.

3.  Create stacks for each pair of words containing the starting word (pushed first) and the word that is one letter different (pushed on top).

4.  Add these new words to your set of used words so you don't use them again.

5.  Enqueue each of these stacks onto a queue. You now have created a queue of stacks!

5.  Now dequeue the first stack from the queue, look at its top word and compare it with the ending word. If they are equal you are done, and this stack represents the word ladder. Otherwise find all the unused words that are one letter different from the word on top of the stack. For each of these words:

    4.1 Make **a clone** of the current stack and push this word onto the clone.

    4.2 Add the new words to the set of used words

    4.3 enqueue this new stack

Make sure that you don't re-use any words or you will create an infinite loop.

We'll go through an example of this in class.

I will provide you with the dictionary you need for this assignment. The dictionary is simply a text file with 12,000 words. You will need to read in this file of words and organize it into three structures, one of three letter words, one of four letter words, and one of five letter words.

Requirements
============

-   Implement the Stack class just like it is in the book
-   Implement a Queue class just like in the book
-   Ask the user to enter a starting and ending word using input. -- if the word is finished you should stop. You can have them enter the words separately or on one line separated by a comma.
-   -   Verify that the start and end word are the same length and are 3, 4 or 5 characters long. If the words are not the correct length display an error message.  If the words are not in the word list display an error message.
    -   Compute the word ladder using the algorithm described above
    -   print out the word ladder with the starting word at the top and the ending word at the bottom.
    -   If no ladder is possible the appropriate message should be displayed.
    -   After one ladder is produced the user should be able to enter another pair of words.


Approach
========

I'm giving you all of this in one big writeup, but you NEED to have a strategy for this project in order to be successful.

1.  Write a function that reads the words.txt file and creates three sets of words.
2.  Write a function that takes a particular word, and the set of words that are the same length, and then returns all of the words that are the different by one letter.
3.  Implement the Stack and Queue classes as we have done in class, or follow the book.  Implement a clone method for your Stack class. It is really important to get the clone method right.  A correct clone method will create a brand new stack, with the same set of words pushed onto the new stack in the same order as the stack you are cloning.  Many people get this wrong by making a new stack but having using something like `newstack.items = self.items`  This statement makes the items of the newstack reference *the same* list as the current stack, which will means that if you push something on to newstack it will also be pushed onto the old stack as well.
4.  Implement the word ladder solution using all of the parts above.


Grading
=======

This assignment is worth 30 points, distributed as follows:

-   5 points for implementing the Queue and Stack classes with a good clone method.
-   5 points for creating sets of words of the right length
-   5 points for writing a function that returns all of the words that are different by one letter from the given word.
-   15 points for a working word ladder implementation

Extra Credit
============

-   Can you devise some heuristics to speed up the search? You will need to write up a good explanation for why your heuristics work.  Use the time.time() method to prove that they work. -- 5 points
-   Does this algorithm produce the shortest, longest, or unknown length ladders? Allow the user to choose whether they get the shortest or longest ladder. -- 5 points

Introduction
============

You have may seen the commercial
(http://www.youtube.com/watch?v=afJRKbBEr2Q) in which Kevin Bacon
attempts to cash a check without ID. In this commercial Bacon collects
an unlikely combination of people with increasingly tenuous
relationships that somehow wind up connecting him with the owner of the
store. So you see, he says, “we are practically related!” This idea
caught on in Hollywood and if you’ve acted in a movie, your Kevin Bacon
number is a reflection of how many links away from Kevin Bacon you are.
One actor is linked to another if they have acted in the same movie. For
example, Simon Helberg of the Big Bang theory acted with Gillian Jacobs
in *Let it Go*, in 2011. Gillian Jacobs acted with John malkovich in
*Gardens of the Night* in 2008. John Malkovich acted with Kevin Bacon in
*Queens Logic* in 1991.

Your job is to write a program that allows the user to enter the name of
an actor and then determines the Kevin Bacon number for that actor. The
program should print out the Kevin Bacon number for the actor and both
the list of actors that form the chain and the movies they acted in
together.

There is one data file for this assignment: movie\_actors.csv. The
format of the file looks like this:

[b]0.33

::

          Apokommata (2010)|Leonardo Sfontouris
          Apokommata (2010)|Dimitra Kokkori
          Apokommata (2010)|Marianna Pouloutiadou
          Apokommata (2010)|Dimitra Kokkori
          Apokommata (2010)|Anna Etiaridou
          Apokrif: Muzyka dlya Petra i Pavla (2005)|Anton Mlodik
          Apollo 13 (1995)|Bill Paxton
          Apollo 13 (1995)|Gary Sinise
          Apollo 13 (1995)|Ed Harris
          Apollo 13 (1995)|Tom Hanks
          Apollo 13 (1995)|Kevin Bacon


There are three main problems to solve for this assignment:

#. Build a graph that represents the links between all the actors. To
   build the graph you should use the Graph and Vertex classes found in
   the pythonds package. These classes are implemented just like the
   code in the textbook. This is the most challenging part of the
   assignment. You should start with a small part of the movies\_actors
   file OR create your own test file. You DO NOT want to start with the
   full movie\_actors.csv file as it contains more than 600,000 lines.
   With your test file use the Python environment to poke around at the
   graph and make sure that the links are correct. You will also need to
   devise a way to keep track of the movie that each actor has in common
   with her neighbors.  Here's an example graph you might convert into a file and use for testing.

   .. image:: easy.png

#. Use the Breadth First Search algorithm to create the links from all
   actors back to Kevin Bacon.

#. Write a loop that allows the user to enter a name and see the Kevin
   Bacon number plus links. You will need to implement the traverse
   function as described in the book to work backward from the actor
   entered to Kevin Bacon.

Here is an example of the Kevin Bacon program in action. Your program
should produce output that is similar.

::

        host-17-15-55:python> python kevinbacon.py
        What Actor would you like to trace? (exit to quit) Johnny Galecki
        The Kevin Bacon Number for  Johnny Galecki  is  3
        Johnny Galecki acted with Rachael Leigh Cook in Bookies (2003)
        Rachael Leigh Cook acted with Luke Wilson in Blonde Ambition (2007)
        Luke Wilson acted with Kevin Bacon in My Dog Skip (2000)

        What Actor would you like to trace? (exit to quit)

Grading
=======

This program is due Friday May 13 at 5:00pm.

There are 30 points to this assignment:

-  15 points for correctly building and searching the graph

-  10 points for traversing the searched graph

-  5 points for good programming practice and style

Measuring Randomness
====================


In class we came up with a nice list of properties that a good random number generator should have, and you implemented a ``Rand`` object for today that takes a seed, and generates a sequence of random numbers starting with that seed.

In class today I want you to implement some code that measures the quality of this first random number generator.  After you have written some measurement functions and captured some data about this first object, you implement a second random number generator and do the same measurements for comparison.

Part 1
------

Extending the Rand object with randrange.  Add a randrange method to your class.  This method should take two parameters, a starting and ending point.  It should return a random number in the range, including start, but excluding end.   Hint:  The modulo operator ``%`` will be pretty useful here.


Part 2
------

Implement the following measures and use them to gather data for the middle-squares method

1.  What is the 'period' of the random number generator?  That is, how long until the sequence starts to repeat itself?  Measure this for the following initial seeds, and use the next() method to generate the numbers.

  1.  2500
  2.  3792
  3.  991027
  4.  105557
  5.  A number of your choosing

2.  What is the distribution of the numbers in a particular range, over a very large number of random numbers.  Using the randrange method of your class, generate 1 million random numbers.  Keep track of how many times each number in the range is chosen.  try the following ranges:

  1.  1 -- 6
  2.  1 -- 100
  3.  Choose your own range.

3.  Do repeating sequences occur within a particular range of random numbers?  Again using the randrange function we want to search for a repeating sequence.  You may want to think for a minute why this is a different problem that number 1.  Searching for a repeated sequence is a pretty interesting problem all by itself.  You may want to think about the problem in two parts:

  1.  Suppose the you are searching for a repeating sequence and are assuming that it starts at the beginning of a list.
  2.  Generalize part 1 by trying out many (all possible?) starting points.  That is if you don't find a repeating sequence that starts at position 0 of the original list, may you can find one that starts at position 1 and so on.



Part 3
------

Implement a different method for generating the sequence of random numbers, and repeat the tests in Part 2  for this new object.


1.  Multiplicative Linear Congruential Generator -- What a mouthful

```
newseed = ( a * oldseed + c) % m
```

Some interesting values to try are
::

    a = 23, m = 100000001 c = 0
    a = 65539 m = 2**29 c = 0
    a = 69069 m = 2**32  c = 0

You should also try some non-zero values for c


2.  Blum Blum Shub

```
newseed = (oldseed*oldseed) % M
```

Where M is the product of p and q which are two primes that are congruent to 3 (mod 4).  For example, p = 11 and q = 19


3.  Fibonacci Sequence

The Fibonacci sequence is a well known sequence.  You may have programmed this in CS150 already.  If you recall that the first two numbers in the sequence are 1 and 1 then you get the sequence:

```
1 1 2 3 5 8 13 21 34
```

The expression for generating the next number is:

```
newnumber = (lastnumber + second_to_last)
return newnumber % M
```

In this case M is usually chosen to be 2**32 or 2**64 to keep the numbers from exploding.  In addition the seed provided to the Fibonacci random number generator constructor should be considered to be the nth Fibonacci number.


4.  Xorshift  -- https://en.wikipedia.org/wiki/Xorshift  -- This one is slightly more challenging in that it requires some bit-twiddling so I'll leave it to the more adventurous to read the description and give it a try.

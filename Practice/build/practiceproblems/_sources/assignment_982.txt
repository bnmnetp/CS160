practice2
=========

**Points**: 15

**Due**: 2016-09-05 20:38:00

More practice with lists and dictionaries

.. activecode:: maxoflist

   Write a function `max_of_list` that takes a list of numbers as a parameter and returns the biggest number in the list.  Your function may not use the builtin `max` function.  For example `maxoflist([1,3,9,4,2,8])` should return the number 9
   ~~~~
   def max_of_list(mylist):
      pass
   ====
   from unittest.gui import TestCaseGui

   class MyTest(TestCaseGui):

      def test_cases(self):
         self.assertEqual(max_of_list([1,2,3]), 3, "max_of_list([1,2,3])")
         self.assertEqual(max_of_list([3,2,1]), 3, "max_of_list([3,2,1])")
         self.assertEqual(max_of_list([1,3,2]), 3, "max_of_list([1,3,2])")
         self.assertEqual(max_of_list([3,3,3]), 3, "max_of_list([3,3,3])")
         self.assertEqual(max_of_list([3,3,3]), 3, "max_of_list([3,1,3])")
         self.assertEqual(max_of_list(range(99)), 98, "max_of_list(range(99)")
         self.assertEqual(max_of_list(range(-999,0,1)), -1, "list is [-999...-1]")

   MyTest().main()


.. activecode:: charcount_practice

   Write a function `letter_count(mystring)` that takes a string as a parameter and returns a dictionary where the keys of the dictionary are letters and the values are the number of times the letter appears in the string.
   ~~~~
   def letter_count(mystring):
      pass
   ====
   from unittest.gui import TestCaseGui

   class MyTest(TestCaseGui):
      def test_cases(self):
         self.assertEqual(letter_count("aaa")['a'], 3)
         self.assertEqual(letter_count("") ,{})
         self.assertEqual(letter_count("abc")['a'], 1, feedback="input was abc")
         self.assertEqual(letter_count("abc")['b'], 1, feedback="input was abc")         
         self.assertEqual(letter_count("abc")['c'], 1, feedback="input was abc")

   MyTest().main()



.. activecode:: pangrams_practice

   A pangram is a sentence that contains all the letters of the English    alphabet at least once, for example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it is a pangram or not.
   ~~~~
   def is_pangram(sentence):
       pass
   ====
   from unittest.gui import TestCaseGui

   class MyTest(TestCaseGui):

       def test_pg(self):
           self.assertTrue(is_pangram("the quick brown fox jumped over the lazy dog"),"the quick brown fox jumped over the lazy dog")
           self.assertTrue(is_pangram("abcdefghijklmnopqrstuvwxyz"),"abcdefghijklmnopqrstuvwxyz")
           self.assertFalse(is_pangram("abcdefghijklmmopqrstuvwxyz"))
           self.assertFalse(is_pangram(""))
           self.assertTrue(is_pangram("How vexingly quick daft zebras jump!"),"How vexingly quick daft zebras jump!")
           self.assertTrue(is_pangram("The five boxing wizards jump quickly." ),"The five boxing wizards jump quickly.")

   MyTest().main()

=====================
This Is A New Project
=====================

.. Here is were you specify the content and order of your new book.

.. Each section heading (e.g. "SECTION 1: A Random Section") will be
   a heading in the table of contents. Source files that should be
   generated and included in that section should be placed on individual
   lines, with one line separating the first source filename and the
   :maxdepth: line.

.. Sources can also be included from subfolders of this directory.
   (e.g. "DataStructures/queues.rst").

SECTION 1: Introduction
:::::::::::::::::::::::

Congratulations!   If you can see this file you have probably successfully run the ``runestone init`` command.  If you are looking at this as a source file you should now run ``runestone build``  to generate html files.   Once you have run the build command you can run ``runestone serve`` and then view this in your browser at ``http://localhost:8000``

This is just a sample of what you can do.  The index.rst file is the table of contents for your entire project.  You can put all of your writing in the index, or  you can include additional rst files.  Those files may even be in subdirectories that you can reference using a relative path.
   
::


ActiveCode
----------

.. activecode:: codeexample1
   :nocodelens:
   :caption: Min of 3

   Write a function `minOfThree` that takes 3 numbers as a parameter and returns the smallest of those numbers.  You may not use the built-in min function of Python in your solution.  You can work on this until you get all of the test cases to pass.
   ~~~~
   def minOfThree(a, b, c):
       pass

   ====
   from unittest.gui import TestCaseGui

   class MyTest(TestCaseGui):

       def test_mins(self):
           self.assertEqual(minOfThree(1,2,3), 1)
           self.assertEqual(minOfThree(3,2,1), 1)
           self.assertEqual(minOfThree(3,1,2), 1)
           self.assertEqual(minOfThree(0,0,0), 0)
           self.assertEqual(minOfThree(99,99,0), 0)
           self.assertEqual(minOfThree(-1,99,99),-1)
           self.assertEqual(minOfThree(-99,-99,-99),-99)
           self.assertNotIn('min(', self.getEditorText(),"You may not call min()")
           self.assertNotIn('min (', self.getEditorText(),"You may not call min()")

   MyTest().main()

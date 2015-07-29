# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 21:28:24 2015

@author: NStornetta
"""

"""Problem 24 from Project Euler reads as follows:
A permutation is an ordered arrangement of objects. For example, 3124 is one 
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations 
are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 
5, 6, 7, 8 and 9?"""

""" Answer:  To begin, the first set of permutations lexicographically will all
have zero in the starting position.  There are 9 permute 9 permutations
with zero in the starting position. That's 362,880 permutations. Similarly,
there are 362,880 permutations beginning with 1. From this point, in order
to reach the 1,000,000th permutation, we need to find the 274,240th
permutation with 2 in the starting position.
There are 8 permute 8 permutations with 2 in the starting position and 0 in
the second position. That's 40,320 more permutations. Furthermore, there are
40,320 permutations with 1 in the second position, 40,320 permutations with
3 in the second position, 40,320 permutations with 4 in the second position,
40,320 permutations with 5 in the second position, etc.
Performing integer division and modulo division shows that we need to find
the 32,320th permutation with 7 in the second position. We continue our search
process as before, finding that there are 5,040 permutations with 2 in the
first position and 7 in the second position.  Performing the same division
process as previous, we find that we need the 2,080th permutation with 8 in the
third position.
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:43:26 2015

@author: NStornetta
"""

"""Project Euler Problem 23.  Problem reads as follows:
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""

#Because (9^5)*6 = 354,294, this is the highest possible value that can be
#written as a sum of fifth powers. Higher than that, and there will not be
#enough digits to make it possible to sum up to the value.
import time

t = time.time()
total_sum = 0

for x in range(2,354295):
    digits_to_fifth_sum = 0    
    string_x = str(x)
    for digit in string_x:
        digits_to_fifth_sum += int(digit)**5
    else:
        if digits_to_fifth_sum == int(x):
            total_sum += digits_to_fifth_sum

print(digits_to_fifth_sum)
print("Answer found in " + str(round(time.time()-t,2)) + " seconds")
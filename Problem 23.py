# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 17:19:57 2015

@author: NStornetta
"""

"""Project Euler Problem 23.  Problem reads as follows:

A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.A 
number n is called deficient if the sum of its proper divisors is less than n 
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. By 
mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. However, this upper limit 
cannot be reduced any further by analysis even though it is known that the 
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum 
of two abundant numbers."""

import math
import time

#Create a loop to find all of the abundant numbers less than 28123 and then
#populate a list with all of those abundant numbers.
abundant_number_list = []

def find_all_divisors(number):
    divisor_list = [1]
    for y in range (2, int(math.sqrt(number)+1)):        
        if number % y == 0:
            divisor_list.append(y)
            if y != math.sqrt(number):
                divisor_list.append(number/y)
    return divisor_list

def abundant_number_finder(maximum_number):
    for x in range(12, maximum_number+1):
        divisor_list = find_all_divisors(x)
        if sum(divisor_list) > x:
            abundant_number_list.append(x)

def main():
    start_time = time.time()
    abundant_number_finder(28123)
    not_two_abundants_sum = 0
    for potential_sum in range(1, 28124):
        for abundant_num in abundant_number_list:
            if (potential_sum-abundant_num) in abundant_number_list:
                break
            else:
                pass
        else:
            not_two_abundants_sum += potential_sum
    else:
        print(not_two_abundants_sum, "returned in " + str(time.time()-start_time) + " seconds")

main()
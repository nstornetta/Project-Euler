# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:38:54 2015

@author: NStornetta
"""

"""Project Euler Problem 23.  Problem reads as follows:

Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

22=4, 23=8, 24=16, 25=32
32=9, 33=27, 34=81, 35=243
42=16, 43=64, 44=256, 45=1024
52=25, 53=125, 54=625, 55=3125
If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?"""

#Use a set of two for loops to find set of values.  Add values to list in order
#to verify uniqueness.

value_list = []

for a in range(2,101):
    for b in range(2,101):
        value = a**b
        if value not in value_list:
            value_list.append(value)

print(len(value_list))
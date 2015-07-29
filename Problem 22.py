# -*- coding: utf-8 -*-

"""Code to solve problem #22 of Project Euler.  Problem reads as follows:

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
from string import ascii_letters
import os
import pprint

os.chdir(r'\\crsffs1\users\nstornetta')

##Open names file and create a list of the individual names. Remove extra quotation marks.  Sort the list.
names = open("names.txt", "r")
names_list = names.read().split(',')
names.close()

for counter, name in enumerate(names_list):
    names_list[counter] = names_list[counter].replace('"', "")

names_list.sort()

##Assign numeric values to each of the letters in the alphabet
uppercase_letters = ascii_letters[26::]

letter_number_values = {}
for value, letter in enumerate(uppercase_letters):
    letter_number_values[letter] = value+1

##Calculate name scores for the entire list of names in the text file
running_total = 0

for name in names_list:
    name_running_total = 0    
    for letter in name:
        name_running_total += letter_number_values[letter]
    
    running_total += (name_running_total*(names_list.index(name)+1))

pprint.pprint(running_total)
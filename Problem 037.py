# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 19:12:25 2015

@author: NStornetta
"""

"""Project Euler Problem 37 reads as follows:  
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes."""

def isPrime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    for x in range(2,int(number**0.5)+1):
        if number % x == 0:
            return False
    else:
        return True

#This is admittedly a little clunkier than it could be; these two functions
#could almost certainly be combined into a single function, but I'm struggling
#to think of a way to do it that's more elegant than with a simple if-statement.
#I will update this later to optimize for elegance, but performance-wise the code
#runs very well.

def isPrimelr(number):
    primes_sum = 0
    number_string = str(number)
    for counter in range(len(number_string)):
        trunc_string_lr = number_string[:len(number_string)-counter]
        if not isPrime(int(trunc_string_lr)):
            break
        else:
            primes_sum += 1
            if primes_sum == len(number_string):
                return True
    else:
        return False
    
def isPrimerl(number):
    primes_sum = 0    
    number_string = str(number)
    for counter in range(len(number_string)):
        trunc_string_lr = number_string[len(string_int)-(counter+1):]
        if not isPrime(int(trunc_string_lr)):
            break
        else:
            primes_sum += 1
            if primes_sum == len(number_string):
                return True
    else:
        return False

current_integer = 10
truncated_primes_list = []

while len(truncated_primes_list) < 11 and current_integer <= 1000000:
    string_int = str(current_integer)    
    for y in range(len(string_int)):
        if not (isPrimelr(current_integer) and isPrimerl(current_integer)):
            break
    else:
        truncated_primes_list.append(current_integer)
    current_integer += 1

print(sum(truncated_primes_list)) #Returns 748,317

print(truncated_primes_list)
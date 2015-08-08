"""
Created on Tue Aug  4 18:39:32 2015
@author: NStornetta
"""

"""Project Euler Problem 31 reads as follows:

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?"""
import time

start = time.time()

coin_list = [1, 2, 5, 10, 20, 50, 100, 200]

def count(n, m):
    if n == 0:
        return 1
    elif n < 0 or m < 0:
        return 0
    return count(n, m-1)+count(n-coin_list[m], m)


print(count(200,len(coin_list)-1))
print("Answered in " + str(time.time()-start) + " seconds")
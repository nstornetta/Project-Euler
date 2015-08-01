# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 21:03:15 2015

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

num_combinations = 0

for x in range(200,-1,-1):
    for y in range(100,-1,-1):
#        if x*1 + y*2 > 200:
#            break
        for z in range(40,-1,-1):
#            if x*1 + y*2 + z*5 > 200:
#                break
            for t in range(20,-1,-1):
#                if x*1 + y*2 + z*5 + t*10 > 200:
#                    break
                for u in range(10,-1,-1):
#                    if x*1 + y*2 + z*5 + t*10 +u*20 > 200:
#                        break
                    for v in range(4,-1,-1):
#                        if x*1 + y*2 + z*5 + t*10 + u*20 + v*50 > 200:
#                            break
                        for w in range(2,-1,-1):
#                            if x*1 + y*2 + z*5 + t*10 + u*20 + v*50 + w*100 > 200:
#                                break
                            if x*1 + y*2 + z*5 + t*10 + u*50 + v*100 == 200:
                                num_combinations += 1

#Need to add 1 combination for the two-pound piece, which is easier to leave 
#out of the loop
print(num_combinations+1, "\nAnswer returned in " + str(round(time.time()-start,2)) + " seconds")
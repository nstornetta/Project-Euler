# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 19:46:17 2015

@author: NStornetta
"""
fraction_list = []

for x in range(10,101):
    for y in range(10,101):
        list_x, list_y= list(str(x)), list(str(y))
        for counter_x, digit_x in enumerate(list_x):
            for counter_y, digit_y in enumerate(list_y):
                if digit_x == digit_y and digit_x != "0":
                    list_x.remove(digit_x)
                    list_y.remove(digit_y)
                    try: 
                        frac = int(list_x[0])/int(list_y[0])                    
                        if frac == x/y and x/y <1:
                            fraction_list.append(frac)
                    except:
                        break

print(fraction_list)
#fraction list contains 1/4, 1/5, 2/5, and 1/2.  Multipled together = 2/200.
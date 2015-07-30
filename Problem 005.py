import time

def smallest_multiple(num):
    s = time.time()
    
    no_remainder = False
    remainder_counter = num+1
    
    while no_remainder == False:
        for i in range(1,num+1):
            if remainder_counter % i != 0:
                remainder_counter += 1
                break
        else:
            no_remainder = True
    return remainder_counter, time.time()-s

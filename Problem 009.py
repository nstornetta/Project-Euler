import time

def pythag_triplet(sum_num):
    s = time.time()
    for x in range(sum_num):
        for y in range(x):
            for z in range(y):
                # print (x,y,z)
                if x+y+z == sum_num and z**2+y**2==x**2:
                    return x*y*z, time.time()-s

import time


def palindrome_3_digit():
    s = time.time()
    for i in range(999,100,-1):
        for j in range(999,i-100,-1):
            product = str(i*j)
            reversed_product = product[::-1]
            if product == reversed_product:
                return product, time.time()-s

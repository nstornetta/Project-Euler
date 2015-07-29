# Trying to find the largest prime factor of 600851475143

def Euler3(n=600851475143):
    for i in range(2,600851475143):
        while n % i == 0:
            n //= i
            print("Yay, %d is a factor, now we should test %d" % (i, n))
            if n == 1 or n == i:
                return i

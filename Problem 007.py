def list_of_primes(nth_prime):
    prime_list = []
    prime_list.append(2)
    prime_list.append(3)
    x = 4
    while len(prime_list)<nth_prime:
        prime = None
        if x % 2 != 0 and x % 3 != 0 and x%5 != 0:
            for i in range(2,int(x**0.5)+1):
                if x % i == 0:
                    prime = False
            else:
                if prime == None:
                    prime = True
                    # print (x)
                    prime_list.append(x)
        x += 1
    else:
        return prime_list[nth_prime-2]

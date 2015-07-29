import time

def sum_of_primes(prime_limit):
    s = time.time()
    
    total = 10
    number_counter = 4
    while number_counter < prime_limit:
        is_prime = True

        if number_counter % 2 != 0 and number_counter % 3 != 0 and number_counter %5 != 0:
            for i in range(2,int(number_counter**0.5+1)):
                if number_counter % i == 0:
                    is_prime = False
                    break
            if is_prime == True:
                total += number_counter
            
        number_counter += 1

    return total, time.time()-s

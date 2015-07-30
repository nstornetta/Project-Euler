def sum_divisors(number):
    divisors_sum = 0
    for x in range(1,int((number/2)+1)):
        if number % x == 0:
            divisors_sum += x
    return divisors_sum

def amicable_number_sum(max_number):
    amicable_sum = 0
    for x in range(1,max_number+1):
        y = sum_divisors(x)
        z = sum_divisors(y)
        if z == x and x != y:
            amicable_sum = amicable_sum + x
            print(x,z,amicable_sum)
    return amicable_sum

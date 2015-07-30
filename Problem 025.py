fibonacci_sum_string = '0'
fibonacci_1 = 1
fibonacci_2 = 1
counter = 2

while len(fibonacci_sum_string) < 1000:
    fibonacci_sum = fibonacci_1 + fibonacci_2
    fibonacci_1 = fibonacci_sum
    counter += 1
    fibonacci_sum_string = str(fibonacci_sum)
    
    if len(fibonacci_sum_string) >= 1000:
        break
    else:
        fibonacci_sum = fibonacci_1 + fibonacci_2
        fibonacci_sum_string = str(fibonacci_sum)
        fibonacci_2 = fibonacci_sum
        counter += 1

print(counter)

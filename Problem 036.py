def decimal_to_binary_string(decimal_int):
    binary_string = bin(decimal_int)
    return binary_string[2:]

def two_base_palindromes_sum(max_number):
    palindrome_number_sum = 0
    for x in range(1,max_number+1):
        string_x = str(x)
        binary_x = decimal_to_binary_string(x)
        if string_x == string_x[::-1] and binary_x == binary_x[::-1]:
            palindrome_number_sum += x
    return palindrome_number_sum
        

def sum_of_digits(num):
    total = 0
    string_num = str(num)
    for digit in string_num:
        total += int(digit)
    return total

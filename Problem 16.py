def problem_16():
    x = 2**1000

    y = str(x)
    total = 0
    for digit in y:
        total += int(digit)
    return total

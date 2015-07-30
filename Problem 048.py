def self_power_sum(last_num):
    total = 0
    for x in range(1,last_num+1):
        total += x**x
    return total

def last_ten_digits(big_num):
    if len(str(big_num)) < 10:
        return "Sorry, that doesn't work"
    else:
        last_ten = str(big_num)[-10:]
        return last_ten

def problem_48(last_num):
    big_num = self_power_sum(last_num)
    return last_ten_digits(big_num)

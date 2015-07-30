def problem_6(top_num):
    total1, int_total, total2 = 0, 0, 0
    for x in range(top_num+1):
        total1 += x**2
    else:
        print total1

    for x in range(top_num+1):
        int_total +=x
    else:
        total2 = int_total**2
        print total2

    return total2-total1

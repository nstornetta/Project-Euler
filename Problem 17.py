from num2words import num2words

def letter_count_numbers(max_num):
    length = 0
    for x in range(1,max_num+1):
        y = num2words(x)
        y = y.replace(" ","")
        y = y.replace("-","")
        length += len(y)
    return length

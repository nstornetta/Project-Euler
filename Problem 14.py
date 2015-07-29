import time

s = time.clock()
def euler_14(max_number):
    max_length = [0, 0]
    for x in range(int((max_number/2)+1),max_number+1):
        y_length = 1
        y = x
        while y != 1:
            if y % 2 == 0:
                y = y/2
                y_length += 1
            else:
                y = 3*y + 1
                y_length += 1

        if y_length > max_length[1]:
            max_length[0],max_length[1] = x, y_length
    return max_length, time.clock()-s

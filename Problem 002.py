x1 = 1
x2 = 2
even_total = 2

while x1 and x2 < 4000000:
    x1 += x2
    if x1 % 2 == 0:
        even_total += x1
    x2 += x1
    if x2 % 2 == 0:
        even_total += x2

print (even_total)

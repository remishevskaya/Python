i = 0
while i < 100:
    i += 1
    if 11 <= i < 20:
        print(str(i) + ' процентов')
    if (1 <= i <= 10 or 20 <= i <= 100) and (i % 10 == 1):
        print(str(i) + ' процент')
    if (1 <= i <= 10 or 20 <= i <= 100) and (i % 10 == 2 or i % 10 == 3 or i % 10 == 4):
        print(str(i) + ' процента')
    if (1 <= i <= 10 or 20 <= i <= 100) and (i % 10 == 5 or i % 10 == 6 or i % 10 == 7 or i % 10 == 8
                                           or i % 10 == 9 or i % 10 == 0):
        print(str(i) + ' процентов')


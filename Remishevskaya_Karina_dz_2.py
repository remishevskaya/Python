list_num = list(range(1, 1000, 2))
list_cube = []  # Список кубов
for i in list_num:
    i = i ** 3
    list_cube.append(i)

list_sum = []  # Список сумм цифр кубов

for i in list_cube:
    sum_num = 0
    while i > 0:
        num = i % 10
        sum_num = sum_num + num
        i = i // 10
    list_sum.append(sum_num)

n = 0  # Чтобы посчитать индекс для list_cube
sum_div = 0  # Сумма чисел, сумма цифр которых делится на 7

for i in list_sum:
    if i % 7 == 0:
        sum_div = sum_div + list_cube[n]
    n += 1
print(sum_div)

cube_new = []

for i in list_cube:
    i = i + 17
    cube_new.append(i)

list_sum = []

for i in cube_new:
    sum_num = 0
    while i > 0:
        num = i % 10
        sum_num = sum_num + num
        i = i // 10
    list_sum.append(sum_num)

n = 0  # Чтобы посчитать индекс для cube_new
sum_div = 0  # Новая сумма чисел, сумма цифр которых делится на 7

for i in list_sum:
    if i % 7 == 0:
        sum_div = sum_div + cube_new[n]
    n += 1
print(sum_div)

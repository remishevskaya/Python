def num_gen(num):
    for num in range(1, num + 1, 2):
        yield num


num_res = num_gen(15)

print(*num_res)

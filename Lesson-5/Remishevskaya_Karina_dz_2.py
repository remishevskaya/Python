num = 15

num_gen = (num for num in range(1, num + 1, 2))

print(*num_gen)

import sys

nums = sys.argv[1:]
with open('bakery.csv', encoding='utf-8') as bakery_sales:
    if len(nums) > 1:
        idx_1 = int(nums[0])
        idx_2 = int(nums[1])
    elif len(nums) == 0:
        idx_1 = 0
        idx_2 = sum(1 for line in bakery_sales)
        bakery_sales.seek(0)
    else:
        idx_1 = int(nums[0])
        idx_2 = sum(1 for line in bakery_sales)
        bakery_sales.seek(0)

    for idx, line in enumerate(bakery_sales):
        if idx_1 <= idx + 1 <= idx_2:
            print(line.strip())

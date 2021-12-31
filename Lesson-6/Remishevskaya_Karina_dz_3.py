import json
from itertools import zip_longest
dict_pers = dict()
sum_lines_users = 0
sum_lines_hobbies = 0
with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobbies:
        for line in users:
            sum_lines_users += 1
        for line in hobbies:
            sum_lines_hobbies += 1
        if sum_lines_hobbies > sum_lines_users:
            exit(1)

        users.seek(0)
        hobbies.seek(0)

        for user, hobby in zip_longest(users, hobbies):
            dict_pers[user.strip().replace(',', ' ')] = hobby.strip() if hobby is not None else hobby

print(dict_pers)

with open('dict_pers.json', 'w') as dict_json:
    json.dump(dict_pers, dict_json, ensure_ascii=False)


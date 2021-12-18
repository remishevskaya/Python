workers_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
             'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for worker in workers_list:
    name = worker.split()[-1]
    print(f'Привет, {name.title()}!')

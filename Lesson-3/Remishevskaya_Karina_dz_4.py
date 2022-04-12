names = ['Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева']


def thesaurus_adv(x):
    dict_surnames = dict()
    dict_surnames_sort = dict()
    for pers in x:
        name, surname = pers.split()
        dict_surnames.setdefault(surname[0], {})
        dict_surnames[surname[0]].setdefault(name[0], [])
        dict_surnames[surname[0]][name[0]].append(pers)

    return dict_surnames


print(thesaurus_adv(names))

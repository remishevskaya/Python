names = ['Иван', 'Мария', 'Петр', 'Илья']


def thesaurus(x):
    dict_names = dict()
    first_let = []
    for name in x:
        first_let.append(name[0])
    first_let = sorted(first_let)
    for letter in first_let:
        dict_names.setdefault(letter, [])
    for name in x:
        dict_names[name[0]].append(name)
    return dict_names


print(thesaurus(names))

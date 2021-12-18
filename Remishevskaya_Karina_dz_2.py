word_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
phrase = []
for i in word_list:
    if i.isdigit():
        phrase.append(f'"{i}"')
    elif i.startswith('+'):
        phrase.append(f'"{i}"')
    else:
        phrase.append(i)
print(' '.join(phrase))





products = [57.8, 46.51, 97, 50.1, 32, 89.67, 60, 5.58, 201.3, 22]
products_new = []
for price in products:
    rub = int(price)
    coin = (price - rub) * 100
    products_new.append(f'{rub} руб. {coin:02.0f} коп.')

print(', '.join(products_new))

products = [57.8, 46.51, 97, 50.1, 32, 89.67, 60, 5.58, 201.3, 22]
print(id(products))
products.sort()
print(id(products))

products_new2 = []
for price in products:
    rub = int(price)
    coin = (price - rub) * 100
    products_new2.append(f'{rub} руб. {coin:02.0f} коп.')

print(', '.join(products_new2))

for price in products[::-1][:5:]:
    print(f'{int(price)} руб. {(price - int(price)) * 100:02.0f} коп.', end=', ')

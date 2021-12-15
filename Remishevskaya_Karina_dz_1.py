duration = int(input('Введите продолжительность времени в секундах: '))
if duration / 86400 >= 1:  # Есть ли дни
    print(str(duration // 86400) + ' дн ' + str((duration % 86400) // 3600) + ' час '
          + str((duration % 3600) // 60) + ' мин ' + str(duration % 60) + ' сек ')
elif duration / 3600 >= 1:  # Если часы
    print(str(duration // 3600) + ' час ' + str((duration % 3600) // 60) + ' мин '
          + str(duration % 60) + ' сек ')
elif duration / 60 >= 1:  # Если минуты
    print(str(duration // 60) + ' мин ' + str(duration % 60) + ' сек ')
else:  # Если секунды
    print(str(duration) + ' сек ')

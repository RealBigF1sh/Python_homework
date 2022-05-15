duration = int(input('Введите продолжительность в секундах: '))
days = duration//86400
hour = (duration-days*86400)//3600
mins = (duration-(days*86400+hour*3600))//60
secs = duration-(days*86400+hour*3600+mins*60)
if duration < 60:
    print(duration, 'сек')
elif 3600 >= duration >= 60:
    print(mins, 'мин', secs, 'сек')
elif 86400 >= duration >= 3600:
    print(hour, 'ч', mins, 'мин', secs, 'сек')
else:
    print(days, 'д', hour, 'ч', mins, 'мин', secs, 'сек')

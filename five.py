revenueSec = input('Какова выручка нашего нефтяного кортеля? : ')
сostsSec = input('Сколько идержек у нас? : ')

val = (int(revenueSec) - int(сostsSec))
res = "Прибыльный бизнесс )" if val > 0 else "кто то спустил всю выручку"
print(f'Так дорогуша значит у нас {res}')

if val > 0:
    print(f'Наша рентабельность хороша: {str(val)}')
    users = input('А не подскажете сколько у нас сотрудников? : ')
    print(f'Прибыль на сотрудника впечатляет: {val / int(users)}')

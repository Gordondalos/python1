user = input('Введите ваще имя: ')
print(f'Привет {user}!')
age = input('Сколько вам лет: ')
if int(age) > 50:
    print('Все повидал', end='\r\n')
else:
    print('Молодой еще', end='\r\n')

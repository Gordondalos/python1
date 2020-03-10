strSec = input('Дайте мне немного времени, сколько у вас есть секунд? : ')
a = int(strSec)
hour = a//3600
mimutes = (a // 60) % 60
seconds = a % 60
if mimutes < 10:
    mimutes = str('0' + str(mimutes))
else:
    mimutes = str(mimutes)
if seconds < 10:
    seconds = str('0' + str(seconds))
else:
    seconds = str(seconds)
print(f'Спасибо до создания новой вселенной осталось - {str(hour)}:{str(mimutes)}:{str(seconds)}')

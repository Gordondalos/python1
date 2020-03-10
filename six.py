aKm = input('Сколько километров мы бежим? : ')
bKm = input('А сколько всего нужно пробежать? : ')

i = 1
while int(aKm) < int(bKm):
    aKm = float(aKm) + float(aKm) * 10 / 100
    print(str(aKm))
    i += 1

print(f'нам понадобится {i} д.')

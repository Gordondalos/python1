strNum = input('Какие монетки у нас в кармане ? : ')
arr = list(strNum)
print(arr)
maxNum = 0
i = 0
while i < len(arr):
    if int(arr[i]) > maxNum:
        maxNum = int(arr[i])
    i += 1

print(f'Самая большая монета {maxNum}')
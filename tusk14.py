n = int(input('Введите число, т.е. диапазон поиска: '))
m = int(input('введите число, ограничевающее поиск: '))
for i in range(n):
    a = 2**i
    if(a < m):
        print(a)

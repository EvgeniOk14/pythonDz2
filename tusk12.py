sum = int(input('Введите сумму двух чисел Sum: '))
mult = int(input('Введите произведение двух чисел mult: '))
for x in range(sum + mult): # ограничиваем диапазон поиска, 
                            # т.к. числа не могут быть больше чем их сумма
    for y in range(sum + mult):
        if (x + y) == sum and (x * y) == mult:
            print('первое загаданное число равно: ', x)
            print('второе загаданное число равно: ', y)
            

'''
Задача 2

Напишите программу, которая ищет все числа в интервале от 300 до 430 включительно, делящиеся на 11,
но не делящиеся на 5. Выведите на экран все найденные числа.
'''

div_11 = []

for item in range(300, 431):
    if item % 5 == 0 and item % 11 == 0:
        pass
    elif item % 11 == 0:
        div_11.append(item)

print(str(div_11))

#[308, 319, 330, 341, 352, 363, 374, 385, 396, 407, 418, 429]
#[308, 319, 341, 352, 363, 374, 396, 407, 418, 429]
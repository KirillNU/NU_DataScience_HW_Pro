'''
Задача 1

Напишите программу, которая просит пользователя ввести произвольную цифру от 1 до 9,
а затем выводит таблицу умножения для введенного числа.

Добавьте проверку введенной пользователем информации:

    данные должны быть целочисленного типа
    число должно находиться в диапазоне от 1 до 9
'''

user_input = ''

while not user_input.isdigit():
    user_input = input('Введите целое число в диапазоне от 1 до 9 -> \n')

while not 1 <= int(user_input) <= 9:
    user_input = input('Введите целое число в диапазоне от 1 до 9 -> \n')

for i in range(1, 11):
    print(f'{user_input} * {i} = ', int(user_input) * i)

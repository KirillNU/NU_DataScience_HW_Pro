'''
Задача 5

Напишите функцию простейшего калькулятора. Пользователь вводит число a, число b и вид арифметической операции над ними.
Функция возвращает результат вычисления.

'''


def calc_arithm(a, b, function):
    func_list = ('+', '-', '*', '**', '/')
    result = None
    if function in func_list:
        if function == '+':
            result = a + b
        elif function == '-':
            result = a - b
        elif function == '*':
            result = a * b
        elif function == '**':
            result = a ** b
        elif function == '/':
            if b == 0:
                print('Деление на ноль!')
            else:
                result = a / b
    else:
        print('Неверная операция')

    return result


d = calc_arithm(121, 0.5, '**')
print(d)

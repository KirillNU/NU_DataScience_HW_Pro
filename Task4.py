'''
Задача 4

Создайте словарь (dict) c ключами, соответствующими числам от 1 до 10 включительно и
значениями, соответствующими квадратам ключей.

'''

my_dict = {key: key ** 2 for key in range(1, 11)}

print(my_dict)
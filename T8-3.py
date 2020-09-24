'''
3.
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на экран.
'''

class OE(Exception):
    def __init__(self, err):
        self.err = err

variable = True
whole = []
while variable == True:
    ini = []
    c_data = input('Input qq to interrupt or type floats or integers separated with spaces: ').split()
    if c_data.count('qq') > 0:
        print(f'{whole}\nand sum of this list is {sum(whole)}')
        variable = False
    else:
        for xx in c_data:
            if not xx.isdigit():
                raise OE('Something is worng!') # похоже, всё работает не так
            else:
                ini.append(float(xx))
    whole.extend(ini)
    print(f'Current list is: {ini}')
    print(f'The sum of current list is: {sum(ini)}')
    print(f'Total amount is: {sum(whole)}')

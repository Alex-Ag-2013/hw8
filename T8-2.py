'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
'''
class OwnErr(Exception):
    def __init__(self, text):
        self.text = text

req = input('Type two numbers (divisible and dividing) separated with semicolon: ').split(';')
try:
    if float(req[1]) == 0:
        raise OwnErr('Dividing number cannot be equal to 0!')
    else:
        print(round(float(req[0]) / float(req[1]), 5))
except ValueError:
    print('At least, one of given objects is not number!')
'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''


class Date:
    date_str = input('Type some date formatted as ''dd-mm-yyyy'': ').split('-')
    def __init__(self):
        pass

    @classmethod
    def date_nm(cls):
        dmy = [int(z) for z in cls.date_str]
        return dmy

    @staticmethod
    def el_proof(sx):
        dd, mm, yy = sx
        m_valid = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if mm > 0 and mm <= 12:
            print('You gave correct month')
        else:
            print('There is ome mistake with number of month')

        try:
            if dd <= m_valid[mm-1] and dd > 0:
                pass
            else:
                print(f'Number of date cannot be equal to 0 or more than {m_valid[mm-1]}')
        except IndexError:
            print('Wrong month or date')

        if yy < 1900:
            print('Far distant back date. But it is not mistake')
        else:
            print('Year is OK!')


da = Date.date_nm()
print(da)

print(Date.el_proof(da))
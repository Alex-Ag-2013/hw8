'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет
базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
'''

class Depot:
    max_capacity = 1000
    current_cap = 0
    def __init__(self, capacity: float):
        self.capacity = capacity

    def lim_cap(self, cap: float):
        self.cap = cap
        if self.current_cap + self.cap <= self.max_capacity:
            self.current_cap += self.cap
            print(f'{self.current_cap} total cubic metres of space is now occupied.')
        else:
            print('This item cannot be held in the depot due to lack of it''s capacity!')

class Technics:
    device_cnt = 0
    def __init__(self, producer, type):
        self.producer = producer
        self.type = type
        print(f'The producer of this {self.type} is {self.producer}.')

    def descript(self, descr: str):
        print(descr)

    def purchase(self, inc):
        self.device_cnt += inc

    def move_to_exp(self, qnty: int):
        self.qnty = qnty
        if self.device_cnt - self.qnty >= 0:
            self.device_cnt -= self.qnty
            print(f'You handed devices: {self.qnty} pcs to exploitation.')


class Printer(Technics, Depot):
    Technics.device_cnt += 1
    def __init__(self, producer, type='printer'):
        super().__init__(producer, type)

    def cap(self, cap: float):
        super().lim_cap(cap)

    def descript(self, descr='Transfers any graphical data on sheet of paper'):
        super().descript(descr)

pr1 = Printer('Xerox')
print(pr1.cap(31.65))
pr1.purchase(3)
print(pr1.device_cnt)

pr2 = Printer('Canon')
print(pr2.lim_cap(51.56))
print(pr2.device_cnt)
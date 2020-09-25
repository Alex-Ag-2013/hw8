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
        Depot.current_cap += self.capacity

    def lim_cap(self, cap: float):
        self.cap = cap
        if Depot.current_cap + self.cap <= Depot.max_capacity:
            Depot.current_cap += self.cap
            print(f'{Depot.current_cap} total cubic metres of space is now occupied.')
        else:
            print('This item cannot be held in the depot due to lack of it''s capacity!')

class Technics:
    printer_count = 0
    monitor_cnt = 0
    def __init__(self, producer, type):
        self.producer = producer
        self.type = type
        print(f'The producer of this {self.type} is {self.producer}.')

    def descript(self, descr: str):
        print(descr)

class Printer(Technics, Depot):
    def __init__(self, producer, type='printer'):
        super().__init__(producer, type)

    def cap(self, cap: float):
        super().lim_cap(cap)

    def descript(self, descr='Transfers any graphical data on sheet of paper'):
        super().descript(descr)

    def purchase(self, inc):
        Technics.printer_count += inc

    def move_to_exp(self, qnty: int):
        self.qnty = qnty
        if Technics.printer_count - self.qnty >= 0:
            Technics.printer_count -= self.qnty
            print(f'You handed devices: {self.qnty} pcs to exploitation.')

class Monitor(Technics, Depot):
    def __init__(self, producer, type='monitor'):
        super().__init__(producer, type)

    def cap(self, cap: float):
        super().lim_cap(cap)

    def purchase(self, inc):
        Technics.monitor_cnt += inc

    def descript(self, descr='Displays visual information on its screen'):
        super().descript(descr)

    def move_to_exp(self, qnty: int):
        self.qnty = qnty
        if Technics.monitor_cnt - self.qnty >= 0:
            Technics.monitor_cnt -= self.qnty
            print(f'You handed devices: {self.qnty} pcs to exploitation.')
        else:
            print(f'You have not so many monitors ({self.qnty})')

pr1 = Printer('Xerox')
xer_purchase = 3
xer_exp = 1
pr1.purchase(xer_purchase) # количество приобретённых принтеров
pr1.move_to_exp(xer_exp) # выдача в эксплуатацию
print(pr1.cap(31.65 * (max(xer_purchase - xer_exp, 0)))) # расчёт количества занимаемого места на складе
print(f'Total devices {pr1.printer_count}')
print(f'Total space in Depot occupied: {round(Depot.current_cap, 3)} cub. m.')
print('***\n' * 3)

mon1 = Monitor('Benq')
mon_purch = 16
mon_exp = 12
mon1.purchase(mon_purch)
mon1.move_to_exp(mon_exp)
mon1.cap(11.16 * (max(mon_purch - mon_exp, 0)))
print(f'Total devices {mon1.monitor_cnt}')
print(f'Total space in Depot occupied: {round(Depot.current_cap, 3)} cub. m.')
print('***\n' * 3)
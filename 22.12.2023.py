class Math:
    def plus(self):
        one_number = int(input('Введите 1 число:'))
        two_number = int(input('Введите 2 число:'))
        summa = one_number + two_number
        print('Равно:', summa)
    def raznost(self):
        one_number = int(input('Введите 1 число:'))
        two_number = int(input('Введите 2 число:'))
        minus = one_number - two_number
        print('Равно:', minus)
    def delenie(self):
        one_number = int(input('Введите 1 число:'))
        two_number = int(input('Введите 2 число:'))
        delit = one_number / two_number
        print('Равно:', delit)
    def umnosh(self):
        one_number = int(input('Введите 1 число:'))
        two_number = int(input('Введите 2 число:'))
        proizvedenie = one_number * two_number
        print('Равно:', proizvedenie)

kalkulator = Math()
while True:
    operation = int(input('Введите операцю(0 - выход из программы, 1 - сложение, 2 - вычитание, 3 - деление, 4 - умножение): '))
    if operation == 1:
        kalkulator.plus()
    elif operation == 2:
        kalkulator.raznost()
    elif operation == 3:
        kalkulator.delenie()
    elif operation == 4:
        kalkulator.umnosh()
    elif operation == 0:
        break
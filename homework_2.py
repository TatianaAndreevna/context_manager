from datetime import datetime


class Time:
    def __enter__(self):
        print('Время запуска кода в менеджере контекста: {}'.format(datetime.now().time()))
        self.time_start = datetime.now()
        return self

    def __exit__(self, *args):
        print('Время окончания работы кода: {}'.format(datetime.now().time()))
        self.time_end = datetime.now()
        self.spent_time = self.time_end - self.time_start
        print('Потрачено времени на выполнение кода: {}'.format(self.spent_time))


operation = str(input('Введите значение: ((-, +, *, /) число_1 число_2):'))
result = operation.split()


def polish_notation(operation):
    try:
        assert float(result[1]) >= 0 and float(result[2]) >= 0, 'Введено отрицательное число!'
        if result[0] == '+':
            print(float(result[1]) + float(result[2]))
        elif result[0] == '-':
            print(float(result[1]) - float(result[2]))
        elif result[0] == '*':
            print(float(result[1]) * float(result[2]))
        elif result[0] == '/':
            try:
                print(float(result[1]) / float(result[2]))
            except ZeroDivisionError:
                print('На ноль делить нельзя!')
        else:
            print('Ошибка')
    except AssertionError:
            print('Введено отрицательное число!')


with Time():
    polish_notation(operation)
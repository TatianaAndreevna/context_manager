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
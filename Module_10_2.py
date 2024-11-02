import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.day = 0

    def fight(self, name, power, delay_day):
        enemy = 100
        self.day = 0
        while enemy:
            self.day += 1
            time.sleep(delay_day)
            print(f'{name} сражается {self.day} дней..., осталось {enemy} воинов.')
            enemy = enemy - power

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.fight(self.name, self.power, delay_day=1)
        print(f'{self.name} одержал победу спустя {self.day} дней(дня)!')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

# if first_knight.is_alive() and second_knight.is_alive():
#     pass
# else:
print('Все битвы закончились!')
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения

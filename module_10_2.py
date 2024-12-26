import time
import threading as thd

class Knight(thd.Thread):
    def __init__(self, name, power):
        thd.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!' )
        enemy = 100
        day = 0
        while enemy:
            time.sleep(1)
            day += 1
            enemy -= self.power
            print(f"{self.name} сражается {day} день(дня)..., осталось {enemy} воинов.")
        print(f"{self.name} одержал победу спустя {day} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")
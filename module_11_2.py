import sys
import inspect as ins
from pprint import pprint
import random
import time

class Human:

    def __init__(self, name:str, weight):
        self.name = name
        self._health = True
        self._cheerfulness = 100
        self.weight = weight
        self._ill_days = 0

    def _get_sick(self):
        r = random.randint(1, 10)
        if r > 9 and self._health:
            self._health = False
            self._ill_days = random.randint(1, 3)
            if self._ill_days > 1:
                d = 'дня'
            else:
                d = 'день'
            print(f'К сожалению, {self.name} заболел/-а на {self._ill_days} {d} и не сможет тренироваться.')

    def _training(self):
        self._get_sick()
        if not self._health:
            print(f'Сегодня {self.name} не сможет тренироваться.')
            time.sleep(1)
            return
        r = round(random.random() * 2, 1)
        self.weight -= r
        print(f'Вы успешно потренировались и потеряли {r} кг. {self.name} весит теперь {self.weight}')
        time.sleep(1)

    def _work(self):
        if self._health:
            print(f'Наступил новый день! {self.name} пошёл/-ла на работу.')
            self._get_sick()
            print(f'Вы закончили работать!')
        else:
            print(f'Сегодня {self.name} не сможет работать.')
        time.sleep(1)

    def lose_weight(self, weight_goal):
        while self.weight > weight_goal:
            self._work()
            self._training()
            if self._ill_days > 0:
                self._ill_days -= 1
            else:
                self._health = True
        print(f'{self.name} похудел/-а до {weight_goal} кг.')




def introspection_info(any_object):
    return {'Type: ': type(any_object),
            'Attributes: ': [a for a in any_object.__dict__.keys()],
            'Methods: ': [m[0] for m in ins.getmembers(any_object, predicate=ins.ismethod)],
            'Module: ': ins.getmodule(any_object)}

alice = Human('Алиса', 80)
info_int = introspection_info(alice)
pprint(info_int)

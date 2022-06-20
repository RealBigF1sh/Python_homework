from time import sleep
from itertools import cycle


class TrafficLight:

    def __init__(self):
        self.__color = (('Red', 8), ('Yellow', 5), ('Green', 8))

    def running(self):
        for color, secs in cycle(self.__color):
            print(color, 'pause {} sec'.format(secs))
            sleep(secs)


tl = TrafficLight()
tl.running()

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} is starting'.format(self.name))

    def stop(self):
        print('{} is stopping'.format(self.name))

    def turn(self, direction):
        print('{} is turning {}'.format(self.name, direction))

    def show_speed(self):
        print('Speed is ', self.speed)


class TownCar(Car):
    def show_speed(self):
        print('Speed is ', self.speed)
        if self.speed > 60:
            print('Attention! Speed is too high!')


class WorkCar(Car):
    def show_speed(self):
        print('Speed is ', self.speed)
        if self.speed > 40:
            print('Attention! Speed is too high!')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


sport = SportCar(200, 'Red', 'Ferrari', False)
town = TownCar(80, 'Blue', 'Skoda', False)
work = WorkCar(50, 'Black', 'Zil', False)
police = PoliceCar(100, 'White', 'Ford', False)

sport.show_speed()
town.show_speed()
work.show_speed()
police.show_speed()
town.turn('right')

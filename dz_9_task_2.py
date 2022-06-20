class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def mass_calculator(self):
        mass = self._lenght * self._width * 25 * 5 / 1000
        return mass


start = Road(200, 50)
print(start.mass_calculator(), 'т')

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('{} пишет'.format(self.title))


class Pencil(Stationery):
    def draw(self):
        print('{} пишет'.format(self.title))


class Handle(Stationery):
    def draw(self):
        print('{} пишет'.format(self.title))


pen = Pen('Parker')
pencil = Pencil('BIC')
handle = Handle('Umo')

pen.draw()
pencil.draw()
handle.draw()

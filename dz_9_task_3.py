class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_pay = income['pay']
        self._income_bonus = income['bonus']

class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'

    def get_total_income(self):
        return self._income_pay + self._income_bonus


p = Position('Сергей', 'Смирнов', 'директор', {'pay' : 150000, 'bonus': 25000})
print(p.get_full_name())
print(p.get_total_income())

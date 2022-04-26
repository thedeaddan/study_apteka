class Apteka(object):
    """Инициализация полей"""

    def __init__(self, name):
        self.data = {
            'name': name,
            'preparats': {
                'name': [],
                'cost': []
            }
        }

    """Выводим стоимость всех лекарств"""

    def total_cost(self):
        cost = 0
        for phar in self.data['preparats']['cost']:
            cost += phar
        print(cost)

    """Выводим самую высокую цену за лекартсво"""

    def max_cost(self):
        cost = max(self.data['preparats']['cost'])
        print(f'Максимальная цена на лекарство в данной аптеке: {cost} р.')

    """Выводим полную информацию об аптеке"""

    def full_info(self):
        i = 1
        c = 0
        print(f'Название аптеки - {self.data["name"]}')
        for name in self.data['preparats']['name']:
            print(f'    {i}) {name} - {self.data["preparats"]["cost"][c]}')
            i += 1
            c += 1

    """Добавляем лекартсва от пользователя"""

    def add_pill(self, prep_name, prep_cost):
        print('Добавление препарата от пользователя')
        self.data['preparats']['name'].append(prep_name)
        self.data['preparats']['cost'].append(prep_cost)
        

from apteka import Apteka
import sys


def phar_list():
    i = 1
    for phar in pharmacy_list:
        print(f'{i}) {phar.data["name"]}')
        i += 1
    return i

pharmacy_list = list()
while True:
    print('Введите help для вывода списка команд..')
    com = input('Введите команду: ')

    if com == 'create':
        name = input('Введите название новой аптеки: ')
        phar = Apteka(name)
        pharmacy_list.append(phar)

    elif com == 'add pill':
        print('В какую аптеку вы хотите добавить лекарство (выберите номер)')
        i = phar_list()
        num = int(input('Ваш выбор - ')) - 1
        print('Добавляем в базу новый препарат..')
        name = input('Название препарата: ')
        cost = input('Стоимость препарата: ')
        pharmacy_list[num].add_pill(name, cost)

    elif com == 'full info':
        print('Выберите аптеку о которой вы хотите получить информацию..')
        i = phar_list()
        num = int(input('Ваш выбор - ')) - 1
        pharmacy_list[num].full_info()

    elif com == 'total cost':
        print('Выберите аптеку, сумму стоимости лекарств которой вы хотите получить')
        i = phar_list()
        num = int(input('Я выбираю - ')) - 1
        pharmacy_list[num].total_cost()

    elif com == 'max cost':
        print('Выберите аптеку в которой вы хотите узнать максимальную цену лекартва')
        i = phar_list()
        num = int(input('Я выбираю - ')) - 1
        pharmacy_list[num].max_cost()

    elif com == 'help':
        print('''
Вот список команд:
create - Добавить в список аптеку
add pill - Добавить лекарство в аптеку
total cost - Узнать сумму стоимости всех лекарств
max cost - Узнать максимальну цену лекартсва в аптеке
full info - Получить полную информацию об аптеке
exit - Выход
''')
    elif com == 'exit':
        sys.exit(0)

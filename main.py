import int_inp

apteki = {}
apteki_names = []
preps = {}


class Apteka:
    def create():
        print("Создание аптеки..")
        name = input("Введите имя аптеки: ")
        apteki_names.append(name)
        print("Добавление препаратов. Напишите *, чтоб закончить добавление")
        i = 1
        while True:
            prep_name = input("Введите имя препарата: ")
            if prep_name == "*":
                print("Добавление препаратов окончено")
                break
            print("Введите стоимость препарата в рублях..")
            prep_cost = int_inp.check_input()
            if prep_cost == None:
                prep_cost = "Стоимость не указана"
            local_prep = {}
            local_prep["Имя препарата"] = prep_name
            local_prep["Стоимость"] = prep_cost
            preps["count"] = i
            preps[i] = local_prep
            apteki[name] = preps

            print(apteki)
            i += 1
            print(f"Добавлен препарат {prep_name} со стоимостью {prep_cost}р.")
    def get_all_fields():
        print("Все данные об аптеках: ")
        if apteki == {}:
            print("Вы ещё не добавляли аптеки...")
        else:
            for i in apteki_names:
                print(f"Название: {i}")
                info = apteki[apteki_names[0]]
                for i in range(1,info["count"]+1):
                    detailed_info = info[i]
                    print(f"    Название препарата:{detailed_info['Имя препарата']} со стоимостью {detailed_info['Стоимость']} рублей")
                    #print(detailed_info)

Apteka.create()
Apteka.get_all_fields()



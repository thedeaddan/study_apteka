def check_input():
    var = input("Введите число: ")
    try:
        var = int(var)
        return var
    except:
        print(f"Ваше число вовсе не число! Как {var} может быть числом?")

# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13


def InputNumbers(inputText):
    okey = False
    while not okey:
        try:
            number = int(input(f"{inputText}"))
            okey = True
        except ValueError:
            print("Это не число!")
    return number


def fillsFormula(num):
    num_list = []
    for i in range(1, num + 1):
        num_list.append(round((1 + 1 / i) ** i))
    print(num_list)
    print(sum(num_list))


num = InputNumbers("Введите число: ")
fillsFormula(num)

# * 4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15


def InputNumbers(inputText):
    okey = False
    while not okey:
        try:
            number = int(input(f"{inputText}"))
            okey = True
        except ValueError:
            print("Это не число!")
    return number


def inputKoord(x, roster):
    a = [0] * x
    coverage = len(roster)
    for i in range(x):
        is_OK = False
        while not is_OK:
            try:
                number = int(input(f"Введите {i+1} позицию числа: "))
                a[i] = number
                is_OK = True
                if number > coverage or number < 0:
                    is_OK = False
                    print("Такой позиции нет! ") 
            except ValueError:
                print("Ты ошибся. Вводить надо числа!")
    return a


def fillsList(num):
    num_list = []
    for i in range(-num, num + 1):
        num_list.append(i)
    return num_list


def findPiece(position, list):
    result = list[position[0]] * list[position[1]]
    return result


num = InputNumbers("Ведите число для заполнения списка: ")
list = fillsList(num)
print(list)
position = inputKoord(2,list)
print(findPiece(position, fillsList(num)))
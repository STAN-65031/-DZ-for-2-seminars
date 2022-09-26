# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

import random

def InputNumbers(inputText):
    okey = False
    while not okey:
        try:
            number = int(input(f"{inputText}"))
            okey = True
        except ValueError:
            print("Это не число!")
    return number


def fillsList(num):
    num_list = []
    for i in range(num):
        num_list.append(round(i))
    return num_list



def shuffleList(list):
    result_list = []
    for i in list:
        result_list =sorted(list, key=lambda i: random.random())
    return result_list

num = InputNumbers("Введите длинну списка: ")
list1 = fillsList(num)
list2 = shuffleList(list1)
print(list1)
print(list2)

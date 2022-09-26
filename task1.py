# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27


def InputNumbers(inputText):
    okey = False
    while not okey:
        try:
            number = float(input(f"{inputText}"))
            okey = True
        except ValueError:
            print("Это не число!")
    return number


def sumNums(num):
    num *= 10 ** len(str(num))
    b = []
    while num > 0:
        b.append(int(num % 10))
        num = num // 10
    sum = 0
    for i in range(len(b)):
        sum += b[i]
    return sum


num = InputNumbers("Введите число: ")

print(f"Сумма цифр = {sumNums(num)}")

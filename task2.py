# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

def InputNumbers(inputText):
    okey = False
    while not okey:
        try:
            number = int(input(f"{inputText}"))
            okey = True
        except ValueError:
            print("Это не число!")
    return number


def findFactorial(n):
    if n == 1:
        return 1
    else:
        return n * findFactorial(n - 1)


num = InputNumbers("Введите число: ")

list = []
for i in range(1, num + 1):
    list.append(findFactorial(i))

print(f"Произведения чисел от 1 до {num}:  {list}")
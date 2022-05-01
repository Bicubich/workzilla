import numpy as np
from random import randint

# функция печатает содержимое массива в виде матрицы
def PrintMassive(massive, name):
    print(f"{name} матрица:", end= " ")
    # вывод массива в виде матрицы на экран
    for i in range(0, n):
        for j in range(0, n):
            if j == 0:
                print()
            if j != n - 1:
                print(massive[i][j] , "|", end=' ')
            else:
                print(massive[i][j], end=' ')
            if i == n - 1 and j == n - 1:
                print()

# ввод размерности и границ значений элементов массива с клавиатуры
try:
    n = int(input("Введите кол-во строк в массиве(1..10^4): "))
    x = int(input("Введите нижний диапазон значения элементов(1..10^4): "))
    y = int(input("Введите верхний диапазон значения элементов(1..10^4): "))
    while n < 1 or n > 10 ** 4 or x < 1 or x > 10 ** 4 or y < 1 or y > 10 ** 4:
        print("Размерность массива не может быть меньше или равно 0, попробуйте ещё!\n")
        n = int(input("Введите кол-во строк в массиве(1..10^4): "))
        x = int(input("Введите нижний диапазон значения элементов(1..10^4): "))
        y = int(input("Введите верхний диапазон значения элементов(1..10^4): "))
except ValueError:
    print("Вы ввели не число!")

print(f"{n} {x} {y}")
# заполнение массива
massive1 = [[randint(-abs(x), abs(y)) for j in range(n)] for i in range(n)]
massive2 = [[randint(-abs(x), abs(y)) for j in range(n)] for i in range(n)]

# вывод матриц на экран
PrintMassive(massive1, "Первая")
PrintMassive(massive1, "Вторая")

# умножение матриц при помощи библиотеки numpy
print("Произведение матриц:")
print(np.dot(massive1, massive2))
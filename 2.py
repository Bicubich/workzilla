from random import randint

# ввод размерности массива с квлавиатуры
try:
    n = int(input("Введите кол-во строк в массиве(1<=n<=10^2): "))
    m = int(input("Введите кол-во столбцов в массиве(1<=n<=10^2): "))
    while n < 1 or m < 1 or n > 10 ** 2 or m > 10 ** 2:
        print("Неверная размерность массива, попробуйте ещё!\n")
        n = int(input("Введите кол-во строк в массиве(1<=n<=10^2): "))
        m = int(input("Введите кол-во столбцов в массиве(1<=n<=10^2): "))
except ValueError:
    print("Вы ввели не число!")

# заполнение массива
massive = [[randint(1, 100) for j in range(m)] for i in range(n)]

maxim = -10000
minim = 10000

print(f"Полученный массив {n}х{m}:")
# вывод массива в виде матрицы на экран
for i in range(0, n):
    for j in range(0, m):
        if j == 0:
            print()
        if j != m - 1:
            print(massive[i][j] , "|", end=' ')
        else:
            print(massive[i][j], end=' ')
        if i == n - 1 and j == m - 1:
            print()

# опеределение максимального и минимального элемента массива
for i in range(0, n):
    for j in range(0, m):
        maxim = max(maxim, massive[i][j])
        minim = min(minim, massive[i][j])


summ = 0
# вывод и опеределение суммы элементов массива по каждой строке
for i in range(0, n):
    for j in range(0, m):
        summ += massive[i][j]
        if j == m - 1:
            print(f"Сумма {i+1} строки = {summ}")
            summ = 0

# вводим доболнительный массив и заполняем его столькими нулями, сколько столбцов у нашего массива            
buff_massive = [0]*m
# опеределение суммы элементов массива по каждому стобцу
for i in range(0, n):
    for j in range(0, m):
        buff_massive[j] += massive[i][j]

#счётчик
k = 1
# вывод суммы элементов массива по каждому столбцу
for i in buff_massive:
    print(f"Сумма {k} столбца = {i}")
    k += 1

print(f"Максимальное значение: {maxim}")
print(f"Минимальное значение: {minim}")


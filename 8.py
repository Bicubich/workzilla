from random import randint

# ввод диапазона чисел
try:
    x = int(input("Введите нижний диапазон значения элементов(0..10^4): "))
    y = int(input("Введите верхний диапазон значения элементов(0..10^4): "))
    while x < 0 or x > 10 ** 4 or y < 0 or y > 10 ** 4:
        print("Неверный диапазон, попробуйте ещё!\n")
        x = int(input("Введите нижний диапазон значения элементов(0..10^4): "))
        y = int(input("Введите верхний диапазон значения элементов(0..10^4): "))
except ValueError:
    print("Вы ввели не число!")

attempts = 1
Var1 = randint(x, y)
print (f"Я загадал число в диапазоне от {x} до {y}. Удачи!")
Var2 = int(input("Введите догадку, пожалуйста: "))
while Var1 != Var2:
    if Var1 > Var2: print (f"Больше!", end = " ")
    elif Var1 < Var2: print (f"Меньше!", end = " ")
    attempts += 1
    Var2 = int(input("Введите догадку, пожалуйста: "))
print (f"Поздравляю, вы угадали число! Вам потребовалось {attempts} попыток.")
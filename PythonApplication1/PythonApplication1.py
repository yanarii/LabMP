import sys
import io

# Настраиваем стандартный вывод на UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("Привет, Visual Studio!")
# Просим пользователя ввести число от 1 до 9
x = int(input("Введите число от 1 до 9: "))

# Проверяем условие: если число от 1 до 3
if 1 <= x <= 3:
    s = input("Введите строку: ")  # просим строку
    n = int(input("Введите число повторов строки: "))  # преобразуем ввод в число
    for i in range(n):  # цикл повторяется n раз
        print(s)

# Если число от 4 до 6
elif 4 <= x <= 6:
    m = int(input("Введите степень: "))  # степень
    result = x ** m  # возведение в степень
    print("Результат:", result)

# Если число от 7 до 9
elif 7 <= x <= 9:
    for i in range(10):  # цикл 10 раз
        x += 1
        print(x)

# Во всех остальных случаях
else:
    print("Ошибка ввода")


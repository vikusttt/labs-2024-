def fibonacci(n):
    if n <= 0:
        return "Введіть число більше 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a + b
        return b

# Запит у користувача введення числа
num = int(input("Введіть число n для обчислення n-го числа Фібоначчі: "))

# Виведення результату
print(f"{num}-те число Фібоначчі: {fibonacci(num)}")
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль!"
    return x / y

def main():
    print("Простой калькулятор")
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")

    while True:
        choice = input("Введите номер операции (1/2/3/4): ")
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
            except ValueError:
                print("Пожалуйста, введите корректные числовые значения.")
                continue

            if choice == '1':
                print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Результат: {num1} / {num2} = {result}")
        else:
            print("Некорректный выбор. Пожалуйста, выберите операцию от 1 до 4.")

        # Спросить пользователя, хочет ли он продолжить
        next_calculation = input("Хотите ли вы выполнить другую операцию? (да/нет): ").strip().lower()
        if next_calculation != 'да':
            print("Спасибо за использование калькулятора. До свидания!")
            break

if __name__ == "__main__":
    main()
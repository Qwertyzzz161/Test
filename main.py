def main(input_str):
    elements = input_str.split()
    num1, operation, num2 = elements

    if len(elements) != 3:
        return "Ошибка: введите два числа и операцию между ними."


    try:
        num1 = int(num1)
        num2 = int(num2)
    except:
        return "Ошибка: введите целые числа."

    if not (1 <= num1 <= 10) or not (1 <= num2 <= 10):
        return "Ошибка: введите числа от 1 до 10 включительно."


    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Ошибка: деление на ноль."
        result = num1 // num2
    else:
        return "Ошибка: неизвестная операция."
    return f"Результат: {result}"


if __name__ == "__main__":
    user_input = input("Введите выражение в формате <<X + Y>>: ")
    print(main(user_input))

#В некоторых местах блок try-except не работал,
# так и не смог понять почему.
# Поэтому вывод ошибок сделал через if-return
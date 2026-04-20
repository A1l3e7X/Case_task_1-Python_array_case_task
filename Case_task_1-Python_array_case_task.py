def get_int_input(prompt):
    """Безопасный ввод целого числа."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")


def main():
    # Ввод количества элементов массива
    n = get_int_input("Введите количество элементов массива: ")

    # Проверка размера массива
    if n <= 0:
        print("Массив пуст или его размер задан некорректно.")
        return

    # Ввод элементов массива
    a = [get_int_input(f"Введите элемент A[{i}]: ") for i in range(n)]

    # Нахождение минимального и максимального элементов
    min_value = min(a)
    max_value = max(a)

    # Нахождение индексов первого вхождения минимального и максимального элементов
    min_index = a.index(min_value)
    max_index = a.index(max_value)

    # Определение диапазона между минимальным и максимальным элементами
    start, end = sorted([min_index, max_index])

    # Вычисление суммы отрицательных элементов между ними
    negative_sum = sum(x for x in a[start + 1:end] if x < 0)

    # Вывод результата
    print("\nИсходный массив:", a)
    print("Минимальный элемент:", min_value)
    print("Максимальный элемент:", max_value)
    print("Индекс минимального элемента:", min_index)
    print("Индекс максимального элемента:", max_index)
    print("Сумма отрицательных элементов между минимальным и максимальным:", negative_sum)


if __name__ == "__main__":
    main()

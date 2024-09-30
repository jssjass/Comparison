import random

# Функция для ввода данных вручную
def input_arrays():
    array1 = input("Введите элементы первого массива через пробел: ")
    array2 = input("Введите элементы второго массива через пробел: ")
    # Преобразуем строку в список чисел
    array1 = list(map(int, array1.split()))
    array2 = list(map(int, array2.split()))
    return array1, array2

# Функция для генерации массивов случайных чисел
def generate_arrays(size=5, range_start=0, range_end=10):
    array1 = [random.randint(range_start, range_end) for _ in range(size)]
    array2 = [random.randint(range_start, range_end) for _ in range(size)]
    return array1, array2

# Функция для отображения главного меню
def display_menu():
    print("\nГлавное меню:")
    print("1: Ввод исходных данных вручную")
    print("2: Генерация исходных данных случайным образом")
    print("3: Выполнение алгоритма")
    print("4: Завершение работы программы")

# Функция для проверки общих чисел
def check_common_numbers(array1, array2):
    common_count = 0
    reversed_array2 = [int(str(num)[::-1]) for num in array2]  # Переворачиваем числа во втором массиве

    # Проверяем, сколько чисел из первого массива встречаются во втором (или его перевернутом)
    for num in array1:
        if num in array2 or num in reversed_array2:
            common_count += 1

    return common_count

def main():
    array1 = []
    array2 = []
    results_processed = False  # Флаг для проверки, были ли обработаны данные

    while True:
        display_menu()
        choice = input("Выберите пункт меню (1-4): ")

        if choice == '1':
            array1, array2 = input_arrays()
            results_processed = False  # Сбрасываем флаг при вводе новых данных

        elif choice == '2':
            array1, array2 = generate_arrays()
            print("Сгенерированы массивы:")
            print("Массив 1:", array1)
            print("Массив 2:", array2)
            results_processed = False  # Сбрасываем флаг при генерации новых массивов

        elif choice == '3':
            if not array1 or not array2:
                print("Ошибка: Для выполнения алгоритма необходимо ввести исходные данные!")
                continue  # Пропускаем итерацию, если данные не введены

            common_count = check_common_numbers(array1, array2)
            print(f"Количество общих чисел (включая перевернутые): {common_count}")
            results_processed = True  # Устанавливаем флаг, что результаты обработаны

        elif choice == '4':
            print("Завершение работы программы.")
            break  # Выходим из цикла и заканчиваем программу

        else:
            print("Ошибка: Неверный выбор. Пожалуйста, выберите пункт меню от 1 до 4.")

        if results_processed:
            print("Результаты были выведены, введите новые данные для сброса результатов.")

if __name__ == "__main__":
    main()

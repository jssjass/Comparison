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

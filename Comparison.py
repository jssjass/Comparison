import random
import threading
import queue

# Очереди для обмена данными между потоками
input_queue = queue.Queue()
output_queue = queue.Queue()

def generate_arrays(size=5, range_start=0, range_end=10):
    """Генерирует два массива случайных целых чисел."""
    array1 = [random.randint(range_start, range_end) for _ in range(size)]
    array2 = [random.randint(range_start, range_end) for _ in range(size)]
    input_queue.put((array1, array2))  # Помещаем массивы в очередь
    output_queue.put(f"Сгенерированы массивы:\nМассив 1: {array1}\nМассив 2: {array2}")

def check_common_numbers(array1, array2):
    """Проверяет наличие общих чисел между двумя массивами."""
    common_numbers = []
    reversed_array2 = [int(str(num)[::-1]) for num in array2]

    for num in array1:
        if num in array2:
            common_numbers.append((num,))
        elif num in reversed_array2:
            idx = reversed_array2.index(num)
            common_numbers.append((num, array2[idx]))

    return common_numbers

def menu():
    """Выводит меню и обрабатывает выбор пользователя."""
    while True:
        print("\nМеню:")
        print("1. Сгенерировать случайные массивы")
        print("2. Ввести массивы вручную")
        print("3. Выход")

        choice = input("Выберите действие (1-3): ")

        if choice == "1":
            thread = threading.Thread(target=generate_arrays)
            thread.start()
            thread.join()  # Ждем завершения генерации массивов

            array1, array2 = input_queue.get()  # Получаем сгенерированные массивы
            print(f"Массив 1: {array1}")
            print(f"Массив 2: {array2}")

            common_numbers = check_common_numbers(array1, array2)
            if common_numbers:
                print("Найдены совпадения:")
                for numbers in common_numbers:
                    if len(numbers) == 1:
                        print(f"Число: {numbers[0]}")
                    else:
                        print(f"Число: {numbers[0]} (отзеркаленно: {numbers[1]})")
            else:
                print("Совпадений не найдено.")

        elif choice == "2":
            # Реализация для ввода массивов вручную
            try:
                array1 = list(map(int, input("Введите элементы первого массива через пробел: ").split()))
                array2 = list(map(int, input("Введите элементы второго массива через пробел: ").split()))
                common_numbers = check_common_numbers(array1, array2)
                if common_numbers:
                    print("Найдены совпадения:")
                    for numbers in common_numbers:
                        if len(numbers) == 1:
                            print(f"Число: {numbers[0]}")
                        else:
                            print(f"Число: {numbers[0]} (отзеркаленно: {numbers[1]})")
                else:
                    print("Совпадений не найдено.")
            except ValueError:
                print("Ошибка ввода. Пожалуйста, введите числовые значения.")

        elif choice == "3":
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Пожалуйста, выберите пункт меню от 1 до 3.")

if __name__ == "__main__":
    menu()

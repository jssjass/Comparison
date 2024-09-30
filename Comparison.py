import random
import threading
import queue
import time

# Очереди для обмена данными между потоками
input_queue = queue.Queue()
output_queue = queue.Queue()
calculation_queue = queue.Queue()

def input_arrays():
    """Запрашивает у пользователя ввод данных для двух массивов."""
    array1 = input("Введите элементы первого массива через пробел: ")
    array2 = input("Введите элементы второго массива через пробел: ")

    array1 = list(map(int, array1.split()))
    array2 = list(map(int, array2.split()))
    input_queue.put((array1, array2))

def generate_arrays(size=5, range_start=0, range_end=10):
    """Генерирует два массива случайных целых чисел."""
    array1 = [random.randint(range_start, range_end) for _ in range(size)]
    array2 = [random.randint(range_start, range_end) for _ in range(size)]
    input_queue.put((array1, array2))
    output_queue.put(f"Сгенерированы массивы:\nМассив 1: {array1}\nМассив 2: {array2}")

def check_common_numbers(array1, array2):
    """Проверяет наличие общих чисел между двумя массивами."""
    common_count = 0
    reversed_array2 = [int(str(num)[::-1]) for num in array2]

    for num in array1:
        if num in array2 or num in reversed_array2:
            common_count += 1

    output_queue.put(f"Количество общих чисел (включая перевернутые): {common_count}")

def calculation_thread():
    """Поток для выполнения вычислений."""
    while True:
        task = calculation_queue.get()
        if task == "exit":
            break
        array1, array2 = task
        check_common_numbers(array1, array2)
        calculation_queue.task_done()

def input_thread():
    """Поток для обработки пользовательского ввода."""
    while True:
        task = input_queue.get()
        if task == "exit":
            break
        if task == "manual":
            input_arrays()
        elif task == "generate":
            generate_arrays()
        input_queue.task_done()

def output_thread():
    """Поток для вывода результатов."""
    while True:
        message = output_queue.get()
        if message == "exit":
            break
        print(message)
        output_queue.task_done()

def main():
    """Главная функция программы, управляющая логикой работы."""
    # Запуск потоков
    threading.Thread(target=calculation_thread, daemon=True).start()
    threading.Thread(target=input_thread, daemon=True).start()
    threading.Thread(target=output_thread, daemon=True).start()

    array1 = []
    array2 = []
    results_processed = False

    while True:
        print("\nГлавное меню:")
        print("1: Ввод исходных данных вручную")
        print("2: Генерация исходных данных случайным образом")
        print("3: Выполнение алгоритма")
        print("4: Завершение работы программы")

        choice = input("Выберите пункт меню (1-4): ")

        if choice == '1':
            input_queue.put("manual")
            array1, array2 = input_queue.get()
            results_processed = False

        elif choice == '2':
            input_queue.put("generate")
            array1, array2 = input_queue.get()
            results_processed = False

        elif choice == '3':
            if not array1 or not array2:
                print("Ошибка: Для выполнения алгоритма необходимо ввести исходные данные!")
                continue

            calculation_queue.put((array1, array2))
            results_processed = True

        elif choice == '4':
            print("Завершение работы программы.")
            input_queue.put("exit")
            calculation_queue.put("exit")
            output_queue.put("exit")
            break

        else:
            print("Ошибка: Неверный выбор. Пожалуйста, выберите пункт меню от 1 до 4.")

        if results_processed:
            print("Результаты были выведены, введите новые данные для сброса результатов.")

        # Небольшая задержка, чтобы дать время другим потокам обработать данные
        time.sleep(0.1)

if __name__ == "__main__":
    main()

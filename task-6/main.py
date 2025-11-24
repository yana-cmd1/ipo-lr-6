#вариант 4
import random  # импорт модуля для случайных чисел
numbers = []#пустой список
for i in range(20):  # цикл для создания 20 групп
    group = []  # создание пустой группы
    for j in range(4):  # цикл для создания 4 чисел в группе
        num = random.randint(-10, 10)  # генерация случайного числа
        group.append(num)  # добавление числа в группу
    numbers.append(group)  # добавление группы в общий список

print("Сгенерированный список:")  # вывод заголовка
for i in range(len(numbers)):  # перебор всех групп
    print(f"Группа {i+1}: {numbers[i]}")  # вывод каждой группы

# нахождение всех уникальных комбинаций
all_combinations = []  # список для всех комбинаций

for group in numbers:  # перебор всех групп чисел
    for i in range(len(group)):  # перебор индексов первого числа
        for j in range(i+1, len(group)):  # перебор индексов второго числа
            # создание кортежа из двух чисел
            pair = (group[i], group[j])
            # сортировка чисел в кортеже для уникальности порядка
            sorted_pair = tuple(sorted(pair))
            all_combinations.append(sorted_pair)  # добавление в общий список

# удаление дубликатов через преобразование в множество и обратно
unique_combinations = list(set(all_combinations))
# сортировка комбинаций для красивого вывода
unique_combinations.sort()

print("\nУникальные комбинации:")  # вывод заголовка
for i in range(len(unique_combinations)):  # перебор всех комбинаций
    print(f"{i+1}. {unique_combinations[i]}")  # вывод каждой комбинации

# пользователь вводит целое число
user_input = input("\nВведите целое число: ")  # ввод числа как строки
user_number = int(user_input)  # преобразование строки в целое число

# вычисление количества пар с суммой меньше заданного числа
count = 0  # счетчик подходящих пар
suitable_pairs = []  # список для хранения подходящих пар

for pair in unique_combinations:  # перебор всех уникальных комбинаций
    total = pair[0] + pair[1]  # вычисление суммы пары
    if total < user_number:  # проверка условия
        count += 1  # увеличение счетчика
        suitable_pairs.append(pair)  # добавление пары в список

print(f"\nКоличество пар с суммой меньше {user_number}: {count}")  # вывод результата

if count > 0:  # проверка наличия подходящих пар
    print("Эти пары:")  # вывод заголовка
    for i in range(len(suitable_pairs)):  # перебор подходящих пар
        pair = suitable_pairs[i]  # получение текущей пары
        total = pair[0] + pair[1]  # вычисление суммы
        print(f"{i+1}. {pair} (сумма: {total})")  # вывод пары и суммы
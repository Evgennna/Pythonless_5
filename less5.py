# 1. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def split_file_path(path):
    dir_path, full_filename = path.rsplit("/", 1)

    name, file_ext = full_filename.split(".", 1)

    return dir_path, name, f".{file_ext}"


file_path = '/home/user/documents/example.txt'
directory, filename, file_extension = split_file_path(file_path)
print("Путь файла:", directory)
print("Имя файла:", filename)
print("Расширение файла:", file_extension)


# 2. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

def generate_bonus_dict(names, rates, bonuses):
    return {name: rate * float(bonus.rstrip("%")) / 100
            for name, rate, bonus in zip(names, rates, bonuses)}


list_names = ["Alice", "Bob", "Charlie"]
list_rates = [1000, 2000, 1500]
list_bonuses = ["10.25%", "5.50%", "12.75%"]

result_dict = generate_bonus_dict(list_names, list_rates, list_bonuses)
print(result_dict)


# 3. Создайте функцию генератор чисел Фибоначчи
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


num_terms = 10
fibonacci_sequence = list(fibonacci_generator(num_terms))
print(fibonacci_sequence)

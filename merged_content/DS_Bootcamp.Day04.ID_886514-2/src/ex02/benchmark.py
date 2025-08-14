"""
benchmark.py

Сравнение четырех методов извлечения Gmail-адресов:
- обычный цикл с append
- list comprehension
- map
- filter

Скрипт принимает два аргумента:
1. Название метода: loop, list_comprehension, map, filter
2. Количество вызовов: целое число

Пример:
$ ./benchmark.py map 1000000
"""
# 1) Обычный цикл и append
def get_gmails_loop(email_list):
    result = []
    for e in email_list:
        if e.endswith('@gmail.com'):
            result.append(e)
    return result

# 2) List comprehension
def get_gmails_comprehension(email_list):
    return [e for e in email_list if e.endswith('@gmail.com')]

# 3) Map
def get_gmails_map(email_list):
    return list(map(lambda e: e if e.endswith('@gmail.com') else None, email_list))

# 4) Filter
def get_gmails_filter(email_list):
    return list(filter(lambda e: e.endswith('@gmail.com'), email_list))

if __name__ == '__main__':
    import timeit
    import sys

    # Данные
    emails = [
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
        'anna@live.com', 'philipp@gmail.com'] * 5
    
    if len(sys.argv) != 3:
        print("Usage: ./benchmark.py <method> <number>")
        sys.exit(1)

    method_name = sys.argv[1]
    try:
        number = int(sys.argv[2])
    except ValueError:
        print("Second argument must be an integer.")
        sys.exit(1)

    functions = {
        "loop": lambda: get_gmails_loop(emails),
        "lc": lambda: get_gmails_comprehension(emails),
        "map": lambda: get_gmails_map(emails),
        "filter": lambda: get_gmails_filter(emails),
    }

    if method_name not in functions:
        print("Unknown method. Use: loop, list_comprehension(lc), map, filter")
        sys.exit(1)

    t = timeit.timeit(functions[method_name], number=number)
    print(t)

    # Вывод результата работы метода
    result = functions[method_name]()
    print(result)

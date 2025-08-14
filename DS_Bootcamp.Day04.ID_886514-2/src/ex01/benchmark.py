"""
benchmark.py

Сравнение трех методов извлечения Gmail-адресов:
- обычный цикл с append
- list comprehension
- map (создание iterator)

Каждый метод вызывается NUMBER раз, затем определяется самый быстрый и выводятся времена в порядке возрастания.
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

# 3) Map: возвращает iterator
def get_gmails_map(email_list):
    return list(map(lambda e: e if e.endswith('@gmail.com') else None, email_list))

if __name__ == '__main__':
    import timeit

    # Данные
    emails = [
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
        'anna@live.com', 'philipp@gmail.com'
    ] * 5
    NUMBER = 5000000 
    # Проверка результатов (map возвращает iterator)
    loop_res = get_gmails_loop(emails)
    comp_res = get_gmails_comprehension(emails)
    map_res = get_gmails_map(emails)
    print(loop_res)
    print()
    print(comp_res)
    print()
    print(map_res)
    print()

    # Замеры
    t_loop = timeit.timeit(lambda: get_gmails_loop(emails), number=NUMBER)
    t_comp = timeit.timeit(lambda: get_gmails_comprehension(emails), number=NUMBER)
    t_map = timeit.timeit(lambda: get_gmails_map(emails), number=NUMBER)

    # Определяем лучшую стратегию
    best = min(t_loop, t_comp, t_map)
    if best == t_map:
        print('it is better to use a map')
    elif best == t_comp:
        print('it is better to use a list comprehension')
    else:
        print('it is better to use a loop')

    # Вывод времени в порядке возрастания
    times = sorted([t_map, t_comp, t_loop])
    print(f"{times[0]} vs {times[1]} vs {times[2]}")
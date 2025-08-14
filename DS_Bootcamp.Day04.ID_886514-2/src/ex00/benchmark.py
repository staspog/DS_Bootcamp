# Функция с обычным циклом и append
def get_gmails_loop(email_list):
    result = []
    for email in email_list:
        # Проверяем окончание строки на нужный домен
        if email.endswith('@gmail.com'):
            result.append(email)
    return result

def get_gmails_comprehension(email_list):
    return [email for email in email_list if email.endswith('@gmail.com')]

if __name__ == '__main__':
    import timeit
    # Исходный список уникальных адресов
    base_emails = [
        'john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
        'anna@live.com', 'philipp@gmail.com'
    ]

    # Дублируем каждый элемент 5 раз, чтобы получить 25 адресов (5 уникальных)
    emails = base_emails * 5
    NUMBER = 500000

    loop_result = get_gmails_loop(emails)
    comp_result = get_gmails_comprehension(emails)
    print(loop_result)
    print()
    print(comp_result)
    print()

    # Измерение времени: передаём callable напрямую, без globals=globals()
    loop_time = timeit.timeit(lambda: get_gmails_loop(emails), number=NUMBER)
    comp_time = timeit.timeit(lambda: get_gmails_comprehension(emails), number=NUMBER)

    # Сравнение и вывод
    if comp_time <= loop_time:
        print('it is better to use a list comprehension')
    else:
        print('it is better to use a loop')
    print(f"{min(loop_time, comp_time)} vs {max(loop_time, comp_time)}")

# Работает быстрее так как выделяет память сразу размера len(emails),
# а не увеличивает по кусочку через for + append
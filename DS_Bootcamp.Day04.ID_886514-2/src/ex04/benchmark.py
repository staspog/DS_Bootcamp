import timeit
import random
from collections import Counter

# 1. Генерация списка случайных чисел от 0 до 100
def generate_data():
    return [random.randint(0, 100) for _ in range(1_000_000)]

# 2. Подсчёт с использованием словаря (без Counter)
def count_with_dict(data):
    counts = {}
    for num in data:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    return counts

# 3. Получение топ-10 самых частых значений (без Counter)
def top_10_with_dict(data):
    counts = count_with_dict(data)
    return dict(sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10])

# 4. Подсчёт с использованием Counter
def count_with_counter(data):
    return Counter(data)

# 5. Топ-10 с использованием Counter
def top_10_with_counter(data):
    return dict(Counter(data).most_common(10))

def main():
    data = generate_data()

    # Подсчёт частот вручную
    t1 = timeit.timeit(lambda: count_with_dict(data), number=1)
    print(f"my function:     {t1:.7f}")

    # Подсчёт частот через Counter
    t2 = timeit.timeit(lambda: count_with_counter(data), number=1)
    print(f"Counter:         {t2:.7f}")

    print()

    # Топ-10 вручную
    t3 = timeit.timeit(lambda: top_10_with_dict(data), number=1)
    print(f"my top:          {t3:.7f}")

    # Топ-10 через Counter
    t4 = timeit.timeit(lambda: top_10_with_counter(data), number=1)
    print(f"Counter's top:   {t4:.7f}")

if __name__ == "__main__":
    main()
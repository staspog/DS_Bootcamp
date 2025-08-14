import sys
import timeit
from functools import reduce

def sum_squares_loop(n):
    """Вычисление суммы квадратов от 1 до n с помощью цикла."""
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

def sum_squares_reduce(n):
    """Вычисление суммы квадратов от 1 до n с помощью reduce."""
    return reduce(lambda acc, x: acc + x * x, range(1, n + 1), 0)

def sum_of_squares_reduce_math(n):
    """Математическая формула: n(n+1)(2n+1)/6."""
    return n * (n + 1) * (2*n + 1) // 6

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./benchmark.py <method> <number_of_calls> <n>")
        print("method: loop, reduce or math")
        sys.exit(1)

    method_name = sys.argv[1]
    try:
        number_of_calls = int(sys.argv[2])
        n = int(sys.argv[3])
    except ValueError:
        print("Number of calls and n must be integers.")
        sys.exit(1)

    if method_name == "loop":
        func = lambda: sum_squares_loop(n)
    elif method_name == "reduce":
        func = lambda: sum_squares_reduce(n)
    elif method_name == "math":
        func = lambda: sum_of_squares_reduce_math(n)
    else:
        print("Unknown method. Use 'loop', 'reduce' or 'math'.")
        sys.exit(1)

    elapsed_time = timeit.timeit(func, number=number_of_calls)
    print(elapsed_time)
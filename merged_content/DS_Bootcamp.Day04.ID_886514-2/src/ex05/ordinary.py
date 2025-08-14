# ordinary.py
import sys
import time

if sys.platform == "win32":
    import psutil
else:
    import resource


def read_all_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines


def measure():
    start_time = time.process_time()
    data = read_all_lines(sys.argv[1])
    for _ in data:
        pass
    cpu_time = time.process_time() - start_time

    if sys.platform == "win32":
        process = psutil.Process()
        mem = process.memory_info().peak_wset / (1024 ** 3)  # GB
    else:
        mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        mem = mem / (1024 ** 2)  # GB (Linux reports in KB)

    print(f"Peak Memory Usage = {mem:.3f} GB")
    print(f"User Mode Time + System Mode Time = {cpu_time:.2f}s")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ordinary.py <file_path>")
        sys.exit(1)
    measure()
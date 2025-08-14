#!/bin/bash

# Профилирование оригинального скрипта (с time.sleep)
python -m cProfile -s tottime financial.py MSFT "Total Revenue" > profiling-sleep.txt

# Профилирование оптимизированного скрипта (без sleep)
python -m cProfile -s tottime financial_enhanced.py MSFT "Total Revenue" > profiling-tottime.txt

# Профилирование HTTP-запросов в enhanced версии
python -m cProfile -s tottime financial_enhanced.py MSFT "Total Revenue" > profiling-http.txt

# Профилирование по количеству вызовов
python -m cProfile -s ncalls financial_enhanced.py MSFT "Total Revenue" > profiling-ncalls.txt

# Создание stats файла для pstats
python -m cProfile -o profile.stats financial_enhanced.py F "Other Income Expense"

# Анализ через pstats (топ-5 по cumtime)
python -c "import pstats; p = pstats.Stats('profile.stats'); p.strip_dirs().sort_stats('cumtime').print_stats(5)" > pstats-cumulative.txt
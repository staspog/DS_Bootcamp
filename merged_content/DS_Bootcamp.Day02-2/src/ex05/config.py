num_of_steps = 3  # Количество шагов для predict_random()

report_template = """Отчёт

Мы провели {observations} наблюдений за подбрасыванием монеты: из них орёл: {tails}, решка: {heads}. Вероятности составляют {tails_pct:.2f}% и {heads_pct:.2f}% соответственно. Наш прогноз на следующие {n} наблюдений: {predicted_tails} орлов и {predicted_heads} решек.
"""
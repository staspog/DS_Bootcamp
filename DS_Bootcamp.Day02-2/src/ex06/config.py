import logging

num_of_steps = 3  # Количество шагов для predict_random()

TELEGRAM_WEBHOOK_URL = "https://api.telegram.org/bot7609817296:AAFlJ7ce8oRJXX05PuMbSyk2H3ahcYEK3Bs/sendMessage"
TELEGRAM_CHAT_ID = "461090709"

LOG_FILE = "analytics.log"
LOG_FORMAT = "%(asctime)s %(message)s"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format=LOG_FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S"
)

report_template = """Отчёт

Мы провели {observations} наблюдений за подбрасыванием монеты: из них орёл: {tails}, решка: {heads}. Вероятности составляют {tails_pct:.2f}% и {heads_pct:.2f}% соответственно. Наш прогноз на следующие {n} наблюдений: {predicted_tails} орлов и {predicted_heads} решек.
"""
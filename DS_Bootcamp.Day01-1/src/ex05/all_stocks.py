import sys

def all_stocks():

    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    # Проверяем количество аргументов
    if len(sys.argv) != 2:
        return  # Завершаем программу, если аргументов нет или их больше одного

    # Создаем обратный словарь для поиска по тикеру
    REVERSE_COMPANIES = {symbol: name for name, symbol in COMPANIES.items()}

    # Получаем строку с выражениями
    input_string = sys.argv[1]

    # Разделяем строку по запятым и удаляем лишние пробелы
    expressions = [expr.strip() for expr in input_string.split(',')]

    # Проверяем, есть ли две запятые подряд или пробелы между запятыми
    if '' in expressions:
        return  # Завершаем программу, если есть пустые выражения


    for expr in expressions:
        # Приводим выражение к верхнему регистру для унификации
        expr_upper = expr.upper()

        # Проверяем, является ли выражение тикером
        if expr_upper in REVERSE_COMPANIES:
            company_name = REVERSE_COMPANIES[expr_upper]
            print(f"{expr_upper} is a ticker symbol for {company_name}")
        # Проверяем, является ли выражение названием компании
        elif expr.capitalize() in COMPANIES:
            ticker = COMPANIES[expr.capitalize()]
            stock_price = STOCKS.get(ticker)
            print(f"{expr.capitalize()} stock price is {stock_price}")
        else:
            print(f"{expr} is an unknown company or an unknown ticker symbol")

if __name__ == '__main__':
    all_stocks()
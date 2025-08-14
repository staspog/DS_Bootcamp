import sys

def get_company_and_price(ticker):

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

    """
    Возвращает название компании и цену акций по тикеру.
    Если тикер неизвестен, возвращает (None, None).
    """
    # Приводим тикер к верхнему регистру (для унификации)
    ticker = ticker.upper()

    # Ищем название компании по тикеру
    company_name = None
    for name, symbol in COMPANIES.items():
        if symbol == ticker:
            company_name = name
            break

    # Получаем цену акций
    stock_price = STOCKS.get(ticker)

    return company_name, stock_price

def main():
    # Проверяем количество аргументов
    if len(sys.argv) != 2:
        return

    # Получаем тикер из аргументов командной строки
    ticker = sys.argv[1]

    # Получаем название компании и цену акций
    company_name, stock_price = get_company_and_price(ticker)

    if company_name and stock_price:
        print(f"{company_name} {stock_price}")
    else:
        print("Unknown ticker")

if __name__ == '__main__':
    main()
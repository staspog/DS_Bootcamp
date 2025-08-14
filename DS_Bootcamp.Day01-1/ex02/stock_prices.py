import sys

def get_stock_price(company_name):

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
    Возвращает цену акций компании или None, если компания неизвестна.
    """
    # Приводим название компании к стандартному виду (с заглавной буквы)
    company_name = company_name.capitalize()

    # Получаем тикер компании из словаря COMPANIES
    ticker = COMPANIES.get(company_name)

    # Если тикер найден, возвращаем цену акций из словаря STOCKS
    return STOCKS.get(ticker)

def main():   
    # Проверяем количество аргументов
    if len(sys.argv) != 2:
        return
    
    # Получаем название компании из аргументов командной строки
    company_name = sys.argv[1]

    # Получаем цену акций
    stock_price = get_stock_price(company_name)

    if stock_price is not None:
        print(stock_price)
    else:
        print("Unknown company")

if __name__ == '__main__':
    main()
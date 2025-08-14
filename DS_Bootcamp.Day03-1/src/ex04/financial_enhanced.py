import sys
import httpx
from bs4 import BeautifulSoup
import re

def validate_arguments():
    if len(sys.argv) != 3:
        raise ValueError("Expected exactly two arguments: ticker and field")
    return sys.argv[1], sys.argv[2]

def create_url(ticker):
    return f"https://finance.yahoo.com/quote/{ticker}/financials/"

def fetch_page(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    with httpx.Client(http2=True) as client:
        try:
            response = client.get(url, headers=headers)
            response.raise_for_status()
            return response
        except httpx.HTTPStatusError as e:
            raise Exception(f"HTTP error: {e}")

def parse_html(response):
    return BeautifulSoup(response.text, 'html.parser')

def find_field_values(soup, target_field):
    # Находим заголовок строки с нужным title, в который входит target_field
    row_title = soup.find('div', class_='rowTitle', title=lambda x: x and target_field in x)
    if not row_title:
        raise ValueError(f"Field '{target_field}' not found")

    # Находим родительский контейнер всей строки (должен быть div с классом 'row')
    row = row_title.find_parent('div', class_=lambda x: x and 'row' in x.split())
    if not row:
        raise ValueError("Row container not found")

    # Извлекаем все колонки с числами
    values = []
    for column in row.find_all('div', class_=lambda x: x and 'column' in x.split() and 'sticky' not in x.split()):
        text = column.get_text(strip=True)
        # Извлекаем число с запятыми
        if any(char.isdigit() for char in text):
            values.append(text)

    if not values:
        raise ValueError(f"No numeric values found for '{target_field}'")

    return values

def print_result(field_name, values):
    print(tuple([field_name] + values))

def main():
    try:
        ticker, field = validate_arguments()
        url = create_url(ticker)
        response = fetch_page(url)
        soup = parse_html(response)
        values = find_field_values(soup, field)
        print_result(field, values)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
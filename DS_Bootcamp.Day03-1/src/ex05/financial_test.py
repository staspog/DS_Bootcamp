import pytest
import requests
import sys
from bs4 import BeautifulSoup
import httpx
from financial import (
    validate_arguments,
    create_url,
    fetch_page,
    parse_html,
    find_field_values,
    print_result
)

# Тесты для validate_arguments()
def test_validate_arguments_correct():
    sys.argv = ["financial.py", "MSFT", "Total Revenue"]
    assert validate_arguments() == ("MSFT", "Total Revenue")

def test_validate_arguments_too_few():
    sys.argv = ["financial.py", "MSFT"]
    with pytest.raises(ValueError):
        validate_arguments()

def test_validate_arguments_too_many():
    sys.argv = ["financial.py", "MSFT", "Revenue", "Extra"]
    with pytest.raises(ValueError):
        validate_arguments()

# Тесты для create_url()
def test_create_url_format():
    assert create_url("MSFT") == "https://finance.yahoo.com/quote/MSFT/financials/"

def test_create_url_special_chars():
    assert create_url("BRK-B") == "https://finance.yahoo.com/quote/BRK-B/financials/"

# Тесты для fetch_page() (с моками)
@pytest.fixture
def mock_response():
    class MockResponse:
        text = "<html><body>Test</body></html>"
        status_code = 200
    return MockResponse()

def test_fetch_page_success(monkeypatch):
    class MockResponse:
        text = "<html><div class='rowTitle' title='Total Revenue'>Test</div></html>"
        status_code = 200
        
        def raise_for_status(self):
            if 400 <= self.status_code < 600:
                raise requests.exceptions.HTTPError("Mocked error")

    def mock_get(*args, **kwargs):
        return MockResponse()
    
    monkeypatch.setattr(requests, "get", mock_get)
    
    response = fetch_page("https://test.com")
    assert response.text == MockResponse.text

def test_fetch_page_404(monkeypatch):
    def mock_get(*args, **kwargs):
        raise httpx.HTTPStatusError("404")
    monkeypatch.setattr(httpx.Client, "get", mock_get)
    with pytest.raises(Exception):
        fetch_page("https://invalid.com")

# Тесты для parse_html()
def test_parse_html_valid():
    class Response:
        text = "<div>Test</div>"
    soup = parse_html(Response())
    assert isinstance(soup, BeautifulSoup)
    assert soup.find("div").text == "Test"

# Тесты для find_field_values()
# Фикстура - это объект, который можно рассматривать, как набор условий необходимых
# тесту для выполнения, например, зачастую фикстуры создаются, чтобы генерировать
# какие-то данные еще до теста и возвращать их для использования в тесте или перед тестом
@pytest.fixture
def mock_soup():
    html = """
    <div class="row">
        <div class="rowTitle" title="Total Revenue">Total Revenue</div>
        <div class="column">100,000</div>
        <div class="column alt">200,000</div>
    </div>
    """
    return BeautifulSoup(html, "html.parser")
# 

def test_find_field_values_valid(mock_soup):
    values = find_field_values(mock_soup, "Total Revenue")
    assert values == ["100,000", "200,000"]

def test_find_field_values_missing_field(mock_soup):
    with pytest.raises(ValueError):
        find_field_values(mock_soup, "Invalid Field")

# Тесты для print_result()
def test_print_result(capsys):
    print_result("Test", ["1", "2"])
    captured = capsys.readouterr()
    assert captured.out == "('Test', '1', '2')\n"

# Интеграционные тесты
def test_main_valid(monkeypatch, capsys):
    def mock_fetch(url):
        class MockResponse:
            text = "<html>...mock data...</html>"
        return MockResponse()
    
    monkeypatch.setattr(httpx.Client, "get", lambda *args, **kwargs: mock_fetch())
    sys.argv = ["financial.py", "MSFT", "Total Revenue"]
    from financial import main
    main()
    captured = capsys.readouterr()
    assert "Total Revenue" in captured.out

def test_main_invalid_ticker(capsys):
    sys.argv = ["financial.py", "INVALID", "Total Revenue"]
    from financial import main
    with pytest.raises(ValueError):
        main()
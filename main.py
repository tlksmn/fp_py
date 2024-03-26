# Разработка Функционального Веб-Скрапера
# - Создать веб-скрапер, использующий функциональные подходы для анализа и
# извлечения данных с веб-страниц.

from requests_html import HTMLSession
from requests import get

sessionCurrency = HTMLSession()

response = sessionCurrency.get("https://www.mig.kz")
html = response.html

title = html.find('title', first=True).text
print(title)

currencies = html.find('tr')
for tableRow in currencies:
    try:
        currencyText = tableRow.find("td.currency", first=True).text
        currencyBuy = tableRow.find("td.buy", first=True).text
        currencySell = tableRow.find("td.buy", first=True).text
        print(f"Курс {currencyText} продажа {currencyBuy} покупка {currencySell}")
    except AttributeError:
        pass



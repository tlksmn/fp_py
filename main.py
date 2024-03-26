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


responseApi = get("https://api.openweathermap.org/data/2.5/weather?q=Almaty,kz&appid=ae6ec9f4ddc82a04dbf98477ba7dc0ac")

if responseApi.status_code == 200:
    res = responseApi.json()
    weather = res['weather'][0]
    main = res['main']
    print("\n\n")
    print(f"{weather['main']} - {weather['icon']};")
    print("Температура")
    print(f"ощущение({main['feels_like'] - 273.15})")
    print(f"прибор({main['temp'] - 273.15})")
    print(f"минимальное({main['temp_min'] - 273.15})")
    print(f"максимальное({main['temp_max'] - 273.15})")
    print(f"видимость({res['visibility']})")
    print(res)
else:
    print(responseApi.status_code)
from bs4 import BeautifulSoup
import requests

source = requests.get(
    'https://weather.com/weather/today/l/USWA0027:1:US').text
thing = BeautifulSoup(source, "html.parser")
temperature = thing.find('div', class_='today_nowcard-temp').span.text
print(temperature)

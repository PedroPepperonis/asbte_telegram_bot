import requests
from bs4 import BeautifulSoup


URL = 'https://asb.te.ua/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def check_last_car(url):
    with open('last_car.txt', 'r') as f:
        last_url = f.readline()
        if last_url == url:
            return False
    with open('last_car.txt', 'w') as f:
        for i in url:
            f.write(i)
        return True


def get_car_data():
    data = ''
    url = ''

    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('div', class_='catalog__content')

    for item in items:
        data += f"{item.find('h3').get_text()}\n" \
                f"Цена: {item.find('h4', class_='catalog__card-price').get_text()}\n" \
                f"Ссылка: {URL}{item.find('a').get('href')}\n" \
                f""
        url = f"{item.find('a').get('href')}"

    if check_last_car(url):
        return data

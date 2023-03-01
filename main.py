import requests
from bs4 import BeautifulSoup

url = 'https://pwdr.ru/futbolka-pwdr-skitour-boarder-uniseks-molochnaya/?sku=1463675'

def listen_kafka():
    pass

def parser(url): # получает ссылку на страницу товара
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.content)
    data = soup.find("div", id="product-core-image")
    src_image = data.find("img")['src']
    http_image = 'https://pwdr.ru' + src_image
    return http_image # возращает ссылку на товар

def send_to_kafka():
    pass

# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    while(True):
        prod_url = listen_kafka()



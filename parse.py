from bs4 import BeautifulSoup
import requests


class Parser:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        mains = self.html.find_all('div', class_='good_block')
        for item in mains:
            func = item.find('div', class_='functional').text
            href = self.url + item.find('a').get('href')
            title = item.find('span', class_='title').text
            price = item.find('div', class_='price3').text
            self.res.append({'func': func, 'title': title, 'price': price, 'href': href})
        # print(self.res)

    def save(self):
        with open(self.path, 'w') as f:
            i = 1
            for item in self.res:
                f.write(f'Аппарат №{i}\n\nНазвание:{item["func"]}\n'
                        f'Модель:{item["title"]}\n'
                        f'Цена:{item["price"]}\n'
                        f'Ссылка:{item["href"]}\n'
                        f"\n{'='* 45}\n\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()

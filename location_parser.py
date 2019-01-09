import requests
from bs4 import BeautifulSoup as bs  # Такая запись позволяет обернуть BeautifulSoup в bs
import time
from tqdm import tqdm



def give_me_html(url):

    https_proxy = "144.217.22.128:8080"


    proxyDict = {
        "https": https_proxy,
    }

    headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5'}
    session = requests.Session()  # Иметирует сессию клиента.
    #request = session.get(url, headers=headers, proxies=proxyDict)
    request = session.get(url, headers=headers)
    return request.content




def find_data():
    with open('/home/moonz/PycharmProjects/BeautifulSoup/venv/users.txt', 'r') as file:
        num = (sum(1 for _ in file))  # Считаем сколько ссылок(строк) в файле.
        #  Не знаю почему НО, данная реализация после считывания забирает в себя все данные.

    with open('/home/moonz/PycharmProjects/BeautifulSoup/venv/users.txt', 'r') as file:

        for i in tqdm(range(num)):  # Прогрессбар для наглядности :3

            url = file.readline()
            html = give_me_html(url.replace('\n',''))

            soup = bs(html, 'html.parser')
            location = soup.find('div', id='aboutme-personal-info')
            # На будущи, что бы собрать и города.
            location_more = soup.find('table', class_='f')
            if location != None:
                data = location.text
                if data != None and data.istitle() == True:  # Проверяем не пустота ли вместо страны.
                    # Данный метод реализует проверку на заглавную букву, были ситуации когда записывал пустоту.
                    #  Велосепед который забирает ужасный текст, а отадёт прекрсный :3
                    b = location.text.split()  # Полученная строка имеет отступы, проблемы, и что-то ещё. Убираем лишнее
                    c = ' '.join(b)  # В связи с тем что метод выше возвращает список, делаем из него строку.
                    with open('user_locatin.txt', 'a') as files:
                        files.writelines(c + '\n')

                time.sleep(2)



find_data()

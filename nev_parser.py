from selenium import webdriver
import time
from bs4 import BeautifulSoup
from tqdm import tqdm
"""Данная конфигурация реализует базовую настройку с использованием профиля пользователя """

PROXY = '144.217.163.93:8888'

options = webdriver.ChromeOptions()
options.add_argument('headless')  # Без GUI
options.add_argument(r"user-data-dir=/home/moonz/chrome/profile")
#options.add_argument('--proxy-server=%s' % PROXY)
driver = webdriver.Chrome(executable_path="/home/moonz/chrome/chromedriver", chrome_options=options)


# Чистим закладки

def start():
    time.sleep(2)  # Ждём загрузку
    for i in range(20):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    #  Реализуем сбор загруженных данных.
    soup = BeautifulSoup(driver.page_source, 'html.parser')  # На вход сразу подаём html из selenium
    test = soup.find(id='browse-results-page-1').find_all(class_='artist')
    adders = int(0)
    for sup in test:  # Реализуем проверку каждой ссылки на наличие её в Уже сформированном листе.
        try:
            user = sup.find('a').get('href')
            with open('links.txt', 'r') as filter_file:
                copy = filter_file.readlines()
                if str(user + '\n') not in copy:
                    with open('links.txt', 'a') as file:
                        file.writelines(user + '\n')
                        adders += 1

        except Exception as error:
            continue
    print('Было давлено ссылок: ',adders)

try:
    for i in tqdm(range(100)):
        driver.get("https://www.deviantart.com/newest/")
        start()
        driver.get("https://www.deviantart.com/photography/newest/")
        start()
        driver.get("https://www.deviantart.com/fanart/newest/")
        start()
        driver.get("https://www.deviantart.com/manga/newest/")
        start()
        time.sleep(200)


except Exception as er:
    print(er)

finally:
    driver.close()
    time.sleep(2)
    driver.quit()
    time.sleep(2)


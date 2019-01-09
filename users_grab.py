from selenium import webdriver
import time
"""Данная конфигурация реализует базовую настройку с использованием профиля пользователя """

from tqdm import tqdm
import progressbar

options = webdriver.ChromeOptions()
options.add_argument('headless')  # Без GUI
options.add_argument(r"user-data-dir=/home/moonz/chrome/profile")
driver = webdriver.Chrome(executable_path="/home/moonz/chrome/chromedriver", chrome_options=options)
# driver.page_source


driver.get("https://www.deviantart.com/newest/")

driver.find_element_by_xpath("//a[@class='torpedo-thumb-link']").click()
time.sleep(1)

progress = progressbar.ProgressBar()

def clean():
    try:
        for i in range(1,50):
            a = driver.find_element_by_xpath \
                ("//div[@class='dev-view-about']").find_element_by_xpath("//span[@class='dev-title-avatar']") \
                .find_element_by_css_selector('a').get_attribute('href')
            time.sleep(2)
            with open('links.txt', 'r+') as c:
                prov = c.readlines()  # Читаем все строки.
                if str(a + '\n') not in prov:  # Реализуем проверку вхождений линка в списке.
                    c.writelines(a + '\n')
                else:
                    driver.find_element_by_xpath("//img[@alt='Right']").click()
            driver.find_element_by_xpath("//img[@alt='Right']").click()
            time.sleep(1)

        driver.get("https://www.deviantart.com/newest/")
        time.sleep(1)

        driver.find_element_by_xpath("//a[@class='torpedo-thumb-link']").click()
        time.sleep(1)

    except Exception as error:
        print('ОШИБКА ! | ', error)
        driver.find_element_by_xpath("//img[@alt='Right']").click()
        time.sleep(1)


try:
    # for i in progress(range(1,100)):
    for x in tqdm(range(1,1000)):
        clean()



except Exception as er:
    print(er)
    driver.get("https://www.deviantart.com/newest/")



finally:
    driver.close()
    time.sleep(2)
    driver.quit()
    time.sleep(2)


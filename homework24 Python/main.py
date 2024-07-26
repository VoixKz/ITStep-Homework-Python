from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import Workbook
import time

edge = webdriver.Edge()
edge.get('https://yandex.kz/pogoda/astana?via=reg')

temperature = edge.find_element(By.CLASS_NAME, 'temp__value').text
sky_status = edge.find_element(By.CLASS_NAME, 'link__condition').text
wind = edge.find_element(By.CLASS_NAME, 'fact__wind-speed').text
humidity = edge.find_element(By.CLASS_NAME, 'fact__humidity').text
pressure = edge.find_element(By.CLASS_NAME, 'fact__pressure').text
with open('./homework24 Python/weather.txt', 'w', encoding='utf-8') as file:
    file.write(f'''
Температура воздуха: {temperature}°С
Состояние неба: {sky_status}
Скорость ветра: {wind} напрвления
Влажность: {humidity}
Давление: {pressure}
    ''')



edge.get('https://www.technodom.kz/astana/catalog/smartfony-i-gadzhety/gadzhety/smart-chasy/f/brands/apple')
edge.find_element(By.CLASS_NAME, 'CitiesList_name__6yw7D').click()
time.sleep(5)
workbook = Workbook()
worksheet = workbook.active
worksheet.append(['Наименование', 'Цена'])
goods = edge.find_elements(By.CSS_SELECTOR, '[data-testid="product-card"]')
print(len(goods))
for good in goods:
    print('-------------------')
    print(good.find_element(By.CSS_SELECTOR, '[data-testid="product-title"]').text)
    print(good.find_element(By.CSS_SELECTOR, '[data-testid="product-price"]').text)
    worksheet.append([good.find_element(By.CSS_SELECTOR, '[data-testid="product-title"]').text,
                      good.find_element(By.CSS_SELECTOR, '[data-testid="product-price"]').text])
workbook.save('./homework24 Python/goods.xlsx')
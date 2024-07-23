import requests
import os
import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def download_image(session, url, image_number):
    async with session.get(url) as response:
        with open(f"homework23 Python/folder_aiohttp/image_{image_number}.jpg", "wb") as file:
            while True:
                chunk = await response.content.read(1024)
                if not chunk:
                    break
                file.write(chunk)

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        tasks.append(download_image(session, image_url, ind+1))
        await asyncio.gather(*tasks)

os.makedirs("homework23 Python/folder_requests", exist_ok=True)
os.makedirs("homework23 Python/folder_aiohttp", exist_ok=True)

site_url = "https://fonwall.ru/"
soup = BeautifulSoup(requests.get(site_url).text, "html.parser")
imgs = soup.find_all("img")
for ind, img in enumerate(imgs):
    if ind > 9:
        break
    image_url = img["src"]
    print(ind+1, image_url)
    response = requests.get(image_url)
    with open(f"homework23 Python/folder_requests/image_{ind+1}.jpg", "wb") as file:
        file.write(response.content)
    
    asyncio.run(main())



url = "https://tengrinews.kz/weather/astana/day/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
weather_element = soup.find('div', class_='weather-city')

location = soup.find('h1', class_='head-single').text.strip()
temperature = weather_element.find('p', class_='weather-city-all-temp-value').text.strip()
sky_status = weather_element.find('p', class_='testimony-item').text.strip()
additional_info = weather_element.find('div', class_='weather-city-other').find_all('p')
wind = additional_info[0].text.strip()
humidity = additional_info[1].text.strip()
pressure = additional_info[2].text.strip()

print(f'''
Погода в {' '.join(location.split()[2:-1])}
Температура: {temperature}
Состояние неба: {sky_status}
Скорость ветра: {wind}
Влажность: {humidity}
Давление: {pressure}
''')
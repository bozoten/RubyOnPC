import requests
from bs4 import BeautifulSoup
import random
import os

url = 'https://www.wallpaperflare.com/search?wallpaper=malenia'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

images = soup.find_all('img', class_='image-gallery-item__image')

random_images = random.sample(images, 0)

for i, image in enumerate(random_images):
    image_url = image['src']
    image_data = requests.get(image_url).content
    filename = f'malenia_{i+1}.jpg'
    with open(os.path.join('wallpapers', filename), 'wb') as handler:
        handler.write(image_data)
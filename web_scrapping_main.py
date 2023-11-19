from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import numpy as np

area = []
sq_meters = []
room_number = []
price = []
for i in range(1, 31):
    webpage_response = requests.get("https://www.halooglasi.com/nekretnine/izdavanje-stanova/beograd?page=" + str(i))

    webpage = webpage_response.text

    soup = BeautifulSoup(webpage, 'html.parser')
    product_titles = soup.find_all(class_='product-title')

    href_texts = [product_title.a['href'] for product_title in product_titles if product_title.a]
    for href_text in href_texts:
        link = "https://www.halooglasi.com" + href_text
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(link)
        html = driver.page_source
        driver.quit()
        soup1 = BeautifulSoup(html, 'html.parser')
        try: 
            opstina = soup1.find(id='plh3').get_text(strip=True)
            area.append(opstina)
            print(opstina)
            kvadratura = soup1.find(id='plh11').get_text(strip=True)
            sq_meters.append(kvadratura)
            broj_soba = soup1.find(id='plh12').get_text(strip=True)
            room_number.append(broj_soba)
            cena = soup1.find(id='plh6').get_text(strip=True)
            price.append(cena)
        except:
            area.append(np.nan)
            sq_meters.append(np.nan)
            room_number.append(np.nan)
            price.append(np.nan)
            continue
        print(cena)


df = pd.DataFrame({
    'area' : area,
    'sq_meters' : sq_meters,
    'room_number' : room_number,
    'price' : price
})
df.to_excel('Cene stanova.xlsx', index=False)
print(df)
print("GOTOVO!")
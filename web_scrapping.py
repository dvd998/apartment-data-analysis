from bs4 import BeautifulSoup
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import numpy as np

area = []
sq_meters = []
room_number = []
price = []
heating = []
floors = []
total_floors = []
for i in range(1, 31):
    url = "https://www.halooglasi.com/nekretnine/izdavanje-stanova/beograd?cena_d_from=250&cena_d_to=1500&cena_d_unit=4&page=" + str(i)
    driver = webdriver.Chrome()
    driver.get(url)
    product_titles = driver.find_elements(By.CLASS_NAME, 'product-title')
    href_texts = [product_title.find_element(By.TAG_NAME, 'a').get_attribute('href') for product_title in product_titles]
    for href_text in href_texts:
        driver.get(href_text)
        html = driver.page_source
        soup1 = BeautifulSoup(html, 'html.parser')
        try: 
            opstina = soup1.find(id='plh3').get_text(strip=True)
            area.append(opstina)
        except:
            area.append(np.nan)
        try:
            kvadratura = soup1.find(id='plh11').get_text(strip=True)
            sq_meters.append(kvadratura)
        except:
            sq_meters.append(np.nan)
        try:
            broj_soba = soup1.find(id='plh12').get_text(strip=True)
            room_number.append(broj_soba)
        except:
            room_number.append(np.nan)
        try:
            cena = soup1.find(id='plh6').get_text(strip=True)
            price.append(cena)
        except:
            price.append(np.nan)
        try:
            heat = soup1.find(id='plh17').get_text(strip=True)
            heating.append(heat)
        except:
            heating.append(np.nan)
        try:
            floor = soup1.find(id='plh18').get_text(strip=True)
            floors.append(floor)
        except:
            floors.append(np.nan)
        try:
            total_floor = soup1.find(id='plh19').get_text(strip=True)
            total_floors.append(total_floor)
        except:
            total_floors.append(np.nan)
    driver.quit()

df = pd.DataFrame({
    'area' : area,
    'sq_meters' : sq_meters,
    'room_number' : room_number,
    'price' : price,
    'heating' : heating,
    'floor' : floors,
    'total_floors' : total_floors
})
df.to_excel('Data 26.11.2023..xlsx', index=False)
print(df)
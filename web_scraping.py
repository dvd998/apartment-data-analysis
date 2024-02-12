
### Webscraping of https://www.halooglasi.com/ ###
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import numpy as np
from datetime import *

areas = []
sq_meters = []
room_numbers = []
prices = []
heatings = []
floors = []
total_floors = []
for i in range(1, 21):
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
            area = soup1.find(id='plh3').get_text(strip=True)
            areas.append(area)
        except:
            areas.append(np.nan)
        try:
            sq_meter = soup1.find(id='plh11').get_text(strip=True)
            sq_meters.append(sq_meter)
        except:
            sq_meters.append(np.nan)
        try:
            room_number = soup1.find(id='plh12').get_text(strip=True)
            room_numbers.append(room_number)
        except:
            room_numbers.append(np.nan)
        try:
            price = soup1.find(id='plh6').get_text(strip=True)
            prices.append(price)
        except:
            prices.append(np.nan)
        try:
            heat = soup1.find(id='plh17').get_text(strip=True)
            heatings.append(heat)
        except:
            heatings.append(np.nan)
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
    'area' : areas,
    'sq_meters' : sq_meters,
    'room_number' : room_numbers,
    'price' : prices,
    'heating' : heatings,
    'floor' : floors,
    'total_floors' : total_floors
})
today = today = datetime.now().strftime("%d.%m.%y.")
df.to_excel(f'Excel_files\\Data {today}.xlsx', index=False)
print(df)
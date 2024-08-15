import pandas as pd
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import numpy as np

BASE_URL = "https://www.nekretnine.rs/stambeni-objekti/stanovi/izdavanje-prodaja/izdavanje/grad/beograd/cena/1_1500/lista/po-stranici/10/stranica/"

def fetch_apartment_links(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')
    links = [link.get('href') for link in doc.select('.offer-title.text-truncate.w-100 a')]

    return links

def scrape_apartment_data(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    area = soup.find(class_="stickyBox__Location").get_text(strip=True) \
        if soup.find(class_="stickyBox__Location") else np.nan
    sq_meter = soup.find(lambda tag: tag.name == 'span' and "Kvadratura:" in tag.text).find_next('br').next_sibling.get_text(strip=True) \
        if soup.find(lambda tag: tag.name == 'span' and "Kvadratura:" in tag.text).find_next('br').next_sibling else np.nan
    room_num = soup.find(lambda tag: tag.name == 'span' and "Sobe:" in tag.text).find_next('br').next_sibling.get_text(strip=True) \
        if soup.find(lambda tag: tag.name == 'span' and "Sobe:" in tag.text).find_next('br').next_sibling else np.nan
    price = soup.find(class_="stickyBox__price").get_text(strip=True).split('EUR')[0].strip() \
        if soup.find(class_="stickyBox__price") else np.nan
    heating = soup.find(lambda tag: tag.name == 'span' and "Grejanje:" in tag.text).find_next('br').next_sibling.get_text(strip=True) \
        if soup.find(lambda tag: tag.name == 'span' and "Grejanje:" in tag.text).find_next('br').next_sibling else np.nan
    floor_text = soup.find(lambda tag: tag.name == 'span' and "Sprat:" in tag.text).find_next('br').next_sibling.get_text(strip=True).split("/") \
        if soup.find(lambda tag: tag.name == 'span' and "Sprat:" in tag.text).find_next('br').next_sibling else np.nan
    floor = floor_text[0] if len(floor_text) == 2 else np.nan
    #floor, total_floor = floor_text if len(floor_text) == 2 else (None, None)
    
    return {'area': area, 'sq_meters': sq_meter, 'room_number': room_num, 'price': price, 'heating': heating, 'floor': floor}

def scrape_data():
    areas, sq_meters, room_numbers, prices, heatings, floors = [], [], [], [], [], []
    for i in range(1, 31):
        print(f"Currently at page: {i}")
        url = BASE_URL + str(i) if i != 1 else BASE_URL
        apartment_links = fetch_apartment_links(url)
        for link in apartment_links:
            apartment_data = scrape_apartment_data("https://www.nekretnine.rs" + link)
            areas.append(apartment_data['area'])
            sq_meters.append(apartment_data['sq_meters'])
            room_numbers.append(apartment_data['room_number'])
            prices.append(apartment_data['price'])
            heatings.append(apartment_data['heating'])
            floors.append(apartment_data['floor'])
            
    return pd.DataFrame({'area': areas, 'sq_meters': sq_meters, 'room_number': room_numbers, 'price': prices, 'heating': heatings, 'floor': floors})

if __name__ == "__main__":
    df = scrape_data()
    today = datetime.now().strftime("%d.%m.%y.")
    df.to_excel(f'Excel_files\\Data nekretnine {today}.xlsx', index=False)
    print(df)

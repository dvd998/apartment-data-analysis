
### Web scrapping of https://www.nekretnine.rs  ###
import pandas as pd
from bs4 import BeautifulSoup
import requests

areas = []
sq_meters = []
room_numbers = []
prices = []
heatings = []
floors = []
total_floors = []
for i in range(1, 31):
    url = "https://www.nekretnine.rs/stambeni-objekti/stanovi/izdavanje-prodaja/izdavanje/grad/beograd/cena/1_1500/lista/po-stranici/10/" + str(i) + "/"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, 'html.parser')

    elements_with_class = doc.find_all(class_ = "offer-title text-truncate w-100")
    hrefs = []
    for element in elements_with_class:
        link_element = element.find('a')
        if link_element:
            href_value = link_element.get('href')
            print(href_value)
            hrefs.append(href_value)
        # print(str(element.text).strip().lower().replace(" ", "-").replace(",", "-").replace("/", "-"))
 
    for link in hrefs:
        url_app = "https://www.nekretnine.rs" + link
        res = requests.get(url_app)
        print(url_app)
        soup = BeautifulSoup(res.text, 'html.parser')
        area = soup.find(class_ = "stickyBox__Location").text.strip()
        areas.append(area)
        sq = soup.find('span', text = "Kvadratura:")
        sq_meter = sq.find_next('br').next_sibling.strip()
        sq_meters.append(sq_meter)
        print(sq_meter)
        room = soup.find('span', text = "Sobe:")
        room_num = room.find_next('br').next_sibling.strip()
        room_numbers.append(room_num)
        price = soup.find(class_ = "stickyBox__price").text.strip().split('EUR')[0].strip()
        prices.append(price)
        heat = soup.find('span', text = "Grejanje:")
        heating = heat.find_next('br').next_sibling.text.strip()
        heatings.append(heating)
        floor_info = soup.find('span', text = "Sprat:")
        floor_text = floor_info.find_next('br').next_sibling.text.strip()
        floor_text = floor_text.split("/")
        floor = floor_text[0]
        total_floor = floor_text[1]
        floors.append(floor)
        total_floors.append(total_floor)

df = pd.DataFrame({
    'area' : areas,
    'sq_meters' : sq_meters,
    'room_number' : room_numbers,
    'price' : prices,
    'heating' : heatings,
    'floor' : floors,
    'total_floors' : total_floors
})
df.to_excel('Data nekretnine.xlsx', index=False)
print(df)
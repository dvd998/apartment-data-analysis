
# ### Webscraping of https://www.halooglasi.com/ ###
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import numpy as np
from datetime import datetime

# Function to scrape individual page
def scrape_page(url, driver):
    driver.get(url)
    product_titles = driver.find_elements(By.CLASS_NAME, 'product-title')
    href_texts = [product_title.find_element(By.TAG_NAME, 'a').get_attribute('href') for product_title in product_titles]
    data = []
    for href_text in href_texts:
        driver.get(href_text)
        html = driver.page_source
        soup1 = BeautifulSoup(html, 'html.parser')
        area = soup1.find(id='plh3').get_text(strip=True) if soup1.find(id='plh3') else np.nan
        sq_meter = soup1.find(id='plh11').get_text(strip=True) if soup1.find(id='plh11') else np.nan
        room_number = soup1.find(id='plh12').get_text(strip=True) if soup1.find(id='plh12') else np.nan
        price = soup1.find(id='plh6').get_text(strip=True) if soup1.find(id='plh6') else np.nan
        heat = soup1.find(id='plh17').get_text(strip=True) if soup1.find(id='plh17') else np.nan
        floor = soup1.find(id='plh18').get_text(strip=True) if soup1.find(id='plh18') else np.nan
        total_floor = soup1.find(id='plh19').get_text(strip=True) if soup1.find(id='plh19') else np.nan
        data.append({'area': area, 'sq_meters': sq_meter, 'room_number': room_number, 'price': price, 'heating': heat, 'floor': floor, 'total_floors': total_floor})
        print(data)
    return data

def main():
    # Initialize webdriver
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    # Scrape multiple pages
    data = []
    num_pages = 20  # You can also dynamically determine this
    for i in range(1, num_pages + 1):
        url = f"https://www.halooglasi.com/nekretnine/izdavanje-stanova/beograd?cena_d_from=250&cena_d_to=1500&cena_d_unit=4&page={i}"
        data += scrape_page(url, driver)

    driver.quit()

    # Create DataFrame and save to Excel
    df = pd.DataFrame(data)
    today = datetime.now().strftime("%d.%m.%y.")
    df.to_excel(f'Excel_files\\Data {today}.xlsx', index=False)
    print(df)

if __name__ == "__main__":
    main()
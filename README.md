# apartment-data-analysis
Web scrapping of apartment rental website and data analysis

This projects consist of three parts:

**1. Web scrapping**
Using Python libraries Selenium and BeautifulSoup, this part of project is about getting data from one of most visited website for aparment rental in Belgrade, https://www.halooglasi.com/nekretnine/izdavanje-stanova/.
Loop is created to gether apartment data for first 30 pages of the website, on each page there are 20 apartments.
Data that is being collected: area (city area where apartment is located), square meters of apartment, number of rooms and price (monthly fee for renting).
Data is structured as pandas DataFrame and saved as an excel file.

**2. Analysis and visualization**
After data is collected, second part of projects is to take a look at the data.
Cleaning and visualization are done with Pandas, Seaborn and matplotlib Python libraries.

**3. Using machine learning models for predicting**

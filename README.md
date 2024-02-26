# apartment-data-analysis
Web scrapping of apartment rental website in Serbia and data analysis using Python.

This projects consist of three parts:

**1. Web scrapping**
Using Python libraries Selenium and BeautifulSoup, this part of project is about getting data from one of most visited websites for apartment rental in Belgrade, https://www.halooglasi.com/nekretnine/izdavanje-stanova/ and https://www.nekretnine.rs/stambeni-objekti/stanovi
Loop is created to gather apartment data for first 30 pages of the website, on each page there are 20 apartments.
Data that is being collected: area (city area where apartment is located), square meters of apartment, number of rooms and price (monthly fee for renting).
Data is structured as pandas DataFrame and saved as an excel file.

**2. Analysis and visualization**
After data is collected, second part of projects is to take a look at the data.
Cleaning and visualization are done with Pandas, Seaborn and matplotlib Python libraries. 
Correlation matrix is created to identify which variables have big impact on price, so they can be fed to machine learning model.

**3. Using machine learning models for predicting**
Classification algorithms such as Random Forest, K-nearest neighbors and SVM (Support Vector Machine) are used to predict number of rooms for each apartment based on square meters and price.
Regression models such as Multiple Linear Regression and Random Forest Regression are used to predict rent price of apartments.

from wsgiref import headers
from selenium import webdriver
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests
import csv

START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Edge()
browser.get(START_URL)

time.sleep(10)
planets_data = []
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_data", 
          "hyperlink", "planet_type", "planet_type", "planet_radius", "orbital_radius", "eccenticity"]

def scrape():
    for i in range(1,5):
        while True:
            time.sleep(2)
            soup = BeautifulSoup(browser.page_source, "html.parser")
                        # Check page number    
            current_page_num = int(soup.find_all("input", attrs={"class", "page_num"})[0].get("value"))
            if current_page_num < i  :
                 browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
            elif current_page_num >i:
                 browser.find_element(By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a').click()
            else :
                break

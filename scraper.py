from selenium import webdriver 
from bs4 import BeautifulSoup
import time 
import csv


START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

browser = webdriver.Chrome("/Users/shenayaverma/Desktop/python/scraper/chromedriver.exe")

browser.get(START_URL) 

time.sleep(10)
def scrape():
    headers = ['NAME',' LIGHT-YEARS FROM EARTH ', 'PLANET MASS	', ' STELLAR MAGNITUDE	', 'DISCOVERY DATE']
    planet_data = []
    for i in range(0,4):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for a in soup.find_all('ul',attrs={"class", "exoplanet"}):
            list = a.find_all('li')
            temp_list = []
            for index, s in enumerate(list):
                if index = 0:
                    temp_list.append(s.find_all("a")[0].contents[0])
                else:
                    temp_list.append(s.contents[0])
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click() 
with open("scrapper_2.csv", "w") as f: csvwriter = csv.writer(f) 
csvwriter.writerow(headers) 
csvwriter.writerows(planet_data)

                    

scrape()

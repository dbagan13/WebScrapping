from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

from bs4 import BeautifulSoup
import requests
import sys


options = webdriver.FirefoxOptions()
options.add_argument("--incognito")
driver = webdriver.Firefox(executable_path="./geckodriver", options=options)

#driver = webdriver.Chrome('.\chromedriver')

url = "https://www.rottentomatoes.com/browse/dvd-streaming-all/"


driver.get(url)
movie_names = driver.find_elements_by_xpath('//h3[@class="movieTitle"]')
#movies = driver.find_elements_by_xpath('//div[@class="mb_movie"]')
movies = driver.find_elements_by_xpath('//div[@class="movie_info"]//a')
movies_list = []

spans = driver.find_elements_by_xpath('//span')

total_movies = 0
for span in spans:
    if span.text.startswith("Showing"):
        total_movies = int(span.text.split(" ")[-1])
        print(total_movies)

for i in range(len(movies)):
    movie = movies[i]
    movie_dict = {'Title':movie_names[i].text}
    #movie_page = driver.get(movie.get_attribute('href'))
    #movie_info = driver.find_elements_by_xpath('//div[@class="meta-value genre"]')
    movie_url = movie.get_attribute('href')
    page_movie = requests.get(movie_url)
    soup = BeautifulSoup(page_movie.content, "html.parser")
    #SCORES
    tomatometer = soup.find("span", {"class": "mop-ratings-wrap__percentage"})
    audience_score = tomatometer.find_next("span", {"class": "mop-ratings-wrap__percentage"})
    tomatometer = tomatometer.text
    if audience_score != None: audience_score = audience_score.text
    else: audience_score = "NotYetAvailable"
    movie_dict['Tomatometer'] = tomatometer.replace('\n',"").replace(" ","")
    movie_dict['Audience score'] = audience_score.replace('\n',"").replace(" ","")

    #genres = soup.find("div", {"class": "meta-value genre"}).text
    #genres = genres.replace('\n',"").replace(" ","")
    info_items = soup.find_all("li", {"class": "meta-row clearfix"})
    for item in info_items:
        field = item.find(("div", {"class": "meta-value subtle"}))
        field_name = field.text
        value = field.find_next().text.replace('\n',"").replace(" ","")
        movie_dict[field_name[:-1]] = value

    print(movie_dict)

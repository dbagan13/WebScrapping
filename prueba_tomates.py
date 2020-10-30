from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup
import requests
import sys
import time


options = webdriver.FirefoxOptions()
options.add_argument("--incognito")
driver = webdriver.Firefox(executable_path="./geckodriver", options=options)

#driver = webdriver.Chrome('.\chromedriver')

url = "https://www.rottentomatoes.com/browse/dvd-streaming-all/"


driver.get(url)

spans = driver.find_elements_by_xpath('//span')
total_movies = 0
for span in spans:
    if span.text.startswith("Showing"):
        total_movies = int(span.text.split(" ")[-1])
        initial_shown_movies = int(span.text.split(" ")[1])
        show_more_clicks = total_movies/initial_shown_movies

from selenium.webdriver import ActionChains
show_more_button =  driver.find_element_by_xpath('//button[@class="btn btn-secondary-rt mb-load-btn"]')

current_shown_movies = initial_shown_movies
while current_shown_movies < total_movies:
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        ActionChains(driver).move_to_element(show_more_button).perform()
        ActionChains(driver).click(show_more_button).perform()
        current_shown_movies += initial_shown_movies
    except:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        ActionChains(driver).move_to_element(show_more_button).perform()
    print(current_shown_movies)


movie_names = driver.find_elements_by_xpath('//h3[@class="movieTitle"]')
movies = driver.find_elements_by_xpath('//div[@class="movie_info"]//a')
movies_list = []


for i in range(len(movies)):
    movie = movies[i]
    movie_dict = {'Title':movie_names[i].text}
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

    info_items = soup.find_all("li", {"class": "meta-row clearfix"})
    for item in info_items:
        field = item.find(("div", {"class": "meta-value subtle"}))
        field_name = field.text
        value = field.find_next().text.replace('\n',"").replace(" ","")
        movie_dict[field_name[:-1]] = value

    movies_list.append(movie_dict)

print(movies_list)

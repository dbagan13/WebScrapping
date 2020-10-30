import pandas as pd
import requests
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup

# Setting up automated Web Browser used by Selenium
options = webdriver.FirefoxOptions()
options.add_argument("--incognito")
driver = webdriver.Firefox(executable_path="./geckodriver.exe", options=options)

# Web Page to do scrapping
url = "https://www.rottentomatoes.com/browse/dvd-streaming-all/"

driver.get(url)

spans = driver.find_elements_by_xpath('//span')
total_movies = 0
for span in spans:
    if span.text.startswith("Showing"):
        total_movies = int(span.text.split(" ")[-1])
        initial_shown_movies = int(span.text.split(" ")[1])
        show_more_clicks = total_movies//initial_shown_movies

show_more_button =  driver.find_element_by_xpath('//button[@class="btn btn-secondary-rt mb-load-btn"]')

current_shown_movies = initial_shown_movies
time_sleep = 0.001
exp = 0.5

# While to show up all the movies. The While loop does a 
# scroll to the "Show more" button and push it until 
# no more movies apprear 
while current_shown_movies < total_movies:
    time.sleep(time_sleep)
    try:
        # Scrolling
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        ActionChains(driver).move_to_element(show_more_button).perform()
        ActionChains(driver).click(show_more_button).perform()
        current_shown_movies += initial_shown_movies
    except:
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            ActionChains(driver).move_to_element(show_more_button).perform()
        except:
            print("All movies are loaded")
            break
        time_sleep = time_sleep**exp
    print(current_shown_movies)

# Creating a two three list:
# - movie_name: contain the selenium objects with the Movies Titles
# - movies: contain the selenium objects with the movies info
# - movies_list: empty list to be fulfilled with each movie info 
movie_names = driver.find_elements_by_xpath('//h3[@class="movieTitle"]')
movies = driver.find_elements_by_xpath('//div[@class="movie_info"]//a')
movies_list = []

print(len(movies))

# Loop to extract each movie info
for i in range(len(movies)):
    try:
    # TUVE QUE AGREGAR ESTE TRY EXCEPT PORQUE ARROJABA EL SIGUIENTE ERROR:
    # AttributeError: 'NoneType' object has no attribute 'find_next'
    # en audience_score = tomatometer.find_next("span", {"class": "mop-ratings-wrap__percentage"})
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
    except Exception as e:
        print(str(e))
        continue

    movies_list.append(movie_dict)

# Creating dataset and CSV file
dataset = pd.DataFrame(movies_list)
dataset.to_csv('recogiendo_tomates.csv')

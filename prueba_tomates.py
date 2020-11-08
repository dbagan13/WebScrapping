
import requests
import sys
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\
    */*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "en-US,en;q=0.8",
    "Cache-Control": "no-cache",
    "dnt": "1",
    "Pragma": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/5\
    37.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}

options = webdriver.FirefoxOptions()
options.add_argument("--incognito")
driver = webdriver.Firefox(executable_path="./geckodriver", options=options)

#driver = webdriver.Chrome('.\chromedriver')

url = "https://www.rottentomatoes.com/browse/dvd-streaming-all/"

driver.get(url)

#Obtenemos el número total de películas
pans = driver.find_elements_by_xpath('//span')
total_movies = 0
for span in spans:
    if span.text.startswith("Showing"):
        total_movies = int(span.text.split(" ")[-1])
        initial_shown_movies = int(span.text.split(" ")[1])
        show_more_clicks = total_movies//initial_shown_movies

show_more_button =  driver.find_element_by_xpath('//button[@class="btn btn-secondary-rt mb-load-btn"]')

#Hacemos clic en el botón de Show more hasta que se muestren todas las películas
current_shown_movies = initial_shown_movies
time_sleep = 0.001
exp = 0.5
while current_shown_movies < total_movies:
    time.sleep(time_sleep)
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        ActionChains(driver).move_to_element(show_more_button).perform()
        ActionChains(driver).click(show_more_button).perform()
        current_shown_movies += initial_shown_movies
    except:
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            ActionChains(driver).move_to_element(show_more_button).perform()
        except:
            print("TDOAS LAS PELIS MOSTRADAS")
            break
        time_sleep = time_sleep**exp
    print(current_shown_movies)

#Obtenemos la lista de películas y nombres
movie_names = driver.find_elements_by_xpath('//h3[@class="movieTitle"]')
movies = driver.find_elements_by_xpath('//div[@class="movie_info"]//a')
movies_list = []

#Obtenemos la info de cada película y la guardamos en una lista de diccionarios
for i in range(len(movies)):
    movie = movies[i]
    #Título
    movie_dict = {'Title':movie_names[i].text}
    movie_url = movie.get_attribute('href')
    page_movie = requests.get(movie_url, headers=headers)
    soup = BeautifulSoup(page_movie.content, "html.parser")
    #Puntuaciones
    tomatometer = soup.find("span", {"class": "mop-ratings-wrap__percentage"})
    if tomatometer != None:
        audience_score = tomatometer.find_next("span", {"class": "mop-ratings-wrap__percentage"})
        tomatometer = tomatometer.text
    else:
        audience_score = None
        tomatometer = "NaN"
    if audience_score != None: audience_score = audience_score.text
    else: audience_score = "NaN"
    movie_dict['Tomatometer'] = tomatometer.replace('\n',"").replace(" ","")
    movie_dict['Audience score'] = audience_score.replace('\n',"").replace(" ","")
    #Otra infotmación: género, director, fecha de estreno, duración
    info_items = soup.find_all("li", {"class": "meta-row clearfix"})
    for item in info_items:
        field = item.find(("div", {"class": "meta-value subtle"}))
        field_name = field.text
        value = field.find_next().text.replace('\n',"").replace(" ","")
        movie_dict[field_name[:-1]] = value

    print(movie_dict)
    movies_list.append(movie_dict)

print(movies_list)

# Creating dataset and CSV file
dataset = pd.DataFrame(movies_list)

# Eliminando columnas innecesarias del dataset
dataset.drop(columns=['Aspect Ratio', 'Sound Mix', 'Producer',
                      'Box Office (Gross USA)', 'Rating']])

# Convirtiendo dataset a Csv
dataset.to_csv('recogiendo_tomates1.csv')

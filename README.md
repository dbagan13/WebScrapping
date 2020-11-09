

![Alt text](./img/film_image.jpg "Rastreador de Peliculas") 

# WebScrapping

## Proyecto de Tipología y ciclo de vida de los datos de la UOC

## Integrantes:

Daniel Bagan Martínez y Rafael García Henríquez

## Contenido

- ### Directorio csv
    recogiendo_tomastes.csv: fichero con el dataset obtenido por el WebScraper.

- ### Directorio drivers
    geckodriver.exe

- ### Directorio img
    film_image.jpg : imagen de portado del README.md

- ### Directorio pdf
    - respuestas_practica.pdf:  documento con las respuestas a las preguntas planteadas en el enunciado de la práctica
    

- ### Directorio source_code
    Web_driver_generator.py: código de las funciones implementadas para la generación de User Agent y Proxy aleatorios.

    Web_scraper.py: Código del Web Scraper.

- ### Directorio txt
    proxy_list.txt: Lista de proxies sobre la cual se realiza una selección aleatoria.

    requirements.txt: librerias requeridas.


## Fichero a ejecutar
    *Web_scraper.py*  


## Observaciones

- La web Rotten Tomatoes contiene información, como críticas y puntuaciones sobre más de 10.000 películas, así como series y otro contenido audiovisual.
- La lista de películas se obtiene de la página https://www.rottentomatoes.com/browse/dvd-streaming-all/.
- La página muestra inicialmente 32 películas, por lo que se ha utilizado *Selenium* para pulsar el botón *Show more* hasra mostrar todas las películas.
- Existe un **error al mostrar el total de películas** disponibles en la página. Inicialmente aparece el mensaje "Showing 32 of 22505" (aproximadamente). Al hacer clic en *Show more*, el número total de películas baja a 17953, al siguiente clic a 17167, y así sucesivamente, hasta llegar al número real de, aproximadamente, 10000. Este error en la página impide que se pueda usar el número de películas mostrado para calcular cuántas veces se pulsa el botón *Show more*. Por lo que se ha tenido que usar otro método.


## Funcionamento

- Generación de User Agent y Proxy aleatorios.
- Creación de un *WebDriver* con **Selenium**.
- Ingreso en driver de Firefox en la página web https://www.rottentomatoes.com/browse/dvd-streaming-all/, donde se muestran 32 películas.
- Obtención del número de películas totales disponibles (el error en la página inutiliza este paso).
- Localización del botón *Show more*.
- Mientras el botón exista, se hace *scroll* hasta el botón y se clica en él hasta que aparazcan en la página todas las películas disponibles.
    - Cada vez que hay un error en la busqueda o uso del botón, adición de un *time.sleep* exponencial entre solicitudes.
- Una vez se muestran todas las películas en la página, obtención de la lista de todas las etiquetas *h3* de clase "movieTitle", que contienen el nombre de la película, y *div* de clase "movie_info", que contienen su url.
- Para cada película:
    - Creación de un diccionario para almacenar su información.
    - Descarga de su correspondiente página con **BeautifulSoup**.
    - Obtención de su título.
    - Obtención de la puntuación de la propia página y de sus usuarios.
    - Ibtención de la información del apartado de la página "movie info": género, director, fecha de estreno, duración, etc.
    - Almacenamiento del diccionario de la película en una lista.
- Creación de un DataFrame a partir de la lista de diccionarios de películas y creación del CSV a partir de este.

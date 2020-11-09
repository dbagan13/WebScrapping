
![Alt text](./film_image.jpg "Rastreador de Peliculas")

# WebScrapping

## Proyecto de Tipología y ciclo de vida de los datos de la UOC (ENTREGA PARCIAL)

El fichero *recogiendo_tomates.csv* contiene el CSV generado.

## Integrantes:

Daniel Bagan Martínez y Rafael García Henríquez

## Fichero a ejecutar

EL fichero *prueba_tomates.py* contiene el código encargado de realizar el Web Scrapping.

## Objetivo

El objetivo de la práctica es recoger la información de todas las películas disponibles en la web https://www.rottentomatoes.com/.

## Observaciones

- La web Rotten Tomatoes contiene información, como críticas y puntuaciones sobre más de 10.000 películas, así como series y otro contenido audiovisual.
- La lista de películas se obtiene de la página https://www.rottentomatoes.com/browse/dvd-streaming-all/.
- La página muestra inicialmente 32 películas, por lo que se ha utilizado *Selenium* para pulsar el botón *Show more* hasra mostrar todas las películas.
- Existe un **error al mostrar el total de películas** disponibles en la página. Inicialmente aparece el mensaje "Showing 32 of 22505" (aproximadamente). Al hacer clic en *Show more*, el número total de películas baja a 17953, al siguiente clic a 17167, y así sucesivamente, hasta llegar al número real de, aproximadamente, 10000. Este error en la página impide que se pueda usar el número de películas mostrado para calcular cuántas veces se pulsa el botón *Show more*. Por lo que se ha tenido que usar otro método.

## Dependencias

- python
- selenium (webdriver)
- beautifusoup
- pandas
- requests
- time
- random_user_agent

## Funcionamento

- Creación de un *WebDriver* con **Selenium**.
- Se genera un User-Agent aleatorio.
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

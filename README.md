

![Alt text](./memoria/film_image.jpg "Rastreador de Peliculas") 

# WebScrapping

## Proyecto de Tipología y ciclo de vida de los datos de la UOC

## Integrantes:

Daniel Bagan Martínez y Rafael García Henríquez

## Contenido

- ### Directorio csv
    **recogiendo_tomastes.csv:** fichero con el dataset obtenido por el WebScraper.

- ### Directorio drivers
    **geckodriver.exe**

- ### Directorio memoria
    **- respuestas_practica.pdf:**  documento con las respuestas a las preguntas planteadas en el enunciado de la práctica
    
    **- film_image.jpg:** imagen de portado del README.md

- ### Directorio source_code
    **Web_scraper.py:** Código del Web Scraper propuesto como solución de la práctica y con el cual fue generado el dataset final 

- ### Directorio test_random_proxy
    **proxy_list.txt:** Lista de proxies sobre la cual se realiza una selección aleatoria.

    **Web_driver_generator.py:**  Código de las funciones implementadas para la generación de User Agent y Proxy aleatorios.

    **Web_scraper_random_proxy.py:**  Código de **prueba** donde se trata implementar un User Agent y Proxy aleatorios

    **Nota:** Los scripts que se encuentran en este directorio surgen como parte de una posible mejora al codigo ***/source_code/Web_scraper.py.

    Los inconvenientes que se tienen por los momentos con esta implementación son:

    - Se utiliza una lista de proxies libres, por lo cual pueden estar muy congestionadas y ralentiza enormemente el proceso. 
    
    - Como causa de lo anterior, muchas peticiones son rechazadas o se obtiene Time Out, por lo cual se pueden dar caso en donde se realicen hasta 10 intentos antes de lograr una conexión satisfactoria.


## Fichero a ejecutar
    */source_code/Web_scraper.py*  

## Requirements
selenium 3.141.0
beautifulsoup 4.9.3
pandas 1.1.1
requests 2.24.0
time 
rando_user_agent 1.0.1
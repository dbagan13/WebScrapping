

![Alt text](./memoria/film_image.jpg "Rastreador de Peliculas") 

# WebScrapping

## Proyecto de Tipología y ciclo de vida de los datos de la UOC

## Integrantes:

Daniel Bagan Martínez y Rafael García Henríquez

## Contenido

- ### Directorio csv
    **- recogiendo_tomastes.csv:** fichero con el dataset obtenido por el WebScraper.

- ### Directorio drivers
    **- geckodriver.exe**

- ### Directorio memoria
    **- respuestas_practica.pdf:**  documento con las respuestas a las preguntas planteadas en el enunciado de la práctica
    
    **- film_image.jpg:** imagen de portada del README.md

- ### Directorio source_code
    **Web_scraper.py:** Código del Web Scraper propuesto como solución de la práctica y con el cual fue generado el dataset final 

- ### Directorio test_random_proxy
    **- proxy_list.txt:** Lista de proxies sobre la cual se realiza una selección aleatoria.

    **- Web_driver_generator.py:**  Código de las funciones implementadas para la generación de User Agent y Proxy aleatorios.

    **- Web_scraper_random_proxy.py:**  Código de **prueba** donde se trata implementar un User Agent y Proxy aleatorios

    **Nota:** Los scripts que se encuentran en este directorio surgen como parte de una posible mejora al codigo ***/source_code/Web_scraper.py***, con el objetivo de evitar posibles baneos. Se han probado exitosamente con un listado pequeño de películas, pero no se han utilizado para la implementación final.

    Los inconvenientes acontecidos a partir de esta implementación son:

    - Se utiliza una lista de proxies libres, por lo cual pueden estar muy congestionadas y ralentiza enormemente el proceso. 
    
    - Como causa de lo anterior, muchas peticiones son rechazadas o se obtiene Time Out, por lo cual se pueden dar caso en donde se realicen hasta 10 intentos antes de lograr una conexión satisfactoria.
    
    - Este problema se podría resolver mediante la compra de direcciones.

## Fichero a ejecutar
    /source_code/Web_scraper.py

## DOI dataset
Este dataset ha sido publicado en Zenodo con el DOI:  10.5281/zenodo.4265051 y puede ser visualizado en el siguiente link: https://zenodo.org/record/4265051#.X6mORGgReUk

## Requirements
- selenium 3.141.0
- beautifulsoup 4.9.3
- pandas 1.1.1
- requests 2.24.0
- time 
- random_user_agent 1.0.1

# WebScrapping

## Proyecto de Tipología y ciclo de vida de los datos de la UOC (ENTREGA PARCIAL)

El CSV completo se está generando, antes de las 00:00 debería estar generado.
Se ha añadido provisionalmente un fichero CSV reducido (*recogiendo_tomates_reducido.py*) con la información extraída de 32 películas.

## Integrantes:

Daniel Bagan Martínez y Rafael García Henríquez

## Fichero a ejecutar

EL fichero *prueba_tomates.py* contiene el código encargado de realizar el Web Scrapping.

## Objetivo

El objetivo de la práctica es recoger la información de todas las películas disponible en la web https://www.rottentomatoes.com/.

## Observaciones

- La web Rotten Tomatoes contiene información, así como críticas y puntuaciones sobre más de 10.000 películas, así como series y otro contenido audiovisual.
- La lista de películas se obtiene de la página https://www.rottentomatoes.com/browse/dvd-streaming-all/.
- La página muestra inicialmente 32 películas, por lo que se ha utilizado *Selenium* para pulsar el botón *Show more* hasra mostrar todas las películas.
- Existe un **error al mostrar el total de películas** disponibles en la página. Inicialmente aparece el mensaje "Showing 32 of 22505" (aproximadamente). Al hacer clic en *Show more*, el número total de películas baja a 17953, al siguiente clic a 17167, y así sucesivamente, hasta llegar al número real de, aproximadamente, 10000. Este error en la página impide que se pueda usar el número de películas mostrado para calcular cuántas veces se pulsa el botón *Show more*. Por lo que se ha tenido que usar otro método.


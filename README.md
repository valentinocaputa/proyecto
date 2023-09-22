# :mag_right: Proyecto integrador N1 :mag:

# Introduccion
:pushpin: Para este proyecto se nos proporciono un conjunto de tres archivos de steam (Steam es una plataforma de distribución digital
de videojuegos desarrollada por Valve Corporation)
para poder trabajar en ellos y poder crear una api para que un servicio web en la nube consuma lo que fuimos haciendo una vez ya
terminada la investigacion. 

# Contexto 
Trabaje con tres archivos de datos principales:

_**steam_games:**_ Este archivo nos proporciona informacion sobre distintos videojuegos dentro de la plataforma, 
incluyendo titulos, generos, desarroladores, precios de productos, entre otros.

_**user_reviews:**_ Este contiene reseñas de usuarios sobre diferentes juegos. 

_**user_items**_: Este contiene detalles sobre los juegos que los usuarios poseen.

# Transformaciones 
 Antes de poder extraer valor de estos datos, tuve que someterlos a un proceso de ETL, 
 este proceso es esencial para limpiar, transformar y preparar los datos para analizarlos posteriormente.

 _**extraccion:**_Comence cargando los archivos para poder entender cada columna y el tipo de datos que contenia. :heavy_check_mark:

_**transformacion:**_ Realice una transformacion de los datos, eliminando duplicados, tratando valores nulos, y 
realizando conversiones de tipos cuando fue necesario. :heavy_check_mark:

_**carga:**_ Una vez limpios y transformados, cargue estos datos en una estructura mas adecuada para su analisis y posterior implementacion,
en mi caso fue esencial pasar estos archivos ya con el proceso de etl realizado a formato de tipo parquet para poder subirlo a github y que
render me los tome ya que quedaban muy grandes de tamaño. :heavy_check_mark:




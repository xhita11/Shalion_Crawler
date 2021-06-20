# This is an <h1> 
## This is an <h2> 
###### This is an <h6> 


## Junior Python Scraping Challenge
### by Xavier Hita
  
### Instalación y configuración de la Base de Datos
   
###### 1. Clonar el Repositorio en la maquina local.
  
###### 2. Crear un nuevo entorno virtual, si se desea, e instalar los requerimientos del proyecto
  
###### 3. Configurar base de datos.
  
###### 4. Instalacion Sqlite DB Browser para acceder de una manera sencilla a la base de datos sqlite.
 
### Uso del Crawler
  
###### 1. Configurar el fichero input.json con las keywords deseadas.
  
###### 2. Ejecutar Crawler
  
###### 3. Ver resultados
  
###### 4. Borrar resultados



DATABASE.py Options

-- SetUp_Database
-- Delete_Results
-- Show_Results


Configuracion del Crawler 

modify the file ./input.json to



Ejecución del Crawler

Para ejecutar el crawler se debe ejecutar el siguiente comando en linea de comandos dentro de la carpeta Shalion_Crawler.

scrapy crawl products_spider -a json_input=input.json



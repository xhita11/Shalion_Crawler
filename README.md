## Junior Python Scraping Challenge
### by Xavier Hita

<br/><br/>

### Instalación y configuración de la Base de Datos
   
##### 1. Clonar el Repositorio en la maquina local.
  Acceder al directorio donde se quiere ubicar el proyecto e ejecutar el siguiente comando:
  `git clone https://github.com/xhita11/Shalion_Crawler.git`
  
##### 2. Configurar entorno virtual del proyecto
  Crear un nuevo entorno virtual, mediante virtualenv o conda, e instalar las librerias de python usadas en el proyecto mediante el siguiente comando.
  `pip install -r requirements.txt` 
  
##### 3. Configurar base de datos.
 Acceder a la carpeta root del proyecto (pwd/Shalion_Crawler)
 Para configurar la base de datos en su maquina virtual debe ejecutar el siguiente comando en la consola:
  `python Database.py SetUp_Database`
  
##### 4. Instalacion Sqlite DB Browser.
Para acceder de una manera sencilla a la base de datos que contiene los resultados se recomienda isntalar Sqlite Db Browser. Una herramienta sencilla que permite explorar, entre otras cosas, las bases de datos sqlite. El link de instalación es el siguiente: [Sqlite DB Browser Instalation](https://sqlitebrowser.org/dl/)
 
<br/><br/><br/>

### Uso del Crawler
  
##### 1. Configurar el fichero input.json con las keywords deseadas.
  
##### 2. Ejecutar Crawler
  
##### 3. Ver resultados
  
##### 4. Borrar resultados



DATABASE.py Options

-- SetUp_Database
-- Delete_Results
-- Show_Results


Configuracion del Crawler 

modify the file ./input.json to



Ejecución del Crawler

Para ejecutar el crawler se debe ejecutar el siguiente comando en linea de comandos dentro de la carpeta Shalion_Crawler.

scrapy crawl products_spider -a json_input=input.json



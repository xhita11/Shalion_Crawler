## Junior Python Scraping Challenge
### by Xavier Hita

<br/><br/>

### Instalación y configuración de la Base de Datos
   
##### 1. Clonar el Repositorio en la maquina local.
  Acceder al directorio donde se quiere ubicar el proyecto y ejecutar el siguiente comando:<br/>
  `git clone https://github.com/xhita11/Shalion_Crawler.git`
  
##### 2. Configurar entorno virtual del proyecto
  En primer lugar se debe acceder a la carpeta del poryecto ./Shalion_Crawler.<br/>
  En segundo lugar  se debe crear un nuevo entorno virtual, mediante virtualenv o conda, e instalar las librerias de python usadas en el proyecto mediante el siguiente comando.<br/>
  `pip install -r requirements.txt` 
  
##### 3. Configurar base de datos.
Para configurar la base de datos en su maquina virtual debe ejecutar el siguiente comando en la consola:<br/>
  `python Database.py SetUp_Database`
  
##### 4. Instalacion Sqlite DB Browser.
Para acceder de una manera sencilla a la base de datos que contiene los resultados se recomienda isntalar Sqlite Db Browser. Se trata de una herramienta sencilla que permite, entre otras cosas,  explorar las bases de datos sqlite. El link de instalación es el siguiente: [Sqlite DB Browser Instalation](https://sqlitebrowser.org/dl/)
 
<br/><br/><br/>

### Uso del Crawler

##### 1. Configurar el fichero input.json.
Modificar el archivo ./input.json añadiendo al campo keywords los productos que se quieren buscar el el dominio [www.target.com]. 

##### 2. Ejecutar Crawler
Para iniciar el crawler programado ejecutar el siguiente comando:<br/>
`scrapy crawl products_spider -a json_input=input.json` 
  
##### 3. Ver resultados
Para ver los resultados del scrawling ejecutar:<br/>
`python Database.py Show_Results`<br/>

O bien abrir el archivo ./Results.db con el Programa Sqlite DB Browser.
  
##### 4. Exportar resultados
Para exportar los resultados almacenadosen la base de datos ejecutar el siguiente comando:<br/>
`python Database.py Export_Results`<br/>
El fichero "./Results.csv" se sobrescribirá con los datos actuales de la base de datos.
  
##### 5. Borrar resultados
Para borrar los resultados obtenidos de la base de datos ejecutar el siguiente comando:<br/>
`python Database.py Delete_Results`






<h1> Proyecto final de Inteligencia de Negocios</h1>
El presente trabajo tiene como finalidad, la predicción de los resultados de la consulta popular realizada el domingo 4 de febrero del 2018 en Ecuador. A través del análisis de tweets recolectados durante toda la campaña de este evento. 

Para la recolección de los tweets fue necesaria la herramienta CouchDB.
# CouchDB
Prerequisitos.
  - Ubuntu 14.04
  - Acceso a root o usuario no root con privilegios administrativos.
  
Se debe preparar el servidor.

            sudo apt-get update

Ahora, se utiliza el siguiente comando para instalar la herramienta que permitira administrar los repositorios.

            sudo apt-get install software-properties-common -y
            
Se agregar el PPA que ayudará a obtener la última versión de CouchDB desde el repositorio apropiado.
            
            sudo add-apt-repository ppa:couchdb/stable -y
            
<h2> Instalación de CouchDB </h2>
Si anteriormente se encontraba instalada una versión de CouchDB en el servidor, es necesario remover dicha versión para proceder a actualizar la herramienta con la versión más reciente.

            sudo apt-get remove couchdb couchdb-bin couchdb-common -yf
            
Una vez realizado el anterior paso, se procede a instalar CouchDB.

            sudo apt-get install couchdb -y
            
Por defecto, CouchDB trabajará en el localhost en el puerto 5984, dicha información se puede obtener con el siguiente comando.

            curl localhost:5984
            
CouchDB ofrece un servicio capaz de facilitar el manejo de las bases de datos, el cual se accede a través de cualquier navegador y colocando la siguiente URL.
            
            localhost:5984/_utils/
            
Una vez que se presenta la página principal de CouchDB, se debe crear una nueva base de datos, que alojará a los tweets. 

            curl -X PUT localhost:5984/consultapopular
            
<h2> Recolección de tweets </h2>

Para la recolección de tweets, es necesario utilizar el script harvester.py (carpeta recolección), que es el encargado de vincularse con el API de Twitter y almacenar los tweets recolectados en la base de datos en CouchDB.

Para ejecutar el script es necesario instalar Python en el servidor, en caso de tener instalada la herramienta, se procede a verificar la versión de esta con el siguiente comando:

          python
          
Se ejecuta el script de la siguiente manera:

          python (ruta absoluta del archivo harverster.py)

<h2> Filtrado de datos </h2>



            


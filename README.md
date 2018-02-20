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
          
Se debe instalar la librería que permitirá realizar las solicitudes a Twitter, por lo que, es necesario instalar la herramienta pip de python con el siguiente comando:

          sudo apt-get install pip-python
          
Y a continuación, se instala la librería utilizando la herramienta pip.

          pip install tweepy
          
También se instala la librería para vincular Python con CouchDB.

          pip install couchdb
          
Se ejecuta el script de la siguiente manera:

          python "ruta absoluta del archivo harvester.py" "Dirección IP del servidor" "Nombre de la base de datos de CouchDB"

Se debe tener en cuenta que las coordenadas se pueden modificar para recolectar tweets de diferentes lugares.

La mejor práctica sería ejecutar el script en varios computadores con diferentes ubicaciones y una vez que se recolectan los tweets se procede a replicar los tweets en una sola base de datos.

<h2> Replicación de datos</h2>

Para replicar los datos en CouchDB es necesario realizar los siguientes pasos: 
  - Configurar el servidor para recibir o enviar los datos.
      - Dirigirse a "Configuración" en el menú de herramientas.
      - Modificar bind_address en httpd de 127.0.0.1 a 0.0.0.0
  - Iniciar la replicación.
      - Dirigirse a replicación y llenar la información que se solicita.
        En caso de extraer los datos, seleccionar la opción de base de datos remota, llenar el campo con la dirección IP del servidor remoto separado con un "/" y el nombre de la base de datos. En el siguiente campo seleccionar la base de datos local en la que se almacenarán los datos, junto con su nombre.
        
<h2> Filtrado de datos </h2>     

Para obtener datos de acuerdo a nuestro objetivo, es posible filtrarlos a través de vistas. Para realizar una vista, es necesario dirigirse a la base de datos con los tweets recolectados y en vistas seleccionar "Vista temporal".
Se desplegará una caja de texto donde se especificarán los datos que serán filtrados a través de un código ejecutado con el lenguaje JavaScript.
En este caso se realizó el filtrado con el siguiente código:
    function(doc){
      if(doc.lang=="es"){
        emit(doc.id, doc.text);
      }
    }
    
Se filtran los datos de tal  forma que solamente se puede visualizar el id del tweets y su contenido.

<h2> Procesamiento de texto </h2>
Los tweets que se recolectaron contienen información que no sirve para el análisis deseado, por lo que se, procede a la limpieza de estos, escogiendo solamente el texto alfanumérico y descartando todo tipo de caracter especial.
Para ello, es necesario ejecutar el script limpieza.py (carpeta Limpieza Tweets).

          python limpieza.py
          
Lo que generará un archivo de salida en formato .json. -> salida.json

<h2> Selección de datos </h2>
El archivo obtenido anteriormente contiene solamente el texto de los tweets de la base de datos. Sin embargo, algunos tweets no corresponden a la consulta popular, por lo que, es necesario filtrar aquellos que contengan información sobre el evento. Con ayuda de un script (scriptFiltrado, carpeta Filtrado) generado en shell y de las funciones cat y grep, se filtran aquellos que contengan frases o palabras claves referentes al evento. Para ejecutar el script, se utiliza el siguiente comando:

          sh ../scriptFiltrado.sh
          
La ejecución de este script generará un archivo tipo json -> resultadoFinal.json

<h2> Análisis de datos </h2>

Del último archivo generado, se analizarán los datos de tal forma que, se pueda clasificar aquellos que pertenezcan a la clase SI y aquellos que pertenezcan a la clase NO. Con ayuda del script realizado en Python (Clasificador.py, carpeta Clasificador) se pueden agrupar las coincidencias en cada tweet filtrado y al final presenta los resultados, que son aquellos que predecirán el resultado de la consulta popular. Para ejecutar el script, es necesario instalar la librería sklearn, con el siguiente comando:

          pip install sklearn
          
A continuación, bastará con ejecutar el script resultados.py (carpeta Resultados), e interpretar el resultado que se presenta al final de la ejecución del mismo.

          py resultados.py




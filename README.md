# SIC_Big_Data_CDC
https://www.whed.net/home.php

https://www.universidades.gob.es/estadistica-de-estudiantes/

https://www.ine.es/jaxi/Datos.htm?tpx=4889

http://siiu.universidades.gob.es/QEDU/

https://www.topuniversities.com/university-rankings/university-subject-rankings/2020/accounting-finance

https://www.adscientificindex.com/university/Universidad+Polit%C3%A9cnica+de+Madrid/

https://estadisticas.universidades.gob.es/dynPx/inebase/index.htm?type=pcaxis&path=/Universitaria/Indicadores/2022/1_Grado&file=pcaxis&l=s0

arte_diseno_arquitectura: arquitectura, diseño, bellas artes

agricultura_forestal

empresariales_administracion: empresa, empresariales, relaciones

economicas: economicas

educacion: educación

ingenieria_tecnologia: Ingenieria, politécnica, informática,

historia_filosofia_teologia:filosofía, historia

leyes_abogacia: derecho, jurídicas

ciencias_salud: psicología, salud, medicina , farmacia, alimentación, deporte, ontodología

ciencias_naturales: Física, matematicas

ciencias_sociales: comunicación, humanidades, sociologia , humana

otros

# Instalación
1. Descargar .zip de la rama main de github
2. Extraer carpeta
3. Crear e insertar datos en MariaDB
4. Crea la base de datos e inserta datos en MariaDB
   - Abre una consola
   - Ejecuta el comando: ```console pip install mysql-connector-python ```
   - Ejecuta jupyter notebook
   - Muévete a la carpeta SIC_Big_Data_CDC-ETLDB/Scripts
   - Abre el archivo: ```console QEDU a MariaDB.ipynb ```
5. Migra datos de Maria DB a Hive
   - Abre una consola
   - Navega a la carpeta SIC_Big_Data_CDC-ETLDB/Scripts
   - Ejecuta el comando: ```console chmod u+x export_MariaDB_hive.sh```
   - Ejecuta el comando: ```console ./export_MariaDB_hive.sh```
6. Crea la tabla externa de tweets en la base de datos de Hive
   - Abre una consola
   - Abre hive con el siguiente comando: ```console beeline -u jdbc:hive2://```
   - Selecciona la base de datos importada: ```console use proyecto_final;```
   - Crea la tabla de tweets desde hive con el comando(consulta el fichero Scripts/external_table_tweets): ```console create external table tweets (usuario string, siglas string, mensaje string, likes int) row format delimited fields terminated by '\t';```
7. Crea un directorio en hdfs para el preprocesado de tweets:
   - Abre una nueva consola
   - Crea el directorio con el comando: ```console hdfs dfs -mkdir /user/student/tweets_precprocessing```
8. Configura el archivo de preprocesado de tweets:
   - Navega a SIC_Big_Data_CDC-ETLDB/Scripts
   - Edita el archivo auto_process.sh con el siguiente comando: ```nano auto_process.sh```
   - En la línea PIG_SCRIPT=... asegúrate de que la ruta al archivo 'pig_tweets_preprocessing.pig' sea correcta.
   - Guarda el archivo con los cambios si los has realizado
   - Ejecuta el siguiente comando para darle permisos de ejecución: ```console chmod u+x auto_process.sh```
9. Configura crontab para que ejecute el script de preprocesado de tweets cada minuto
   - Abre una consola
   - Navega a SIC_Big_Data_CDC-ETLDB/Scripts
   - Ejecuta el siguiente comando para editar crontab: ```console EDITOR=nano crontab -e```
   - Copia el contenido del archivo SIC_Big_Data_CDC-ETLDB/Crontab configuration en la pantalla que aparece (ASEGÚRATE DE QUE LA RUTA AL ARCHIVO auto_process.sh ES CORRECTA)
   - Guarda los cambios
10. Ejecuta el agente flume que escucha tweets
    - Abre una consola
    - Navega a SIC_Big_Data_CDC-ETLDB/Scripts
    - Ejecuta el siguiente comando para activar el agente flume: ```console flume-ng agent -name tweet_listener -conf-file tweet_listener_agent.conf```
    - NO CIERRES ESTA CONSOLA SI QUIERES ESCUCHAR TWEETS
11. Simula los tweets
    - Abre una consola
    - Navega a SIC_Big_Data_CDC-ETLDB/Scripts
    - Ejecuta el siguiente comando para generar tweets: ```console python3 fake_tweet_generator.py localhost 44444```

# SIC_Big_Data_CDC

# Instalación
1. Descargar .zip de la rama main de github y extrae la carpeta
2. Instala dependencias de python
   - Ejecuta el comando: ```pip install mysql-connector-python ```
   - Ejecuta el comando: ```pip install matplotlib ```
4. Crea la base de datos e inserta datos en MariaDB
   - Abre una consola
   - Ejecuta jupyter notebook
   - Muévete a la carpeta SIC_Big_Data_CDC-ETLDB/Scripts
   - Abre el archivo: ```QEDU a MariaDB.ipynb ```
   - Ejecuta todas las celdas del notebook
3. Crea la base de datos en Hive
   - Abre una consola
   - Abre hive con el siguiente comando: ```beeline -u jdbc:hive2://```
   - Crea la base de datos con el comando: ```create database proyecto_final```
5. Migra datos de Maria DB a Hive
   - Abre una consola
   - Navega a la carpeta SIC_Big_Data_CDC-ETLDB/Scripts
   - Ejecuta el comando: ```chmod u+x export_MariaDB_hive.sh```
   - Ejecuta el comando: ```./export_MariaDB_hive.sh```
6. Crea la tabla externa de tweets en la base de datos de Hive
   - Abre una consola
   - Abre hive con el siguiente comando: ```beeline -u jdbc:hive2://```
   - Selecciona la base de datos importada: ```use proyecto_final;```
   - Crea la tabla de tweets desde hive con el comando(consulta el fichero Scripts/external_table_tweets): ```create external table tweets (usuario string, siglas string, mensaje string, likes int) row format delimited fields terminated by '\t';```
7. Crea un directorio en hdfs para el preprocesado de tweets:
   - Abre una nueva consola
   - Crea el directorio con el comando: ```hdfs dfs -mkdir /user/student/tweets_preprocessing```
8. Configura el archivo de preprocesado de tweets:
   - Navega a SIC_Big_Data_CDC-ETLDB/Scripts
   - Edita el archivo auto_process.sh con el siguiente comando: ```nano auto_process.sh```
   - En la línea PIG_SCRIPT=... asegúrate de que la ruta al archivo 'pig_tweets_preprocessing.pig' sea correcta.
   - Guarda el archivo con los cambios si los has realizado
   - Ejecuta el siguiente comando para darle permisos de ejecución: ```chmod u+x auto_process.sh```
9. Configura crontab para que ejecute el script de preprocesado de tweets cada minuto
   - Abre una consola
   - Ejecuta el siguiente comando para editar crontab: ```EDITOR=nano crontab -e```
   - Copia el contenido del archivo SIC_Big_Data_CDC-ETLDB/Crontab configuration en la pantalla que aparece (ASEGÚRATE DE QUE LA RUTA AL ARCHIVO auto_process.sh ES CORRECTA)
   - Guarda los cambios
10. Ejecuta el agente flume que escucha tweets
    - Abre una consola
    - Navega a SIC_Big_Data_CDC-ETLDB/Scripts
    - Ejecuta el siguiente comando para activar el agente flume: ```flume-ng agent -name tweet_listener -conf-file tweet_listener_agent.conf```
    - NO CIERRES ESTA CONSOLA SI QUIERES ESCUCHAR TWEETS
11. Simula los tweets
    - Abre una consola
    - Navega a SIC_Big_Data_CDC-ETLDB/Scripts
    - Ejecuta el siguiente comando para generar tweets: ```python3 fake_tweet_generator.py localhost 44444```
    - Cierra el script cuando creas que tienes suficientes tweets
12. Entrena los modelos
    - Abre una consola
    - Ejecuta el comando: ```pyspark```
    - Ejecuta el notebook SIC_Big_Data_CDC/Scripts/AnalisisSentimientosBueno.ipynb
    - Ejecuta el notebook SIC_Big_Data_CDC/Scripts/regresion_notas_corte.ipynb
13. Prueba el sistema de recomendación
    - Abre una consola
    - Ejecuta el comando: ```pyspark```
    - Ejecuta el notebook SIC_Big_Data_CDC/Scripts/recomendacion_universidades.ipynb
    - Introduce inputs con tus preferencias cuando el programa lo requiera

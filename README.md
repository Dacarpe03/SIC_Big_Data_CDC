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
   - Ejecuta el comando ```console pip install mysql-connector-python ```
   - Ejecuta jupyter notebook
   - Muévete a la carpeta SIC_Big_Data_CDC-ETLDB/Scripts
   - Abre el archivo ```console QEDU a MariaDB.ipynb ```
5. Migra datos de Maria DB a Hive
   - Abre una consola
   - Navega a la carpeta SIC_Big_Data_CDC-ETLDB/Scripts
   - Ejecuta el comando ```console chmod u+x export_MariaDB_hive.sh```
   - Ejecuta el comando ```console ./export_MariaDB_hive.sh```
6. Crea la tabla externa de tweets en la base de datos de Hive
   - Abre una consola
   - Abre hive con el siguiente comando ```console beeline -u jdbc:hive2://```
   - 

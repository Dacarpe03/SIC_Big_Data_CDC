sqoop import --connect jdbc:mysql://localhost/proyecto_final --username student --password student --fields-terminated-by '\t' --table Universidades --hive-import --hive-database 'proyecto_final' --hive-table 'universidades' --split-by id

sqoop import --connect jdbc:mysql://localhost/proyecto_final --username student --password student --fields-terminated-by '\t' --table Facultades --hive-import --hive-database 'proyecto_final' --hive-table 'facultades' --split-by id

sqoop import --connect jdbc:mysql://localhost/proyecto_final --username student --password student --fields-terminated-by '\t' --table Grados --hive-import --hive-database 'proyecto_final' --hive-table 'grados' --split-by id

sqoop import --connect jdbc:mysql://localhost/proyecto_final --username student --password student --fields-terminated-by '\t' --table Campos --hive-import --hive-database 'proyecto_final' --hive-table 'campos' --split-by id

sqoop import --connect jdbc:mysql://localhost/proyecto_final --username student --password student --fields-terminated-by '\t' --table Rankings --hive-import --hive-database 'proyecto_final' --hive-table 'rankings' --split-by id


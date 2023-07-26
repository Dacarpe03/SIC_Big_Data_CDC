#!/bin/bash

PATH=/usr/lib64/qt-3.3/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin:/opt/jdk1.8.0_291/bin:/opt/jdk1.8.0_291/jre/bin:/home/hadoop/hadoop/sbin:/home/hadoop/hadoop/bin:/usr/local/hive/hive-3.1.2/bin:/usr/local/sqoop/sqoop-1.4.7/bin:/usr/local/flume/flume-1.9.0/bin:/home/kafka/kafka/bin:/usr/local/hbase/hbase-2.3.5/bin:/usr/local/spark3/spark-3.1.2-bin-hadoop3.2/bin:/usr/local/pig/pig-0.17.0/bin:/home/student/.local/bin:/home/student/bin
export JAVA_HOME='/opt/jdk1.8.0_291'

NOW=$(date +'%Y-%m-%d-%H-%M-%S')
FILENAME='tweets-'$NOW'.csv'
HDFS_PREPROCESSING_FILES_PATH='/user/student/tweets_preprocessing/*csv'
HDFS_PROCESSED_PATH='/user/student/tweets_processed'
HDFS_PROCESSED_FILES_PATH='/user/student/tweets_processed/part*'
HDFS_DB_PATH='/user/hive/warehouse/proyecto_final.db/tweets/'

HDFS_COMMAND='/home/hadoop/hadoop/bin/hdfs'
PIG_COMMAND='/usr/local/pig/pig-0.17.0/bin/pig'

PIG_SCRIPT='/home/student/SIC_Project/pig_tweets_preprocessing.pig'
$PIG_COMMAND $PIG_SCRIPT

$HDFS_COMMAND dfs -rm $HDFS_PREPROCESSING_FILES_PATH
$HDFS_COMMAND dfs -mv $HDFS_PROCESSED_FILES_PATH $HDFS_DB_PATH$FILENAME
$HDFS_COMMAND dfs -rm -r $HDFS_PROCESSED_PATH

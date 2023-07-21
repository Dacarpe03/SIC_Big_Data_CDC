#!/bin/bash
NOW=$(date +'%Y-%m-%d-%H-%M-%S')
FILENAME='tweets-'$NOW'.csv'
HDFS_PREPROCESSING_FILES_PATH='/user/student/tweets_preprocessing/*csv'
HDFS_PROCESSED_PATH='/user/student/tweets_processed'
HDFS_PROCESSED_FILES_PATH='/user/student/tweets_processed/part*'
HDFS_DB_PATH='/user/hive/warehouse/proyecto_final.db/tweets/'

PIG_SCRIPT='/home/student/SIC_Project/pig_tweets_preprocessing.pig'
pig $PIG_SCRIPT

hdfs dfs -rm $HDFS_PREPROCESSING_FILES_PATH
hdfs dfs -mv $HDFS_PROCESSED_FILES_PATH $HDFS_DB_PATH$FILENAME
hdfs dfs -rm -r $HDFS_PROCESSED_PATH

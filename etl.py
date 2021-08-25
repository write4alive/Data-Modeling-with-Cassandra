from cassandra import cluster
import pandas as pd
import cassandra
from cassandra.cluster import Cluster
import re
import os
import glob
import numpy as np
import json
import csv
from cassandra_queries import *

def data_denormalization():
    '''
    data_denormalization() funcion get data from /event_data path and denormalize it with using csv operation and creating new file called "event_datafile_new.csv". then continue with  all database operations  

    No Parameters
    No Return value

    '''
    try:
        # checking your current working directory
        # print(os.getcwd())

        # Get your current folder and subfolder event data
        filepath = os.getcwd() + '/event_data'

        # Create a for loop to create a list of files and collect each filepath
        for root, dirs, files in os.walk(filepath):
            
        # join the file path and roots with the subdirectories using glob
            file_path_list = glob.glob(os.path.join(root,'*'))
            # print(file_path_list)

        # initiating an empty list of rows that will be generated from each file
        full_data_rows_list = [] 
            
        # for every filepath in the file path list 
        for f in file_path_list:

        # reading csv file 
            with open(f, 'r', encoding = 'utf8', newline='') as csvfile: 
                # creating a csv reader object 
                csvreader = csv.reader(csvfile) 
                next(csvreader)
                
        # extracting each data row one by one and append it        
                for line in csvreader:
                    #print(line)
                    full_data_rows_list.append(line) 
                    
        # uncomment the code below if you would like to get total number of rows 
        # print(len(full_data_rows_list))
        # uncomment the code below if you would like to check to see what the list of event data rows will look like
        # print(full_data_rows_list)

        # creating a smaller event data csv file called event_datafile_full csv that will be used to insert data into the \
        # Apache Cassandra tables
        csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

        with open('event_datafile_new.csv', 'w', encoding = 'utf8', newline='') as f:
            writer = csv.writer(f, dialect='myDialect')
            writer.writerow(['artist','firstName','gender','itemInSession','lastName','length',\
                        'level','location','sessionId','song','userId'])
            for row in full_data_rows_list:
                if (row[0] == ''):
                    continue
                writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))


        # check the number of rows in your csv file
        with open('event_datafile_new.csv', 'r', encoding = 'utf8') as f:
            print('New file contains ',sum(1 for line in f),' of rows')
            print("------------------------------")
    except Exception as e:
        print(e)

def cassandra_operations():
    '''
    cassandra_operations() function eastablish connection with cassandra and there are some operations : create keyspace , insert data and drop tables that our work done.
    
    No Paramaters
    No Return value

    '''
# connection to cassandra
    try:
        cluster=Cluster(['127.0.0.1'])
        session=cluster.connect()
        print("Connection established to server !")
    except Exception as e:
        print(e)
        print("Fail to connect Cassandra !")


# Creating KEYSPACE
    try:
        session.execute(q_create_keyspace)
    except Exception as e:
        print(e)
        print("Create keyspace fail !")


# Connectting KEYSPACE
    try:
        session.set_keyspace('project2')
        print("Connection established to keyspace")
        print("------------------------------")
    except Exception as e:
        print(e)
        print("Fail to connect keyspace !")


# Droping Tables
    try:
        session.execute(q1_drop_table)
        print("musicapp_sessionid_iteminsession dropped !")
    except Exception as e:
        print(e)
        print("Fail to drop musicapp_sessionid_iteminsession !")

    try:
        session.execute(q2_drop_table)
        print("musicapp_userid_sessionid_c_iteminsession dropped !")
    except Exception as e:
        print(e)
        print("Fail to drop musicapp_userid_sessionid_c_iteminsession !")

    try:
        session.execute(q3_drop_table)
        print("musicapp_song_userid dropped !")
        print("------------------------------")
    except Exception as e:
        print(e)
        print("Fail to drop musicapp_song_userid !")




# Creating Tables
    try:
        session.execute(q1_create_table)
        print("musicapp_sessionid_iteminsession created !")
    except Exception as e:
        print(e)
        print("Fail to create musicapp_sessionid_iteminsession !")


    try:
        session.execute(q2_create_table)
        print("musicapp_userid_sessionid_c_iteminsession created !")
    except Exception as e:
        print(e)
        print("Fail to create musicapp_userid_sessionid_c_iteminsession !")


    try:
        session.execute(q3_create_table)
        print("musicapp_song_userid created !")
        print("------------------------------")
    except Exception as e:
        print(e)
        print("Fail to create musicapp_song_userid !")






    # insert data from Csv file to 3 different tables based on required queries
    try:
        file = 'event_datafile_new.csv'
        with open(file, encoding = 'utf8') as f:
            csvreader = csv.reader(f)
            next(csvreader) # skip header
            for line in csvreader:
                query = q1_table_insert
                session.execute(query, (int(line[8]),int(line[3]),line[0],line[9],float(line[5])))
            print("musicapp_sessionid_iteminsession data extraction completed")
    except Exception as e:
        print(e)


    try:
        file = 'event_datafile_new.csv'
        with open(file, encoding = 'utf8') as f:
            csvreader = csv.reader(f)
            next(csvreader) # skip header
            for line in csvreader:
                query = q2_table_insert
                session.execute(query, (int(line[10]),int(line[8]),int(line[3]),line[0],line[9],line[1],line[4]))
            print("musicapp_userid_sessionid_c_iteminsession data extraction completed")
    except Exception as e:
        print(e)
                


    try:
        file = 'event_datafile_new.csv'
        with open(file, encoding = 'utf8') as f:
            csvreader = csv.reader(f)
            next(csvreader) # skip header
            for line in csvreader:
                query=""
                query = q3_table_insert
                session.execute(query, (line[9],int(line[10]),line[1],line[4]))
            print("musicapp_song_userid data extraction completed")
            print("------------------------------")
    except Exception as e:
        print(e) 


# Select queries for each question

# Query 1:  Give me the artist, song title and song's length in the music app history that was heard during \
## sessionId = 338, and itemInSession = 4

    
    try:
        query = q1_select
        rows = session.execute(query)
    except Exception as e:
        print(e)
    
    for row in rows:
        print ('Question 1 - Query Result :  ',row.artist, row.song,row.length)
    print("------------------------------")



# Query 2 - Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name)\
## for userid = 10, sessionid = 182

    
    try:
        query = q2_select
        rows = session.execute(query)
    except Exception as e:
        print(e)
    
    for row in rows:
        print ('Question 2 - Query Result :  ',row.artist, row.song, row.firstname, row.lastname)
    print("------------------------------")

       

# Query 3: Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'

    
    try:
        query = q3_select
        rows = session.execute(query)
    except Exception as e:
        print(e)
    
    for row in rows:
        print ('Question 3 - Query Result :  ',row.firstname, row.lastname)
    print("------------------------------")


    try:
        session.shutdown()
        print('Session Shutdown...')
        cluster.shutdown()
        print('closing clusters...')
    except Exception as e:
        print(e)
    

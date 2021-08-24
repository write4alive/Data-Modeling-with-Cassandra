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
    data_denormalization() funcion get data from /event_data path and denormalize it with using csv operation and creating new file called "event_datafile_new.csv". then you can pass to cassandra operations

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
    except Exception as e:
        print(e)
        print("Fail to connect keyspace !")


# Droping Tables
    try:
        session.execute(q_drop_table_1)
        print("q_table_1 dropped !")
    except Exception as e:
        print(e)
        print("Fail to drop q_table_1 !")



# Creating Tables
    try:
        session.execute(q_create_table_1)
        print("q1_table created !")
    except Exception as e:
        print(e)
        print("Fail to create q1_table !")








    # We have provided part of the code to set up the CSV file. Please complete the Apache Cassandra code       below#
    file = 'event_datafile_new.csv'

    with open(file, encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header
        for line in csvreader:
    ## TO-DO: Assign the INSERT statements into the `query` variable
            query = q1_table_insert
            # query = query + "<ASSIGN VALUES HERE>"
            ## TO-DO: Assign which column element should be assigned for each column in the INSERT statement.
            ## For e.g., to INSERT artist_name and user first_name, you would change the code below to `line[0], line[1]
            session.execute(query, (line[0],line[9],line[5],line[3],line[8]))
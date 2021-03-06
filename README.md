# Data Engineering Nano Degree Programm of Udacity - Project 2 -

<h1>Project: Data Modeling with Cassandra</h1>
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analysis team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate the results, since the data reside in a directory of CSV files on user activity on the app.<br>

They'd like a data engineer to create an Apache Cassandra database which can create queries on song play data to answer the questions, and wish to bring you on the project. Your role is to create a database for this analysis. You'll be able to test your database by running queries given to you by the analytics team from Sparkify to create the results.<br>

<h2>Project Overview</h2> <br>
In this project, you'll apply what you've learned on data modeling with Apache Cassandra and complete an ETL pipeline using Python. To complete the project, you will need to model your data by creating tables in Apache Cassandra to run queries. You are provided with part of the ETL pipeline that transfers data from a set of CSV files within a directory to create a streamlined CSV file to model and insert data into Apache Cassandra tables.<br>

We have provided you with a project template that takes care of all the imports and provides a structure for ETL pipeline you'd need to process this data.<br>

<h2>Datasets</h2>
For this project, you'll be working with one dataset: event_data. The directory of CSV files partitioned by date. Here are examples of filepaths to two files in the dataset:
<br>
event_data/2018-11-08-events.csv <br>
event_data/2018-11-09-events.csv <br>

<h2>Project Template</h2><br>
To get started with the project, go to the workspace on the next page, where you'll find the project template (a Jupyter notebook file). You can work on your project and submit your work through this workspace.<br>

The project template includes one Jupyter Notebook file, in which:<br>

you will process the event_datafile_new.csv dataset to create a denormalized dataset<br>
you will model the data tables keeping in mind the queries you need to run<br>
you have been provided queries that you will need to model your data tables for<br>
you will load the data into tables you create in Apache Cassandra and run your queries<br>
<br>

<h2>Project Steps </h2> <br>
Below are steps you can follow to complete each component of this project.<br>

Modeling your NoSQL database or Apache Cassandra database<br>
Design tables to answer the queries outlined in the project template<br>
Write Apache Cassandra CREATE KEYSPACE and SET KEYSPACE statements<br>
Develop your CREATE statement for each of the tables to address each question<br>
Load the data with INSERT statement for each of the tables<br>
Include IF NOT EXISTS clauses in your CREATE statements to create tables only if the tables do not already exist. We recommend you also include DROP TABLE statement for each table, this way you can run drop and create tables whenever you want to reset your database and test your ETL pipeline<br>
Test by running the proper select statements with the correct WHERE clause<br>
Build ETL Pipeline<br>
Implement the logic in section Part I of the notebook template to iterate through each event file in event_data to process and create a new CSV file in Python<br>
Make necessary edits to Part II of the notebook template to include Apache Cassandra CREATE and INSERT statements to load processed records into relevant tables in your data model<br>
Test by running SELECT statements after running the queries on your database<br>

You can run project with using just start.py and check all results in terminal<br>

![Result](https://user-images.githubusercontent.com/16669517/130688919-9950dc91-7198-49bf-a0fd-51853f79911f.png)



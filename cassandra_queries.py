# cassandra_queris.py contains keyspace queries for cassandra

# create keyspace 
q_create_keyspace=("""
CREATE KEYSPACE IF NOT EXISTS project2 
WITH REPLICATION = 
{ 'class' : 'SimpleStrategy', 'replication_factor' : 1 } """)


# create question query tables
q1_create_table=(""" 
CREATE TABLE IF NOT EXISTS q1_table (sessionid int ,iteminsession int,artist text ,song text, length text, primary key(sessionid,iteminsession))
""")

q2_create_table=(""" 
CREATE TABLE IF NOT EXISTS q2_table (userid int,sessionid int,iteminsession int, artist text ,song text, firstname text ,lastname text, primary key((userid,sessionid),iteminsession))
""")

q3_create_table=(""" 
CREATE TABLE IF NOT EXISTS q3_table (song text, userid int, firstname text, lastname text , primary key(song,userid))
""")



# insert tables

q1_table_insert =("""
insert into q1_table (sessionid, iteminsession, artist, song, length ) values(%s,%s,%s,%s,%s)
""")

q2_table_insert=("""
insert into q2_table (userid ,sessionid ,iteminsession , artist, song, firstname, lastname ) values(%s,%s,%s,%s,%s,%s,%s)
""")

q3_table_insert=("""
insert into q3_table (song, userid, firstname, lastname ) values(%s,%s,%s,%s)
""")



# select from tables

q1_select=("""
SELECT artist,song,length from q1_table where sessionid= 338 and iteminsession=4
""")

q2_select=("""
SELECT artist,song,firstname ,lastname from q2_table where sessionid= 182 and userid=10
""")

q3_select=("""
SELECT firstname ,lastname from q3_table where song='All Hands Against His Own'
""")



# drop tables
q1_drop_table=(""" drop table if exists q1_table
""")

q2_drop_table=(""" drop table if exists q2_table
""")

q3_drop_table=(""" drop table if exists q3_table
""")


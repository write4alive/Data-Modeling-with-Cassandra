# cassandra_queris.py contains keyspace queries for cassandra

# create keyspace 
q_create_keyspace=("""
CREATE KEYSPACE IF NOT EXISTS project2 
WITH REPLICATION = 
{ 'class' : 'SimpleStrategy', 'replication_factor' : 1 } """)


# create question query tables
#  we are going to create musicapp_sessionid_iteminsession table for question 1 and query 1. we pick sessionid and iteminsession as primary key to make data unique for the required query.
q1_create_table=(""" 
CREATE TABLE IF NOT EXISTS musicapp_sessionid_iteminsession (sessionid int ,iteminsession int,artist text ,song text, length float, primary key(sessionid,iteminsession))
""")

#  we are going to create musicapp_userid_sessionid_c_iteminsession table for question 2 and query 2. userid and sessionid  are our primary key to make data unique and we are doing a little trick adding iteminsessionid as clustring column to order our data as requested in the question 2.
q2_create_table=(""" 
CREATE TABLE IF NOT EXISTS musicapp_userid_sessionid_c_iteminsession (userid int,sessionid int,iteminsession int, artist text ,song text, firstname text ,lastname text, primary key((userid,sessionid),iteminsession))
""")

#  we are going to create musicapp_song_userid with using song and userid as primary key.We need these two columns to make our data row as unique.
q3_create_table=(""" 
CREATE TABLE IF NOT EXISTS musicapp_song_userid (song text, userid int, firstname text, lastname text , primary key(song,userid))
""")



# insert tables

#  inserting data to table musicapp_sessionid_iteminsession  - for the question 1 
q1_table_insert =("""
insert into musicapp_sessionid_iteminsession (sessionid, iteminsession, artist, song, length ) values(%s,%s,%s,%s,%s)
""")

# inserting data to table musicapp_userid_sessionid_c_iteminsession  - for the question 2
q2_table_insert=("""
insert into musicapp_userid_sessionid_c_iteminsession (userid ,sessionid ,iteminsession , artist, song, firstname, lastname ) values(%s,%s,%s,%s,%s,%s,%s)
""")

# inserting data to table musicapp_song_userid  - for the question 3
q3_table_insert=("""
insert into musicapp_song_userid (song, userid, firstname, lastname ) values(%s,%s,%s,%s)
""")



# select from tables

# we are going to select artist name ,song name and length of the song for question 1 answer with using condition on sessionid and iteminsession
q1_select=("""
SELECT artist,song,length from musicapp_sessionid_iteminsession where sessionid= 338 and iteminsession=4
""")
# we are going to select artist name , song name , user first name , last name from our second table which is musicapp_userid_sessionid_c_iteminsession with using condition on sessionid and userid
q2_select=("""
SELECT artist,song,firstname ,lastname from musicapp_userid_sessionid_c_iteminsession where sessionid= 182 and userid=10
""")
#  we are selecting user name and user last name from musicapp_song_userid who  listed song named 'All Hands Against His Own'
q3_select=("""
SELECT firstname ,lastname from musicapp_song_userid where song='All Hands Against His Own'
""")



# drop tables
q1_drop_table=(""" drop table if exists musicapp_sessionid_iteminsession
""")

q2_drop_table=(""" drop table if exists musicapp_userid_sessionid_c_iteminsession
""")

q3_drop_table=(""" drop table if exists musicapp_song_userid
""")


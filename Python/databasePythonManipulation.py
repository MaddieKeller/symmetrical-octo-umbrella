import sqlite3

#connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')
'''

#add the SQL Table
conn.execute("CREATE TABLE Simpson_info( \
ID INTEGER PRIMARY KEY AUTOINCREMENT, \
NAME TEXT, \
GENDER TEXT, \
AGE INT, \
OCCUPATION TEXT );")


#add Bart Simpson to the table
conn.execute("INSERT INTO Simpson_info (\
NAME,\
GENDER,\
AGE,\
OCCUPATION) \
VALUES ('Bart Simpson', \
'Male', \
10, \
'Student')")

#add Homer Simpson to the table
conn.execute("INSERT INTO Simpson_info (\
NAME,\
GENDER,\
AGE, \
OCCUPATION) \
VALUES ('Homer Simpson', \
'Male', \
40, \
'Nuclear Plant Operator')")

#add Lisa Simpson to the table
conn.execute("INSERT INTO Simpson_info (\
NAME, \
GENDER, \
AGE, \
OCCUPATION) \
VALUES ('Lisa Simpson', \
'Female', \
8, \
'Student')")

#Save your changes
conn.commit()

#print number of changes
changes = conn.total_changes
print "Number of Changes: ", changes


cursor = conn.execute("SELECT * FROM SIMPSON_INFO WHERE GENDER='Female'")
rows = cursor.fetchall()

print rows

cursor = conn.execute("SELECT * FROM SIMPSON_INFO WHERE OCCUPATION='Student'")
rows = cursor.fetchall()

print rows

#delete a row of data
conn.execute("DELETE FROM SIMPSON_INFO WHERE ID=6")
conn.commit()

#update a value
conn.execute("UPDATE Simpson_info set AGE=41 where NAME='Homer Simpson'")

#view all rows in the table
cursor = conn.execute("SELECT * FROM SIMPSON_INFO")
rows = cursor.fetchall()
print rows
'''
#delete the table
conn.execute("DROP TABLE Simpson_info")


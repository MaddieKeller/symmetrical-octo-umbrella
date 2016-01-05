import sqlite3

#connect to the database
conn = sqlite3.connect('simpsons.db')

def dupCheck(name):
    #check for duplicates
    sql_str = "SELECT * from Simpson_info where NAME='{}'".format(name)
    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()
    if len(rows)>0:
        print 'This character already exists.'
        return True
    else:
        return False



def createTable ():
    conn.execute("CREATE TABLE if not exists Simpson_info( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    NAME TEXT, \
    GENDER TEXT, \
    AGE INT, \
    OCCUPATION TEXT);")

def printData(data):
    for row in data:
        print "ID: ",row[0]
        print "Name: ", row[1]
        print "Gender: ",row[2]
        print "Age: ",row[3]
        print "Occupation: ", row[4], "\n"

def newCharacters(name, gender, age, occupation):
    print'\nAdding a new character...'
    #create a string with all the raw input
    val_str = "'{}','{}',{},'{}'".format(name, gender, age, occupation)
    #update the table with the raw input
    execString='INSERT INTO Simpson_info (NAME, GENDER, AGE, OCCUPATION) values ({});'.format(val_str)
    print execString
    conn.execute(execString)
    conn.commit()
    return conn.total_changes

def viewAll():
    #create a sql string
    sql_str = "SELECT * FROM Simpson_info"
    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()
    return rows

def changeCharacter(change_id,name,age,gender,occupation):
    # Create values part of sql command
    val_str = "NAME='{}', GENDER='{}',\
              AGE={}, OCCUPATION='{}'".format(\
              name, gender, age, occupation)

    sql_str = "UPDATE SIMPSON_INFO set {} where ID={};".format(val_str,change_id)
    print sql_str

    conn.execute(sql_str)
    conn.commit()
    return conn.total_changes

def deleteCharacter(change_id):
    # Create sql string
    sql_str = "DELETE from SIMPSON_INFO where ID={}"\
             .format(change_id)
    conn.execute(sql_str)
    conn.commit()
    return conn.total_changes

createTable()

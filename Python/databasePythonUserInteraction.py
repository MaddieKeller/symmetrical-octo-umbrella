import sqlite3

#connect to the database
conn = sqlite3.connect('simpsons.db')

def createTable ():
    conn.execute("CREATE TABLE if not exists Simpson_info( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    NAME TEXT, \
    GENDER TEXT, \
    AGE INT, \
    OCCUPATION TEXT);")

createTable()

def printData(data):
    for row in data:
        print "ID: ",row[0]
        print "Name: ", row[1]
        print "Gender: ",row[2]
        print "Age: ",row[3]
        print "Occupation: ", row[4], "\n"

#create a function to add a new character
def newCharacters():
    print'\nAdding a new character...'

    #take inputs
    name = raw_input('Name: ')
    gender = raw_input('Gender: ')
    age = raw_input('Age: ')
    occupation = raw_input('Occupation: ')

    #check for duplicates
    sql_str = "SELECT * from Simpson_info where NAME='{}'".format(name)
    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()
    if len(rows)>0:
        print 'This character already exists.'
        response = raw_input('Add a different character? y/n    :')
        if response == 'y':                       
            newCharacters()

    else:
        
        #create a string with all the raw input
        val_str = "'{}','{}',{},'{}'".format(name, gender, age, occupation)

        #update the table with the raw input
        conn.execute('INSERT INTO Simpson_info (NAME, GENDER, AGE, OCCUPATION) values ({});'.format(val_str))
        conn.commit()
        print (name +' has been added to the database.')
        

def viewAll():
    #create a sql string
    sql_str = "SELECT * FROM Simpson_info"
    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()
    printData(rows)

def viewDetails():
    print "\nViewing Character Details"

    #take name input
    name = raw_input('Enter the Character\'s name: ')
    sql_str = ('SELECT * from Simpson_info where NAME="{}"').format(name)
    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()

    if len(rows) == 0:
        #There is no data in the array
        print 'No Records Found'
    else:
        #there is data
        printData(rows)

def selectChange(rows):
    for row in rows:
        
        print ('\nWhich would you like to change?')
        print ('1. Change Name from '+row[1])
        print ('2. Change Gender from '+row[2])
        print ('3. Change Age from '+str(row[3]))
        print ('4. Change Occupation from ' +row[4])
        
    selection = raw_input('Enter the number of the attribute you want to change:    ')
        
    if selection == '1':
        newName = raw_input('Enter the new name for '+row[1]+":    ")
        sql_str = ("UPDATE Simpson_info set NAME ='{}' where ID = '{}'").format(newName, row[0])
        conn.execute(sql_str)
        conn.commit()
        print (row[1] + ' is updated from '+row[1] +' to'+ newName + '.')
    elif selection == '2':
        newGender = raw_input('Enter the new gender for '+row[1]+":    ")
        sql_str = ("UPDATE Simpson_info set GENDER ='{}' where ID = '{}'").format(newGender, row[0])
        conn.execute(sql_str)
        conn.commit()
        print (row[1] + ' is updated from '+row[2] +' to '+ newGender + '.')
    elif selection == '3':
        newAge = raw_input('Enter the new age for '+row[1]+":    ")
        sql_str = ("UPDATE Simpson_info set AGE ={} where ID = '{}'").format(newAge, row[0])
        conn.execute(sql_str)
        conn.commit()
        print (row[1] + ' is updated from '+ str(row[3])+' to '+ str(newAge) + ' years old.')
    elif selection == '4':
        newOcc = raw_input('Enter the new occupation for '+row[1]+":    ")
        sql_str = ("UPDATE Simpson_info set OCCUPATION ='{}' where ID = '{}'").format(newOcc, row[0])
        conn.execute(sql_str)
        conn.commit()
        print (row[1] + ' is updated from '+row[4] +' to be a '+ newOcc + '.')
    else:
        print ('Invalid selection. Change Cancelled')


def changeCharacter():
    print '\nChanging a Character'
    #take user input
    name = raw_input('Which character do you want to change?  :')
    #create the sql string
    sql_str = ("SELECT * from Simpson_info where NAME = '{}'").format(name)

    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()

    
    if len(rows)==0:
        #No character with that name
        print 'No Records Found'
    elif len(rows)==1:
        #change the character
        printData(rows)
        confirm = raw_input('Please Confirm you want to change '+name+': y/n    :')
        if confirm == 'y':
            selectChange(rows)
        else:
            print ('Change Cancelled.')
    else:
        print 'More than one record found...'
        printData(rows)
        change_id = raw_input('Type the ID of the character to change:  ')
        sql_str = ('UPDATE from Simpson_info where ID = {}').format(change_id)
        confirm = raw_input('Please Confirm you want to change '+name+' ID# ' +change_id+' y/n    :')
        if confirm == 'y':
            selectChange(rows)
        else:
            print('Delete cancelled.')


def deleteCharacter():
    print '\nDeleting a Character'
    #take user input
    name = raw_input('Which character do you want to delete?  :')
    #create the sql string
    sql_str = ("SELECT * from Simpson_info where NAME = '{}'").format(name)

    cursor = conn.execute(sql_str)
    rows = cursor.fetchall()
    if len(rows)==0:
        #No character with that name
        print 'No Records Found'
    elif len(rows)==1:
        #delete the character
        deleteConfirm = raw_input('Please Confirm you want to delete '+name+': y/n    :')
        if deleteConfirm == 'y':
            sql_str = ("DELETE from Simpson_info where NAME = '{}'").format(name)
            conn.execute(sql_str)
            conn.commit()
            print (name + ' is deleted.')
        else:
            print ('Delete Cancelled.')
    else:
        print 'More than one record found...'
        printData(rows)
        change_id = raw_input('Type the ID of the character to delete:  ')
        sql_str = ('DELETE from Simpson_info where ID = {}').format(change_id)
        deleteConfirm = raw_input('Please Confirm you want to delete '+name+' ID# ' +change_id+' y/n    :')
        if deleteConfirm == 'y':
            conn.execute(sql_str)
            conn.commit()
            print(name + " ID # "+change_id+" is deleted.")
        else:
            print('Delete cancelled.')

def options():
    #Print out the options
    print '\nWhat would you like to do?'
    print '1. Add a new character'
    print '2. View all characters'
    print '3. Search for a character'
    print '4. Delete a character'
    print '5. Change a character'
    print '6. Exit'

    #Ask user what they want to do
    response = raw_input('Enter number: ')
    if response == '1':
      
        newCharacters()
    elif response == '2':
       
        viewAll()
    elif response == '3':
       
        viewDetails()
    elif response == '4':
        
        deleteCharacter()
    elif response == '5':

        changeCharacter()
    elif response == '6':
        print '\n'
        print 'Exiting the program'
        return

def mainLoop():
    in_loop = True
    while in_loop == True:
        #Run Options Function
        print '\n'
        options()
        #ask user if they want to continue
        again = raw_input('Would you like to do something else? y/n    :')
        if again !='y':
            in_loop = False

mainLoop()

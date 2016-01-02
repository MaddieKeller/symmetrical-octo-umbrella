epic_programmer_dict={'tim berners-lee':['tbl@gmail.com',111],
                        'guido van rossum':['gvr@gmail.com',222],
                      'linus torvalds':['lt@gmail.com',333]}


#makes our search function
def searchPeople(personsName):

    try:
        #code that searchs for the name and out puts the resutl
        personsInfo = epic_programmer_dict[personsName]
        print 'Name: ' + personsName.title()
        print 'Email: ' + str(personsInfo[0])
        print 'Number: ' + str(personsInfo[1])

    except:
        #code that gets run if there are errors
        print 'No Information found for that name'

#initial search
searchAgain = True
while searchAgain == True:
    personsName = raw_input('Please enter a name:').lower()
    searchPeople(personsName)

    searchAgain = False

#see if they want to search again
    wantMore = raw_input('Search again? (y/n)')
    if wantMore =='y':
        searchAgain = True
    elif wantMore=='n':
        searchAgain = False
    else:
        print ("I don't understand what you mean")
        searchAgain =False

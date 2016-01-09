import urllib2, os, csv, progressbar
from bs4 import BeautifulSoup

#open webpage
webpage = urllib2.urlopen("http://inadaybooks.com/justiceleague")

#convert the webpage into something readable and pull the list of members
soup= BeautifulSoup(webpage,"html.parser")
divContainer = soup.find('div',{'id':'container'})
divBlock = divContainer.findAll('div',{'class':'block'})
divSep = divBlock[3].findAll('div',{'class':'separator'})
members = divSep[3].findAll('a')
nMembers = len(members)
bar = progressbar.ProgressBar(nMembers)

#create a CSV file to dump the data into
currentPath = os.path.dirname(os.path.abspath('webScrapPythonExercises.py'))
outputCsv = currentPath + '/JusticeLeagueWebScrap.csv'
csvFile = open(outputCsv,'wb')
writer = csv.writer(csvFile,delimiter = ',')


#function to pull the member data from each individual page
def extractMData(webpage):
    soup = BeautifulSoup(webpage,"html.parser") #pull the full html
    divContainer = soup.find('div',{'id':'container'}) #pull the container id
    divBlock = divContainer.findAll('div',{'class':'block'})#pull the block class
    info = divBlock[3] #narrow down to the fourth block

    findLeft = info.findAll('div',{'class':'info_left'})#pull the column names
    findRight = info.findAll('div',{'class':'info_right'})#pull the info

    #loop through both arrays and get just the text and drop the html tag
    textLeftArray = []
    textRightArray = []
    for i in range(0,len(findLeft)):
        textLeft = findLeft[i].get_text()
        textRight = findRight[i].get_text()
        textLeftArray.append(textLeft)
        textRightArray.append(textRight)
        #row = (textLeft,textRight)
        #riter.writerow(row)
    return (textLeftArray, textRightArray)


count = 0
#loop through the members list to pull out the individual members
for member in bar(members):
    href = member.get('href')
    url = "http://inadaybooks.com/justiceleague/"+href
    mPage = urllib2.urlopen(url)
    data = extractMData(mPage)
    
    if count == 0:
        writer.writerow(data[0])
    writer.writerow(data[1])
    count += 1

    


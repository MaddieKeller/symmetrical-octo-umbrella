import sqlite3
import datetime
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


global conn, cursor, graphArray

def main():
    global conn, cursor, graphArray
    conn = sqlite3.connect('tutorial.db')

    cursor = conn.cursor()

    date = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))

    #dataEntry('stuffToPlot',time.time(),date,'Python Sentiment',7)

    graphArray = []

    readData('Python Sentiment')

    datestamp, value = np.loadtxt(graphArray, delimiter=',',unpack=True, converters={0:mdates.strpdate2num("%Y-%m-%d %H:%M:%S")})
    fig = plt.figure()
    rect = fig.patch
    axl = fig.add_subplot(1,1,1, axisbg='white')
    plt.plot_date(x=datestamp, y= value, fmt='b-',label = 'value',linewidth = 2)
    plt.show()

def readData(wordUsed):
    for row in cursor.execute("SELECT * FROM stuffToPlot WHERE keyword = '{}';".format(wordUsed)):
        startingInfo = str(row).replace(')','').replace('(','').replace('u\'','').replace("'","")
        splitInfo = startingInfo.split(',')
        graphArrayAppend = splitInfo[2]+','+splitInfo[4]
        graphArray.append(graphArrayAppend)

def dataEntry(table, unix, datetime, keyword, value):
    cursor.execute("INSERT INTO {} (unix, datestamp, keyword, value) VALUES({},'{}', '{}',{});".format(table, unix, datetime, keyword, value))
    conn.commit()

def tableCreate():
    #cursor.execute(DROP TABLE stuffToPlot)
    cursor.execute("CREATE TABLE stuffToPlot (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, unix REAL, datestamp TEXT, keyword TEXT, value REAL);")

if __name__ == '__main__': main()
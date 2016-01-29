import shutil, os
from datetime import datetime, timedelta
from pytz import timezone

'''
    Scenario: Users create or edit files throughout the day. Any new files or files edited
    within last 24 hours need to be copied to a specific destination

'''

def detectAge(file, destination,prevTime):
    fileStat = os.stat(file)
    seconds = fileStat.st_mtime
    portland_tz = timezone("US/Pacific")
    fileAge = portland_tz.localize(datetime.fromtimestamp(seconds))
    currentTime = portland_tz.localize(datetime.now())
    #making sure it doesn't get passed blank value
    if prevTime == '':
        prevTime = currentTime-timedelta(hours=24)
    if fileAge<=currentTime and fileAge>=prevTime:
        copyFile(file, destination)
        print("File Age: " + fileAge.strftime('%m/%d/%Y %H:%M %Z%z'))

def copyFile(file, destination):
    shutil.copy2(file,destination)

def getFiles(source, destination,prevTime):
    fileNames = os.listdir(source)
    for file in fileNames:
        fullpath = os.path.join(source,file)
        detectAge(fullpath, destination,prevTime)


def main():
    portland_tz = timezone("US/Pacific")
    portland_dt = portland_tz.localize(datetime.now())
    print(portland_dt.strftime('%d/%m/%Y %H:%M %Z%z'))
    print(portland_dt-timedelta(hours=24))
    getFiles('c:/users/madison/desktop/folder b','c:/users/madison/desktop/folder a',
             portland_dt-timedelta(hours=24))

if __name__ == '__main__':main()
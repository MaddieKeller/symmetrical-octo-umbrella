import shutil, os
from datetime import datetime, timedelta

'''
    Scenario: Users create or edit files throughout the day. Any new files or files edited
    within last 24 hours need to be copied to a specific destination

'''
def detectAge(file):
    fileStat = os.stat(file)
    seconds = fileStat.st_mtime
    fileAge = datetime.fromtimestamp(seconds)
    currentTime = datetime.now()
    prevTime = currentTime- timedelta(hours=24)

    if fileAge<=currentTime and fileAge>=prevTime:
        copyFile(file)


def copyFile(file):
    destination = 'c:/users/madison/desktop/folder a'
    shutil.copy2(file,destination)

def getFiles(source):
    fileNames = os.listdir(source)
    for file in fileNames:
        fullpath = os.path.join(source,file)
        detectAge(fullpath)


def main():
    getFiles('c:/users/madison/desktop/folder b')

if __name__ == '__main__':main()
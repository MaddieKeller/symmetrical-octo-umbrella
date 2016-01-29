import shutil, os
'''
Scenario:Employer wants a program to move all txt files from one folder to another

Objective:Move the files, print out each file path that got moved, clear files out of the original file

'''

def moveFile(src, dest):
    print(src + " moved to " + dest)
    shutil.move(src, dest)

def main():

    sourceFile = 'c:\users\madison\desktop\Folder A'
    destFile = 'c:\users\madison\desktop\Folder B'
    names = os.listdir(sourceFile)

    for name in names:
        srcname = os.path.join(sourceFile,name)
        moveFile(srcname, destFile)


if __name__=='__main__': main()
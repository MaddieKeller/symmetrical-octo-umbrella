import sqlite3

global conn, cursor

conn = sqlite3.connect('webpage.db')
cursor = conn.cursor()

def getContent():
    content = conn.execute("SELECT * FROM page_content")
    return content

def createTable():
    global conn
    conn.execute("CREATE TABLE page_content\
         (content_id INTEGER PRIMARY KEY AUTOINCREMENT, \
            content_desc VARCHAR(255), \
            content VARCHAR)")

def getLine(line):
    info = conn.execute("SELECT content FROM page_content WHERE content_id = ".format(line))
    return info

def createLines(desc, content):
    global conn
    conn.execute("INSERT INTO page_content (content_desc, content) VALUES ('{}', '{}');".format(desc,content))
    conn.commit()


def main():
    global conn, cursor
    getContent()
    conn.close()
    

if __name__ == '__main__': main()
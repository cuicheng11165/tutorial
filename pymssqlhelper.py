import pyodbc

class pymssqlhelper(object):
    """description of class"""

    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost\s2012;DATABASE=AliyunDBSource;UID=sa;PWD=1qaz2wsxE')


    @staticmethod
    def insertpage(url,author,title,stream):
        print url
        print author
        print title

        cursor = pymssqlhelper.cnxn.cursor()
        cursor.callproc('InsertPage',[url ,author , title , stream])
        pymssqlhelper.cnxn.commit()
        print 'test3'



import pyodbc

class pymssqlhelper(object):
    """description of class"""

    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost\s2012;DATABASE=AliyunDBSource;UID=sa;PWD=1qaz2wsxE;autocommit=True')


    @staticmethod
    def insertpage(url,author,title,stream):
        cursor = pymssqlhelper.cnxn.cursor()
        cursor.execute("select * from ItemUserData where Url='{}'".format(url))
        row = cursor.fetchone()
        if not row:
            cursor.execute("exec InsertPage @Url = ?, @Author = ?, @Title = ?, @Stream = ?",url,author,title,stream)
        cursor.close()
        pymssqlhelper.cnxn.commit()



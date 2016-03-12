import pyodbc

class pymssqlhelper(object):
    """description of class"""

    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=testdb;UID=me;PWD=pass')


    @staticmethod
    def test3(url,author,title,stream):
        cursor = cnxn.cursor()
        cursor.execute('{call InsertPage (' + url + author + title + stream + ')}')
        print 'test3'



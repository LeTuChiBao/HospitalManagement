import pyodbc

class MSSQLConnection:
    def __init__(self, drive = 'SQL Server',
                 server='MSI\\SQLEXPRESS',
                 database='DoAn',
                 username='', password=''):
        self.drive = drive
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = pyodbc.connect(f'DRIVER={self.drive};'
                                             f'SERVER={self.server};'
                                             f'DATABASE={self.database};'
                                             f'UID={self.username};'
                                             f'PWD={self.password}')
            print("Connection successful")
        except Exception as e:
            print("Error in connection: ", e)

    def query(self, sql,values =None):
        try:
            cursor = self.connection.cursor()
            if values:
                cursor.execute(sql,values)
            else:
                cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            print(f"Error deleting data: {str(e)}")
            self.connection.rollback()

    def update(self, sql,values):
        try:
            cursor = self.connection.cursor()
            if values:
                cursor.execute(sql, values)
            else:
                cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print(f"Error deleting data: {str(e)}")
            self.connection.rollback()
        finally:
            cursor.close()


    def insert(self, sql, values):
        try:
            cursor = self.connection.cursor()
            if values:
                cursor.execute(sql, values)
            else:
                cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print(f"Error deleting data: {str(e)}")
            self.connection.rollback()
        finally:
            cursor.close()

    def delete(self, sql,values=None):
        try:
            cursor = self.connection.cursor()
            if values:
                cursor.execute(sql,values)
            else:
                cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print(f"Error deleting data: {str(e)}")
            self.connection.rollback()
        finally:
            cursor.close()

    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection closed")


if __name__ == '__main__':
    SqlSever = MSSQLConnection()
    SqlSever.connect()
    Query = "select * from hospital"
    Result = SqlSever.query(Query)
    print(Result)
    SqlSever.close()


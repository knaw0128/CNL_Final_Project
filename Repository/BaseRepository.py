from IBaseRepository import IBaseRepository
import pymysql

class BaseRepository(IBaseRepository):
    def __init__(self, repoType) -> None:
        super().__init__(repoType)
        self.db_settings = {
            "host": "127.0.0.1",
            "port": 3306,
            "user": "root",
            "password": "資料庫管理員密碼",
            "db": type(repoType),
            "charset": "utf8"
        }
        self.table_name = type(repoType)
        self.connect_db = pymysql.connect(**self.db_settings)

    def Create(self, newData: object):
        if type(newData) != self.table_name:
            raise TypeError("Wrong storing type")
        insert_command = f"INSERT INTO {self.table_name}" + " (%s)VALUES(%s)"
        col = ""
        value = ""
        for key in newData.__dict__.keys():
            col = f"{col}{key}, "
            value = f"{value}{newData[key]}, "
        insert_command.format(col[:-2], value[:-2])
        try:
            with self.connect_db.cursor() as cursor:
                cursor.execute(insert_command)
                self.connect_db.commit()
            return 1
        except:
            return -1
            
    def Read(self, primarykey):
        return super().Read(primarykey)
    
    def Update(self, newData, primarykey):
        return super().Update(newData, primarykey)
    
    def Delete(self, primarykey):
        return super().Delete(primarykey)
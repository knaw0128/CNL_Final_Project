from .IBaseRepository import IBaseRepository
import pymysql

class BaseRepository(IBaseRepository):
    def __init__(self, repoType) -> None:
        super().__init__(repoType)
        self.db_settings = {
            "host": "140.112.29.203",
            "port": 3306,
            "user": "cnl",
            "password": "cnlfinal",
            "db": "appdb",
            "charset": "utf8"
        }
        self.table_name = repoType.__name__
        self.connect_db = pymysql.connect(**self.db_settings)

    def Create(self, newData):
        if type(newData).__name__ != self.table_name:
            raise TypeError("Wrong storing type")
        
        command_string = f"INSERT INTO {self.table_name}"
        col = ""
        value = ""
        for key in newData.__dict__.keys():
            col = f"{col}{key}, "
            value = f"{value}\'{newData.__dict__[key]}\', "
        command_string += f" ({col[:-2]}) VALUES ({value[:-2]});"

        try:
            with self.connect_db.cursor() as cursor:
                cursor.execute(command_string)
                self.connect_db.commit()
            return 1
        except pymysql.MySQLError as e:
            print('Got error {!r}, errno is {}'.format(e, e.args[0]))
            return -1
            
    def Read(self, primarykey):
        if type(primarykey).__name__ != self.table_name:
            raise TypeError("Wrong storing type")
        
        command_string = f"SELECT * FROM {self.table_name} "
        condition = "WHERE "
        for key in primarykey.__dict__.keys():
            if primarykey.__dict__[key] == None:
                continue
            condition = f"{condition} {key}=\'{primarykey.__dict__[key]}\' AND "
        
        if condition == "WHERE ":
            command_string += ";"
        else:
            command_string += f"{condition[:-4]};"

        try:
            with self.connect_db.cursor() as cursor:
                cursor.execute(command_string)
                all_data = cursor.fetchall()
                result = []
                for data in all_data:
                    now = {}
                    for idx, key in enumerate(primarykey.__dict__.keys()):
                        now[key] = data[idx]
                    result.append(type(primarykey)(**now))
            return result
        except pymysql.MySQLError as e:
            print('Got error {!r}, errno is {}'.format(e, e.args[0]))
            return -1
    
    def Update(self, newData, primarykey):
        if type(newData).__name__ != self.table_name:
            raise TypeError("Wrong storing type")
        
        command_string = f"UPDATE {self.table_name} SET "
        new_setting = ""
        for key in newData.__dict__.keys():
            if newData.__dict__[key] == None:
                continue
            new_setting = f"{new_setting} {key}=\'{newData.__dict__[key]}\', "
        
        condition = ""
        for key in primarykey.__dict__.keys():
            if primarykey.__dict__[key] == None:
                continue
            condition = f"{condition} {key}=\'{primarykey.__dict__[key]}\' AND "
        command_string += f"{new_setting[:-2]} WHERE {condition[:-4]};"
        print(command_string)
        try:
            with self.connect_db.cursor() as cursor:
                cursor.execute(command_string)
                self.connect_db.commit()
            return 1
        except pymysql.MySQLError as e:
            print('Got error {!r}, errno is {}'.format(e, e.args[0]))
            return -1
    
    def Delete(self, primarykey):
        if type(primarykey).__name__ != self.table_name:
            raise TypeError("Wrong storing type")
        
        command_string = f"DELETE FROM {self.table_name} WHERE "
        condition = ""
        for key in primarykey.__dict__.keys():
            if primarykey.__dict__[key] == None:
                continue
            condition = f"{condition}{key}=\'{primarykey.__dict__[key]}\' AND "
        command_string += f"{condition[:-4]};"

        print(command_string)
        try:
            with self.connect_db.cursor() as cursor:
                cursor.execute(command_string)
                self.connect_db.commit()
            return 1
        except pymysql.MySQLError as e:
            print('Got error {!r}, errno is {}'.format(e, e.args[0]))
            return -1
    


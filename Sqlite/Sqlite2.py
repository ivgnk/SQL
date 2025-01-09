'''
2017 Python: Работа с базой данных, часть 1/2: Используем DB-API
https://habr.com/ru/articles/321510/

Данные из https://github.com/lerocha/chinook-database/blob/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite

Описание демо-базы данных
https://www.sqlitetutorial.net/sqlite-sample-database/

01.09.2023 Воссоздание базы данных Chinook
'''

# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3
from Sqlite_const import *
from pfile import *
from pstring import *

class MySqlite3_Chinook():
    def __init__(self, work_name:str):
        self.clear_db_file(work_name = work_name)
        self.db_name = work_name
        # Создаем соединение с нашей базой данных
        # В нашем примере у нас это просто файл базы
        self.conn = sqlite3.connect(self.db_name)
        # Создаем курсор - это специальный объект который делает запросы и получает их результаты
        self.cursor = self.conn.cursor()
        self.clear_all_tables()
        print('Object initialized')

    def work_frame(self):
        self.cursor.execute("PRAGMA foreign_keys = off;")
        self.cursor.execute("BEGIN TRANSACTION;")

        self.cursor.execute("COMMIT TRANSACTION;")
        self.cursor.execute("PRAGMA foreign_keys = on;")

    def clear_db_file(self, work_name:str):
        '''
        https://sky.pro/media/udalenie-fajla-ili-papki-v-python/
        '''
        delete_file(work_name)

    def clear_all_tables(self):
        '''
        https://stackoverflow.com/questions/38672579/delete-all-tables-from-sqlite-database
        '''
        # ------- 1 вариант
        for table_name in tables_list:
            self.cursor.execute("DROP TABLE IF EXISTS " + table_name+';')




class_exem = MySqlite3_Chinook(my_db_fn)
class_exem.work_frame()

# class_exem = MySqlite3(ini_fn)
# class_exem.work(5,'Начальный вариант')

'''
2017 Python: Работа с базой данных, часть 1/2: Используем DB-API
https://habr.com/ru/articles/321510/

Данные из https://github.com/lerocha/chinook-database/blob/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite

Описание демо-базы данных
https://www.sqlitetutorial.net/sqlite-sample-database/
'''

# Импортируем библиотеку, соответствующую типу нашей базы данных
import sqlite3
import os
from Sqlite_const import *

class MySqlite3():
    def __init__(self, work_name:str):
        self.db_name = work_name
        # Создаем соединение с нашей базой данных
        # В нашем примере у нас это просто файл базы
        self.conn = sqlite3.connect(self.db_name)
        # Создаем курсор - это специальный объект который делает запросы и получает их результаты
        self.cursor = self.conn.cursor()
        print('Object initialized')

    def work(self, num:int, info:str=''):
        self.cursor.execute(f"SELECT Name FROM Artist ORDER BY Name LIMIT {num}")
        # Получаем результат сделанного запроса
        results = self.cursor.fetchall()
        print('\n',info)
        print(results)   # [('A Cor Do Som',), ('Aaron Copland & London Symphony Orchestra',), ('Aaron Goldberg',)]

class MySqlite3_ext:
    '''
    Примеры работы с классами в Python
    https://pythonru.com/primery/primery-raboty-s-klassami-v-python
    '''
    def __init__(self, ini_name, work_name):
        print('Inside Constructor')
        # есть ли что-то типа encoding при вызове os.system
        # https://ru.stackoverflow.com/questions/1329129/есть-ли-что-то-типа-encoding-при-вызове-os-system
        os.system("chcp 65001 > nul")
        try:
            the_command = f'copy {ini_name} {work_name}  > dat.dat'
            print(the_command)
            os.system(the_command)
        except:
            print('Ошибка копирования')
        self.db_name = work_name
        # Создаем соединение с нашей базой данных
        # В нашем примере у нас это просто файл базы
        self.conn = sqlite3.connect(self.db_name)
        # Создаем курсор - это специальный объект который делает запросы и получает их результаты
        self.cursor = self.conn.cursor()
        print('Object initialized')

    def the_query(self, num:int, info:str=''):
        # Делаем SELECT запрос к базе данных, используя обычный SQL-синтаксис
        self.cursor.execute(f"SELECT Name FROM Artist ORDER BY Name LIMIT {num}")
        # Получаем результат сделанного запроса
        results = self.cursor.fetchall()
        print('\n',info)
        print(results)   # [('A Cor Do Som',), ('Aaron Copland & London Symphony Orchestra',), ('Aaron Goldberg',)]

    def work(self):
        # НАШ КОД РАБОТЫ С БАЗОЙ ДАННЫХ
        # ---------------- (1)
        self.the_query(5,'before commit')
        # ---------------- (2)
        # Делаем INSERT запрос к базе данных, используя обычный SQL-синтаксис
        self.cursor.execute("insert into Artist values (Null, 'A Aagrh!') ")
        # Если мы не просто читаем, но и вносим изменения в базу данных - необходимо сохранить транзакцию
        self.conn.commit()
        #  Проверяем результат
        self.the_query(5, 'after commit')

        # ---------------- (3)
        # Использование курсора как итератора
        c_e = self.cursor.execute('SELECT Name from Artist ORDER BY Name LIMIT 3')
        print('----------(3)----------Использование курсора как итератора')
        for row in c_e:
            print(row)
        # ('A Cor Do Som',)
        # ('Aaron Copland & London Symphony Orchestra',)
        # ('Aaron Goldberg',)

        # ---------------- (3)
    def __del__(self):
        '''
        Деструктор в Python: уничтожение объектов
        https://pythonist.ru/destruktor-v-python-unichtozheniye-obektov/
        '''
        # Не забываем закрыть соединение с базой данных
        self.conn.close()
        print('Inside destructor')
        print('Object destroyed')


class_exem = MySqlite3_ext(ini_fn, wrk_fn)
class_exem.work()

# class_exem = MySqlite3(ini_fn)
# class_exem.work(5,'Начальный вариант')

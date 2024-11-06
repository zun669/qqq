from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, QTableWidgetItem # это базовый класс диалогового окна
)

import sqlite3

class Operator(QDialog):
    def __init__(self, table):        
        super(Operator, self).__init__()
        print("Проверка открытия страницы оператора")
        self.tableWidget_Operator = table
        print(self.tableWidget_Operator)
        self.vivod()
    def vivod(self):
        conn = sqlite3.connect("uchet.db") # подключение к базе данных в () изменить на название своей БД
        cur = conn.cursor()# создаём переменную для хранения запросов
        zayavki=cur.execute('SELECT * FROM requests') # получаем тип пользователя, логин и пароль которого был введен
        print(zayavki)
        #typeUser = cur.fetchone() # получает только один тип пользователя
        name_stolba = [xz[0] for xz in zayavki.description] # вывод названия столбцов
        print(name_stolba)
        self.tableWidget_Operator.setColumnCount(len(name_stolba))# считает кол-во столбцов
        self.tableWidget_Operator.setHorizontalHeaderLabels(name_stolba)# вместо цифр название столбцов
        dantable = cur.fetchall()# получили данные но они не структурированны 
        for i, row in enumerate(dantable): #цикл по строчкам
            self.tableWidget_Operator.setRowCount(self.tableWidget_Operator.rowCount() +1) # добавил пусте строки в нужном колличестве 
            for l, cow in enumerate(row): #начинает по ячейкам заносить данные 
                self.tableWidget_Operator.setItem(i, l, QTableWidgetItem(str(cow)))
        print(dantable)
        self.tableWidget_Operator.resizeColumnsToContents()
        conn.commit() # сохраняет в подключении запросы
        conn.close() # закрываем подключение

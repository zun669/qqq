from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, QTableWidgetItem # это базовый класс диалогового окна
)

import sqlite3

class Manager(QDialog):
    def __init__(self, table):        
        super(Manager, self).__init__()
        print("Проверка открытия страницы менеджера")
        self.tableWidget_Manager = table
        print(self.tableWidget_Manager)
        self.vivod()
    def vivod(self):
        conn = sqlite3.connect("uchet.db")
        cur = conn.cursor()
        zayavki = cur.execute('SELECT * FROM requests')
        print(zayavki)
        name_stolba = [xz[0] for xz in zayavki.description]
        print(name_stolba)
        self.tableWidget_Manager.setColumnCount(len(name_stolba))
        self.tableWidget_Manager.setHorizontalHeaderLabels(name_stolba)
        dantable = cur.fetchall()
        for i, row in enumerate(dantable):
            self.tableWidget_Manager.setRowCount(self.tableWidget_Manager.rowCount() +1)
            for l,cow in enumerate(row):
                self.tableWidget_Manager.setItem(i, l, QTableWidgetItem(str(cow)))
        print(dantable)
        self.tableWidget_Manager.resizeColumnsToContents()
        conn.commit()
        conn.close()        
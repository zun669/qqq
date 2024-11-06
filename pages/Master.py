from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, QTableWidgetItem # это базовый класс диалогового окна
)

import sqlite3

class Master(QDialog):
    def __init__(self, table):        
        super(Master, self).__init__()
        print("Проверка открытия страницы мастера")
        self.tableWidget_Master = table
        print(self.tableWidget_Master)
        self.vivod()
    def vivod(self):
        conn = sqlite3.connect("uchet.db")
        cur = conn.cursor()
        zayavki = cur.execute('SELECT * FROM requests')
        print(zayavki)
        name_stolba = [xz[0] for xz in zayavki.description]
        print(name_stolba)
        self.tableWidget_Master.setColumnCount(len(name_stolba))
        self.tableWidget_Master.setHorizontalHeaderLabels(name_stolba)
        dantable = cur.fetchall()
        for i, row in enumerate(dantable):
            self.tableWidget_Master.setRowCount(self.tableWidget_Master.rowCount() +1)
            for l, cow in enumerate(row):
                self.tableWidget_Master.setItem(i, l, QTableWidgetItem(str(cow)))
        print(dantable)
        self.tableWidget_Master.resizeColumnsToContents()
        conn.commit()
        conn.close()        
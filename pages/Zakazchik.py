from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (    
    QDialog, QTableWidgetItem # это базовый класс диалогового окна
)

import sqlite3

class Zakazchik(QDialog):
    def __init__(self, table):        
        super(Zakazchik, self).__init__()
        print("Проверка открытия страницы заказчика")
        self.tableWidget_Zakazchik = table
        print(self.tableWidget_Zakazchik)
        self.vivod()
    def vivod(self):
        conn = sqlite3.connect("uchet.db")
        cur = conn.cursor()
        zayavki=cur.execute('SELECT * FROM requests')
        print(zayavki)
        name_stolba = [xz[0] for xz in zayavki.description]
        print(name_stolba)
        self.tableWidget_Zakazchik.setColumnCount(len(name_stolba))
        self.tableWidget_Zakazchik.setHorizontalHeaderLabels(name_stolba)
        dantable = cur.fetchall()
        for i, row in enumerate(dantable):
            self.tableWidget_Zakazchik.setRowCount(self.tableWidget_Zakazchik.rowCount() +1)
            for l, cow in enumerate(row):
                self.tableWidget_Zakazchik.setItem(i, l, QTableWidgetItem(str(cow)))
        print(dantable)
        self.tableWidget_Zakazchik.resizeColumnsToContents()
        conn.commit()
        conn.close()        
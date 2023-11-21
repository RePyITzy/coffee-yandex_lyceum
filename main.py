from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem
from PyQt5 import uic as QInterface

import sqlite3
import sys


class CoffeeViewer(QMainWindow):
  def __init__(self):
    super(CoffeeViewer, self).__init__()
    QInterface.loadUi('main.ui', self)

    self.loadCoffeeData(self.tableWidget)

  def loadCoffeeData(self, parent):
    parent.setRowCount(0)
    headers = ['ID', 'Сорт', 'Обжарка', 'Кофе', 'Вкус', 'Цена кофе', 'Объем кофе']
    parent.setColumnCount(len(headers))
    parent.setHorizontalHeaderLabels(headers)
    parent.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    database = sqlite3.connect('coffee.sqlite')
    cursor = database.cursor()

    coffee_data = cursor.execute('SELECT * FROM coffees').fetchall()
    for y, coffee in enumerate(coffee_data):
      parent.setRowCount(parent.rowCount() + 1)
      for x, description in enumerate(coffee):
        parent.setItem(y, x, QTableWidgetItem(str(description)))
    
    

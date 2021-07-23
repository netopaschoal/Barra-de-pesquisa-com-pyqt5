from PyQt5 import  uic,QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItem, QStandardItemModel

carros = ('Gol', 'Celta', 'Corsa', 'Uno', 'Fox', 'Cruze', 'Brasilia', 'Saveiro', 'Fusca', 'Hilux', 'Onix')
modelo = QStandardItemModel(len(carros),1)
modelo.setHorizontalHeaderLabels(['Carros'])

for linha, carro in enumerate(carros):    # [(1, 'Gol'), (2,'Celta') ]     
    elemento = QStandardItem(carro)
    modelo.setItem(linha, 0, elemento)

filtro = QSortFilterProxyModel()
filtro.setSourceModel(modelo)
filtro.setFilterKeyColumn(0)
#filtro.setFilterCaseSensitivity(Qt.CaseInsensitive)

app=QtWidgets.QApplication([])
tela=uic.loadUi("layout.ui")
tela.tableView.setModel(filtro)
tela.tableView.horizontalHeader().setStyleSheet("font-size: 35px;color: rgb(50, 50, 255);")
tela.lineEdit.textChanged.connect(filtro.setFilterRegExp)

tela.show()
app.exec()
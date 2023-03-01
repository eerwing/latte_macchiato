import sys
import sqlite3
from PyQt5 import uic
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(828, 400)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 808, 350))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.add_button = QtWidgets.QPushButton(Form)
        self.add_button.setGeometry(QtCore.QRect(720, 365, 100, 30))
        self.add_button.setObjectName("add_button")
        self.change_button = QtWidgets.QPushButton(Form)
        self.change_button.setGeometry(QtCore.QRect(610, 365, 100, 30))
        self.change_button.setObjectName("change_button")
        self.not_aligned = QtWidgets.QLabel(Form)
        self.not_aligned.setGeometry(QtCore.QRect(10, 365, 300, 30))
        self.not_aligned.setText("")
        self.not_aligned.setObjectName("not_aligned")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add_button.setText(_translate("Form", "Добавить"))
        self.change_button.setText(_translate("Form", "Изменить"))


class Ui_Form_2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(440, 380)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 25, 110, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 75, 110, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 125, 110, 20))
        self.label_3.setObjectName("label_3")
        self.type = QtWidgets.QComboBox(Form)
        self.type.setGeometry(QtCore.QRect(140, 120, 290, 30))
        self.type.setObjectName("type")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 175, 110, 20))
        self.label_4.setObjectName("label_4")
        self.taste = QtWidgets.QLineEdit(Form)
        self.taste.setGeometry(QtCore.QRect(140, 170, 290, 30))
        self.taste.setObjectName("taste")
        self.button = QtWidgets.QPushButton(Form)
        self.button.setGeometry(QtCore.QRect(310, 320, 120, 40))
        self.button.setText("")
        self.button.setObjectName("button")
        self.sort = QtWidgets.QComboBox(Form)
        self.sort.setGeometry(QtCore.QRect(140, 20, 290, 30))
        self.sort.setObjectName("sort")
        self.roasting = QtWidgets.QComboBox(Form)
        self.roasting.setGeometry(QtCore.QRect(140, 70, 290, 30))
        self.roasting.setObjectName("roasting")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 225, 110, 20))
        self.label_5.setObjectName("label_5")
        self.price = QtWidgets.QLineEdit(Form)
        self.price.setGeometry(QtCore.QRect(140, 220, 290, 30))
        self.price.setObjectName("price")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 275, 110, 20))
        self.label_6.setObjectName("label_6")
        self.volume = QtWidgets.QLineEdit(Form)
        self.volume.setGeometry(QtCore.QRect(140, 270, 290, 30))
        self.volume.setObjectName("volume")
        self.error = QtWidgets.QLabel(Form)
        self.error.setGeometry(QtCore.QRect(10, 320, 221, 40))
        self.error.setText("")
        self.error.setObjectName("error")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Название сорта"))
        self.label_2.setText(_translate("Form", "Степень обжарки"))
        self.label_3.setText(_translate("Form", "Молотый/в зернах"))
        self.label_4.setText(_translate("Form", "Описание вкуса"))
        self.label_5.setText(_translate("Form", "Цена"))
        self.label_6.setText(_translate("Form", "Объем упаковки"))



class Show_Coffee_Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Виды кофе')
        self.con = sqlite3.connect("coffee.db")
        info = list(map(list, self.con.cursor().execute("SELECT * FROM info").fetchall()))
        self.tableWidget.setRowCount(len(info))
        self.tableWidget.setColumnCount(len(info[0]))
        for i, row in enumerate(info):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.setHorizontalHeaderLabels(
            ['id', 'sort', 'roasting', 'ground/grain', 'taste', 'price', 'packaging volume'])
        self.tableWidget.resizeColumnsToContents()
        self.change_button.clicked.connect(self.open_change_coffee)
        self.add_button.clicked.connect(self.open_add_coffee)

    def update(self):
        info = list(map(list, self.con.cursor().execute("SELECT * FROM info").fetchall()))
        self.tableWidget.setRowCount(len(info))
        self.tableWidget.setColumnCount(len(info[0]))
        for i, row in enumerate(info):
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.setHorizontalHeaderLabels(
            ['id', 'sort', 'roasting', 'ground/grain', 'taste', 'price', 'packaging volume'])
        self.tableWidget.resizeColumnsToContents()

    def open_change_coffee(self):
        if list(set([i.row() for i in self.tableWidget.selectedItems()])):
            self.to_change = list(set([i.row() for i in self.tableWidget.selectedItems()]))[0]
            self.window_show = Change_Coffee(self.to_change)
            self.window_show.show()
        else:
            self.not_aligned.setText('Выделите запись в таблице')

    def open_add_coffee(self):
        self.window_show = Add_Coffee()
        self.window_show.show()


class Change_Coffee(QWidget, Ui_Form_2):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Редактирование кофе')
        self.con = sqlite3.connect("coffee.db")
        self.sort.addItems(['Арабика', 'Робуста', 'Либерика', 'Эксцельза'])
        self.roasting.addItems(['светлая', 'средняя', 'темная'])
        self.type.addItems(['молотый', 'зерновой'])
        self.row = args[0]
        self.info = (self.con.cursor().execute("SELECT * FROM info").fetchall())[self.row]
        print(self.info)
        self.sort.setCurrentIndex(['Арабика', 'Робуста', 'Либерика', 'Эксцельза'].index(self.info[1]))
        self.roasting.setCurrentIndex(['светлая', 'средняя', 'темная'].index(self.info[2]))
        self.type.setCurrentIndex(['молотый', 'зерновой'].index(self.info[3]))
        self.taste.setText(str(self.info[4]))
        self.price.setText(str(self.info[5]))
        self.volume.setText(str(self.info[6]))
        self.button.setText("Отредактировать")
        self.button.clicked.connect(self.change)

    def change(self):
        if self.taste.text() != '' and self.price.text() != '' and self.volume.text() != '':
            self.con.cursor().execute(f"DELETE FROM info WHERE id = {self.row + 1}")
            self.con.commit()
            insert = [self.row + 1, self.sort.currentText(), self.roasting.currentText(), self.type.currentText(), self.taste.text(), self.price.text(), self.volume.text()]
            self.con.cursor().execute(f"INSERT INTO info(id, sort, roasting, ground_or_grain, taste, price, packaging_volume) VALUES (?, ?, ?, ?, ?, ?, ?)", insert)
            self.con.commit()
            form.update()
            self.close()
        else:
            self.error.setText('Неверно заполнена форма')


class Add_Coffee(QWidget, Ui_Form_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Добавить кофе')
        self.con = sqlite3.connect('coffee.db')
        self.sort.addItems(['Арабика', 'Робуста', 'Либерика', 'Эксцельза'])
        self.roasting.addItems(['светлая', 'средняя', 'темная'])
        self.type.addItems(['молотый', 'зерновой'])
        self.button.setText('Добавить')
        self.button.clicked.connect(self.add)

    def add(self):
        if self.taste.text() != '' and self.price.text() != '' and self.volume.text() != '':
            insert = [self.sort.currentText(), self.roasting.currentText(), self.type.currentText(), self.taste.text(), self.price.text(), self.volume.text()]
            self.con.cursor().execute(f"INSERT INTO info(sort, roasting, ground_or_grain, taste, price, packaging_volume) VALUES (?, ?, ?, ?, ?, ?)", insert)
            self.con.commit()
            form.update()
            self.close()
        else:
            self.error.setText('Неверно заполнена форма')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    form = Show_Coffee_Widget()
    form.show()
    sys.exit(app.exec())
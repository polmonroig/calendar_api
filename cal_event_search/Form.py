# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1790, 526)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = EventsTable(Form)
        self.tableWidget.setMinimumSize(QtCore.QSize(800, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(800, 16777215))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(200)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_9.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_9.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_9.addWidget(self.pushButton_3)
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_9.addWidget(self.pushButton_7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.chart = ChartView(Form)
        self.chart.setMinimumSize(QtCore.QSize(500, 500))
        self.chart.setMaximumSize(QtCore.QSize(500, 500))
        self.chart.setObjectName("chart")
        self.horizontalLayout_5.addWidget(self.chart)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.search_widget = QtWidgets.QWidget(Form)
        self.search_widget.setObjectName("search_widget")
        self.sear = QtWidgets.QHBoxLayout(self.search_widget)
        self.sear.setObjectName("sear")
        self.label_7 = QtWidgets.QLabel(self.search_widget)
        self.label_7.setObjectName("label_7")
        self.sear.addWidget(self.label_7)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.sear.addItem(spacerItem3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.search_widget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(220, 35))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(220, 35))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.sear.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addWidget(self.search_widget)
        self.type_widget_2 = QtWidgets.QWidget(Form)
        self.type_widget_2.setObjectName("type_widget_2")
        self.type_widget = QtWidgets.QHBoxLayout(self.type_widget_2)
        self.type_widget.setObjectName("type_widget")
        self.label = QtWidgets.QLabel(self.type_widget_2)
        self.label.setObjectName("label")
        self.type_widget.addWidget(self.label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.type_widget.addItem(spacerItem4)
        self.comboBox = QtWidgets.QComboBox(self.type_widget_2)
        self.comboBox.setMinimumSize(QtCore.QSize(220, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(220, 30))
        self.comboBox.setMaxVisibleItems(3)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.type_widget.addWidget(self.comboBox)
        self.verticalLayout_2.addWidget(self.type_widget_2)
        self.max_entries_widget = QtWidgets.QWidget(Form)
        self.max_entries_widget.setObjectName("max_entries_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.max_entries_widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.max_entries_widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.lineEdit = QtWidgets.QLineEdit(self.max_entries_widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(220, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(220, 30))
        self.lineEdit.setInputMask("")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_2.addWidget(self.max_entries_widget)
        self.basic_time_widget = QtWidgets.QWidget(Form)
        self.basic_time_widget.setObjectName("basic_time_widget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.basic_time_widget)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.basic_time_widget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.pushButton_4 = QtWidgets.QPushButton(self.basic_time_widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_11.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.basic_time_widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_11.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.basic_time_widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_11.addWidget(self.pushButton_6)
        self.checkBox = QtWidgets.QCheckBox(self.basic_time_widget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_11.addWidget(self.checkBox)
        self.verticalLayout_2.addWidget(self.basic_time_widget)
        self.start_time_widget = QtWidgets.QWidget(Form)
        self.start_time_widget.setObjectName("start_time_widget")
        self.start_time_layout = QtWidgets.QHBoxLayout(self.start_time_widget)
        self.start_time_layout.setObjectName("start_time_layout")
        self.start_time_label = QtWidgets.QLabel(self.start_time_widget)
        self.start_time_label.setEnabled(True)
        self.start_time_label.setObjectName("start_time_label")
        self.start_time_layout.addWidget(self.start_time_label)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.start_time_layout.addItem(spacerItem7)
        self.start_time = QtWidgets.QDateTimeEdit(self.start_time_widget)
        self.start_time.setEnabled(True)
        self.start_time.setMinimumSize(QtCore.QSize(220, 35))
        self.start_time.setMaximumSize(QtCore.QSize(220, 35))
        self.start_time.setDate(QtCore.QDate(2019, 4, 20))
        self.start_time.setCalendarPopup(True)
        self.start_time.setObjectName("start_time")
        self.start_time_layout.addWidget(self.start_time)
        self.verticalLayout_2.addWidget(self.start_time_widget)
        self.end_time_widget = QtWidgets.QWidget(Form)
        self.end_time_widget.setObjectName("end_time_widget")
        self.end_time_layout = QtWidgets.QHBoxLayout(self.end_time_widget)
        self.end_time_layout.setObjectName("end_time_layout")
        self.end_time_label = QtWidgets.QLabel(self.end_time_widget)
        self.end_time_label.setObjectName("end_time_label")
        self.end_time_layout.addWidget(self.end_time_label)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.end_time_layout.addItem(spacerItem8)
        self.end_time = QtWidgets.QDateTimeEdit(self.end_time_widget)
        self.end_time.setMinimumSize(QtCore.QSize(220, 35))
        self.end_time.setMaximumSize(QtCore.QSize(220, 35))
        self.end_time.setDate(QtCore.QDate(2025, 12, 31))
        self.end_time.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(9925, 12, 31), QtCore.QTime(13, 59, 59)))
        self.end_time.setCalendarPopup(True)
        self.end_time.setObjectName("end_time")
        self.end_time_layout.addWidget(self.end_time)
        self.verticalLayout_2.addWidget(self.end_time_widget)
        self.total_widget_2 = QtWidgets.QWidget(Form)
        self.total_widget_2.setObjectName("total_widget_2")
        self.total_widget = QtWidgets.QHBoxLayout(self.total_widget_2)
        self.total_widget.setObjectName("total_widget")
        self.label_3 = QtWidgets.QLabel(self.total_widget_2)
        self.label_3.setObjectName("label_3")
        self.total_widget.addWidget(self.label_3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.total_widget.addItem(spacerItem9)
        self.label_4 = QtWidgets.QLabel(self.total_widget_2)
        self.label_4.setMinimumSize(QtCore.QSize(220, 30))
        self.label_4.setMaximumSize(QtCore.QSize(220, 30))
        self.label_4.setObjectName("label_4")
        self.total_widget.addWidget(self.label_4)
        self.verticalLayout_2.addWidget(self.total_widget_2)
        self.duration_widget = QtWidgets.QWidget(Form)
        self.duration_widget.setObjectName("duration_widget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.duration_widget)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.duration_widget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem10)
        self.label_9 = QtWidgets.QLabel(self.duration_widget)
        self.label_9.setMinimumSize(QtCore.QSize(220, 30))
        self.label_9.setMaximumSize(QtCore.QSize(220, 30))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.verticalLayout_2.addWidget(self.duration_widget)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem11)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.pushButton.hide)
        self.pushButton.clicked.connect(self.tableWidget.connect_api)
        self.pushButton_2.clicked.connect(self.tableWidget.add_list_elements)
        self.pushButton_3.clicked.connect(self.tableWidget.save_data)
        self.lineEdit_2.textChanged['QString'].connect(self.tableWidget.set_search_entry)
        self.comboBox.currentIndexChanged['int'].connect(self.tableWidget.filter_color)
        self.lineEdit.textChanged['QString'].connect(self.tableWidget.set_max_entries)
        self.start_time.dateTimeChanged['QDateTime'].connect(self.tableWidget.set_start_time)
        self.end_time.dateTimeChanged['QDateTime'].connect(self.tableWidget.set_end_time)
        self.tableWidget.send_entries['int'].connect(self.label_4.setNum)
        self.tableWidget.send_duration['QString'].connect(self.label_9.setText)
        self.checkBox.toggled['bool'].connect(self.start_time_widget.setVisible)
        self.checkBox.toggled['bool'].connect(self.end_time_widget.setVisible)
        self.pushButton_4.clicked.connect(self.tableWidget.set_last_week)
        self.pushButton_5.clicked.connect(self.tableWidget.set_last_month)
        self.pushButton_6.clicked.connect(self.tableWidget.set_last_year)
        self.pushButton_7.clicked.connect(self.tableWidget.empty_table)
        self.tableWidget.send_colors.connect(self.chart.display_color_data)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calendar Manager"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Summary"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Duration"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Start Date"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Color"))
        self.pushButton.setText(_translate("Form", "Connect"))
        self.pushButton_2.setText(_translate("Form", "Search"))
        self.pushButton_3.setText(_translate("Form", "Save"))
        self.pushButton_7.setText(_translate("Form", "Empty"))
        self.label_7.setText(_translate("Form", "Search"))
        self.label.setText(_translate("Form", "Type"))
        self.comboBox.setItemText(0, _translate("Form", "All"))
        self.comboBox.setItemText(1, _translate("Form", "Lavender"))
        self.comboBox.setItemText(2, _translate("Form", "Esmerald Green"))
        self.comboBox.setItemText(3, _translate("Form", "Intense purple"))
        self.comboBox.setItemText(4, _translate("Form", "Turquoise"))
        self.comboBox.setItemText(5, _translate("Form", "Egg Yellow"))
        self.comboBox.setItemText(6, _translate("Form", "Mandarin orange"))
        self.comboBox.setItemText(7, _translate("Form", "Pink Bubblegum"))
        self.comboBox.setItemText(8, _translate("Form", "Graphite"))
        self.comboBox.setItemText(9, _translate("Form", "Blueberry Blue"))
        self.comboBox.setItemText(10, _translate("Form", "Moss Green"))
        self.comboBox.setItemText(11, _translate("Form", "Tomato"))
        self.label_2.setText(_translate("Form", "Max Entries"))
        self.label_10.setText(_translate("Form", "Time"))
        self.pushButton_4.setText(_translate("Form", "Last Week"))
        self.pushButton_5.setText(_translate("Form", "Last Month"))
        self.pushButton_6.setText(_translate("Form", "Last Year"))
        self.checkBox.setText(_translate("Form", "Advanced"))
        self.start_time_label.setText(_translate("Form", "Start Time"))
        self.start_time.setDisplayFormat(_translate("Form", "d/M/yyyy h:mm AP"))
        self.end_time_label.setText(_translate("Form", "End Time"))
        self.end_time.setDisplayFormat(_translate("Form", "d/M/yyyy h:mm AP"))
        self.label_3.setText(_translate("Form", "Total found"))
        self.label_4.setText(_translate("Form", "0"))
        self.label_8.setText(_translate("Form", "Duration"))
        self.label_9.setText(_translate("Form", "0"))

from chart_view import ChartView
from events_table import EventsTable

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


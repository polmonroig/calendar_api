from PyQt5 import QtGui, QtCore, QtWidgets
from api_utils import connect, get_list


class EventsList(QtWidgets.QListWidget):

    send_entries = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        QtWidgets.QListWidget.__init__(self, parent=parent)
        self.service = None
        self.color = None
        self.max_entries = 10

    def set_max_entries(self, entries):
        self.max_entries = int(entries)

    def empty_list(self):
        while self.count() > 0:
            self.takeItem(0)

    def add_list_elements(self):
        elements = get_list(self.service, self.max_entries)
        self.empty_list()
        count = 0
        for e in elements:
            if 'colorId' in e:
                color = e['colorId']
                print(e['summary'], e['colorId'])
                if self.color is None:
                    self.addItem(e['summary'])
                    count += 1
                elif int(color) == self.color:
                    self.addItem(e['summary'])
                    count += 1
        self.send_entries.emit(count)

    def connect_api(self):
        self.service = connect()


    def filter_color(self, color):
        print("Current filter:", color)
        if color != 0:
            self.color = color
        else:
            self.color = None

from PyQt5 import QtGui, QtCore, QtWidgets
from api_utils import connect, get_list
import datetime


class EventsList(QtWidgets.QListWidget):

    send_entries = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        QtWidgets.QListWidget.__init__(self, parent=parent)
        self.service = None
        self.color = None
        self.max_entries = None
        self.start_time = datetime.datetime.utcnow().isoformat() + 'Z'
        self.end_time = None
        self.search_entry = None

    def set_max_entries(self, entries):
        try:
            self.max_entries = int(entries)
        except ValueError:
            self.max_entries = None

    def empty_list(self):
        while self.count() > 0:
            self.takeItem(0)

    def set_search_entry(self, s):
        self.search_entry = s

    def set_end_time(self, time):
        self.end_time = time.toPyDateTime().isoformat() + 'Z'

    def set_start_time(self, time):
        self.start_time = time.toPyDateTime().isoformat() + 'Z'

    def add_list_elements(self):
        print("Events: ")
        elements = get_list(self.service, self.start_time,
                            self.end_time)
        self.empty_list()
        count = 0
        print(len(elements))
        for e in elements:
            if self.color is None:
                self.addItem(e['summary'])
                count += 1
            elif 'colorId' in e and int(e['colorId']) == self.color:
                self.addItem(e['summary'])
                count += 1
                print(e['summary'], e['colorId'])
            if self.max_entries and count >= self.max_entries:
                break
        self.send_entries.emit(count)

    def connect_api(self):
        self.service = connect()

    def filter_color(self, color):
        print("Current filter:", color)
        if color != 0:
            self.color = color
        else:
            self.color = None

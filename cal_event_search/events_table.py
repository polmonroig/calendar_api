from PyQt5 import QtCore, QtWidgets, QtGui
from cal_event_search.api_utils import connect, get_list
import datetime
import numpy as np


class EventsTable(QtWidgets.QTableWidget):

    send_entries = QtCore.pyqtSignal(int)
    send_duration = QtCore.pyqtSignal(str)
    SIMILAR_RANGE = 3

    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent=parent)
        self.service = None
        self.color = None
        self.max_entries = None
        self.start_time = datetime.datetime.utcnow().isoformat() + 'Z'
        self.end_time = None
        self.search_entry = None
        self.count = 0
        self.color_reference = [(125, 125, 125), (116, 134, 197), (10, 176, 124),
                                (148, 40, 165), (0, 162, 220), (248, 190, 64),
                                (248, 73, 43), (236, 121, 126), (97, 97, 97),
                                (51, 86, 185), (4, 130, 79), (221, 7, 27)]

    def set_max_entries(self, entries):
        try:
            self.max_entries = int(entries)
        except ValueError:
            self.max_entries = None

    def empty_list(self):
        self.setRowCount(0)
        self.count = 0

    def set_search_entry(self, s):
        self.search_entry = s.lower()
        if len(s) == 0:
            self.search_entry = None

    def set_end_time(self, time):
        self.end_time = time.toPyDateTime().isoformat() + 'Z'

    def set_start_time(self, time):
        self.start_time = time.toPyDateTime().isoformat() + 'Z'

    def similar(self, bag):
        words = bag.split()
        for word in words:
            if EventsTable.levenshtein(self.search_entry, word) < self.SIMILAR_RANGE:
                return True
        return False

    def add_row(self, summary, duration, start_date, color):
        self.insertRow(self.count)
        self.setItem(self.count, 0, QtWidgets.QTableWidgetItem(summary))
        self.setItem(self.count, 1, QtWidgets.QTableWidgetItem(duration))
        self.setItem(self.count, 2, QtWidgets.QTableWidgetItem(start_date))
        self.setItem(self.count, 3, QtWidgets.QTableWidgetItem(""))
        self.item(self.count, 3).setBackground(QtGui.QColor(color[0], color[1], color[2]))

    def add_list_elements(self):
        print("Events: ")
        elements = get_list(self.service, self.start_time,
                            self.end_time)
        self.empty_list()
        print(len(elements))
        total_duration = 0
        for e in elements:
            if 'summary' in e and 'dateTime' in e['start']:
                summary = e['summary']
                color = self.color_reference[0]

                start_time = e['start']['dateTime']
                start_time = datetime.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S+02:00")
                end_time = e['end']['dateTime']
                end_time = datetime.datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%S+02:00")
                duration = end_time - start_time
                if 'colorId' in e:
                    print("color: ", int(e['colorId']))
                    color = self.color_reference[int(e['colorId'])]
                if self.color is None:
                    if self.search_entry is None or self.similar(summary.lower()):
                        self.add_row(summary, str(duration.seconds),
                                     str(start_time.hour) + ":" + str(start_time.minute) + ":" + str(start_time.second),
                                     color)
                        self.count += 1
                        total_duration += int(duration.seconds)
                elif 'colorId' in e and int(e['colorId']) == self.color:
                    if self.search_entry is None or self.similar(summary.lower()):
                        self.add_row(summary, str(duration.seconds),
                                     str(start_time.hour) + ":" + str(start_time.minute) + ":" + str(start_time.second),
                                     color)
                        self.count += 1
                        total_duration += int(duration.seconds)
                if self.max_entries and self.count >= self.max_entries:
                    break

        # emit signals
        self.send_entries.emit(self.count)
        self.send_duration.emit(str(total_duration) + " seconds")

    def save_data(self):
        data = np.array([])
        n_cols = 3
        for i in range(self.count):
            for j in range(n_cols):
                data = np.append(data, self.item(i, j).text())
        data = data.reshape(self.count, n_cols)
        np.savetxt("data.csv", data, delimiter=",", fmt='%s')

    def connect_api(self):
        self.service = connect()

    def filter_color(self, color):
        print("Current filter:", color)
        if color != 0:
            self.color = color
        else:
            self.color = None

    @staticmethod
    def levenshtein(s1, s2):
        if len(s1) < len(s2):
            return EventsTable.levenshtein(s2, s1)

        # len(s1) >= len(s2)
        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]


#! usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
Slot = pyqtSlot


class MyMovie(QMovie):
    def __init__(self, *args, **keyword):
        super(MyMovie, self).__init__(*args, **keyword)
        self.indexes = []
        self.frameChanged.connect(self.onUpdated)

    @Slot(int)
    def onUpdated(self, frame):
        for index in self.indexes:
            # index.setData(self.currentPixmap(), Qt.DecorationRole)
            # index.setData(self.currentPixmap(), Qt.DecorationRole)
            # index.model().setData(index, str(frame), Qt.DisplayRole)
            index.model().setData(index, self.currentPixmap(), Qt.DecorationRole)
        # print(frame)


def main():
    app = QApplication(sys.argv)

    view = QTreeView()
    # view = QLabel("test")

    movie = MyMovie("./loading.gif", parent=view)
    # movie.started.connect(movie.onStarted)
    # movie.frameChanged.connect(movie.onUpdated)
    # print(movie.frameCount(), movie.isValid())
    # view.setMovie(movie)
    # movie.start()


    model = QStandardItemModel(view)
    item = QStandardItem("a")
    # label = QLabel("loading", view.viewport())
    # label.setMovie(movie)
    # item.setIcon(QIcon("./loading.gif"))
    model.appendRow(item)

    movie.indexes.append(item.index())
    # view.setIndexWidget(item.index(), label)

    model.appendRow(QStandardItem("b"))
    model.appendRow(QStandardItem("c"))
    view.setModel(model)
    movie.start()

    view.show()

    app.exec_()

if __name__ == '__main__':
    main()
import sys
from PyQt4 import QtGui


class PYQDemo:

    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)

    def addLabel(self, lableStr, pox, poy):
        b = QtGui.QLabel()
        b.setText("test label")

    def addButton(self, text, posx, posy):
        qbutn = QPushButton(text, self)


    def startGUI(self):
        w.setWindowTitle("testing PYQT")
        w.show()
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    pyqDemo = PYQDemo()
    pyqDemo.startGUI()
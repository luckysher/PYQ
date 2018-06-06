import sys
from PyQt4 import QtGui


class PYQDemo:

    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)

    def startGUI(self):

        w.show()
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    pyqDemo = PYQDemo()
    pyqDemo.startGUI()
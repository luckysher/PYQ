import sys
from PyQt4 import QtGui


class PYQDemo:

    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)

    def addTopTitle(self):
        self.setTopHeading("PyQT demo form ")
        setPosition('top', 'center')
        setBackColor("Blue")

    def addLabel(self, lableStr, pox, poy):
        b = QtGui.QLabel()
        b.setText("test label")

    def addButton(self, text, posx, posy):
        qbutn = QPushButton(text, self)
        qbutn.move(posx, posy)

    def addEditor(self, pox, poy, width=620):
        te = QPlainTextEdit(self)
        qbutn.move(posx, posy)

    def addPict(self, path, pox, poy):
        pic.setFrameStyle(Qt.DashLine)
        pic.setWidth(100)

    def startGUI(self):
        w.setWindowTitle("testing PYQT")

        self.addTopTitle()

        self.addPict("pic.png", 100, 100)

        self.addLabel("Name", 100, 120)

        self.addLabel("Age", 100, 140)

        self.addLabel("Country", 100, 160)


        w.show()
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    pyqDemo = PYQDemo()
    pyqDemo.startGUI()
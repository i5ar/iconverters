import sys

from PyQt4 import QtGui
from MainWindow import MainWindow
#from Form import Form

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    #form = Form()
    sys.exit(app.exec_())

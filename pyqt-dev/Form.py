from PyQt4 import QtCore, QtGui
from MainWindowUi import Ui_MainWindow
from FormUi import Ui_Form

class Form(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)

        # Widget user interface elements
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Widget signal/slot connections
        self.setupConnectionsForm()

    def clearLine(self):
        '''Clear text when button next is clicked'''
        self.ui.lineEdit.clear()

    def setupConnectionsForm(self):
        '''Signal and Slot Support'''
        self.connect(self.ui.pushButton_next, QtCore.SIGNAL('clicked()'), self.clearLine)

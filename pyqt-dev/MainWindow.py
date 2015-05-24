from PyQt4 import QtCore, QtGui
from MainWindowUi import Ui_MainWindow
from FormUi import Ui_Form

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # Main window user interface elements
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Main window signal/slot connections
        self.setupConnections()

    @QtCore.pyqtSlot()
    def showTipDialog(self):
        '''Trig dialog Tip'''
        form = QtGui.QDialog()
        form.ui = Ui_Form()
        form.ui.setupUi(form)
        form.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        #form.ui.lineEdit.clear()
        form.exec_()

    def setupConnections(self):
        '''Signal and Slot Support'''
        self.connect(self.ui.actionTip_of_the_Day, QtCore.SIGNAL('triggered()'), self.showTipDialog)

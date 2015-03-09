from PyQt4 import QtCore, QtGui

from MainWindowUi import Ui_MainWindow

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # Add user interface elements.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Validations
        iSarValidator = QtGui.QDoubleValidator()
        iSarValidator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        self.ui.lineEdit.setValidator(iSarValidator)
        self.ui.lineEdit_2.setValidator(iSarValidator)

        # Signal/slot connections
        self.setupConnections()

    def convertPascalPressure(self, text):

        if len(text) == 0:
            self.ui.lineEdit_2.clear()
            return

        # QComboBox Class Reference [1]
        # [1]: http://pyqt.sourceforge.net/Docs/PyQt4/qcombobox.html
        index = int(self.ui.comboBox.currentIndex())
        index_2 = int(self.ui.comboBox_2.currentIndex())

        if index == 0 and index_2 == 0: # Pa - kN/mmq
            pascal = float(text)
            knewton_per_mmq = pascal * (1. / 1000000000.)
            self.ui.lineEdit_2.setText(str(knewton_per_mmq))

        if index == 1 and index_2 == 0: # MPa - kN/mmq
            mpascal = float(text)
            knewton_per_mmq = mpascal / 1000.
            self.ui.lineEdit_2.setText(str(knewton_per_mmq))

        if index == 0 and index_2 == 1: # Pa - N/mmq
            pascal = float(text)
            newton_per_mmq = pascal / 1000000.
            self.ui.lineEdit_2.setText(str(newton_per_mmq))

        if index == 1 and index_2 == 1: # MPa - N/mmq
            mpascal = float(text)
            newton_per_mmq = mpascal
            self.ui.lineEdit_2.setText(str(newton_per_mmq))

    def convertNewtonPressure(self, text):

        if len(text) == 0:
            self.ui.lineEdit.clear()
            return

        index = int(self.ui.comboBox.currentIndex())
        index_2 = int(self.ui.comboBox_2.currentIndex())
        if index == 0 and index_2 == 0: # Pa - kN/mmq
            knewton_per_mmq = float(text)
            pascal = knewton_per_mmq * 1000000000.
            self.ui.lineEdit.setText(str(pascal))

        if index == 1 and index_2 == 0: # MPa - kN/mmq
            knewton_per_mmq = float(text)
            mpascal = knewton_per_mmq * 1000.
            self.ui.lineEdit.setText(str(mpascal))

        if index == 0 and index_2 == 1: # Pa - N/mmq
            newton_per_mmq = float(text)
            pascal = newton_per_mmq * 1000000.
            self.ui.lineEdit.setText(str(pascal))

        if index == 1 and index_2 == 1: # MPa - N/mmq
            newton_per_mmq = float(text)
            mpascal = newton_per_mmq
            self.ui.lineEdit.setText(str(mpascal))

    # External link test [2]
    # [2]: http://stackoverflow.com/questions/3684857/pyqt4-open-website-in-standard-browser-on-button-click
    def isarUrl(self):
        self.ui.pushButton_5.click
        #webbrowser.open('http://stackoverflow.com')

    # Signal and Slot Support [2]
    # [2]: http://pyqt.sourceforge.net/Docs/PyQt4/new_style_signals_slots.html
    def setupConnections(self):
        self.connect(self.ui.lineEdit, QtCore.SIGNAL('textEdited(QString)'), self.convertPascalPressure)
        self.connect(self.ui.lineEdit_2, QtCore.SIGNAL('textEdited(QString)'), self.convertNewtonPressure)

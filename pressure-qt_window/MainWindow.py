from PyQt4 import QtCore, QtGui

from MainWindowUi import Ui_MainWindow

# Convert pyuic4 MainWindow.ui -o MainWindowUi.py
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

      if index == 0: # Pa

        newton_per_mmq = float(text)
        pascal = newton_per_mmq * 1000000.
        self.ui.lineEdit_2.setText(str(pascal))

      if index == 1: # MPa

        newton_per_mmq = float(text)
        mpascal = newton_per_mmq
        self.ui.lineEdit_2.setText(str(mpascal))


    def convertNewtonPressure(self, text):

      if len(text) == 0:
        self.ui.lineEdit.clear()
        return

      index = int(self.ui.comboBox.currentIndex())
      if index == 0: # Pa

        newton_per_mmq = float(text)
        pascal = newton_per_mmq * (1. / 1000000.)
        self.ui.lineEdit.setText(str(pascal))

      if index == 1: # MPa

        newton_per_mmq = float(text)
        mpascal = newton_per_mmq
        self.ui.lineEdit.setText(str(mpascal))


    def setupConnections(self):
      self.connect(self.ui.lineEdit,
          QtCore.SIGNAL('textEdited(const QString &)'),
          self.convertPascalPressure)

      self.connect(self.ui.lineEdit_2,
          QtCore.SIGNAL('textEdited(const QString &)'),
          self.convertNewtonPressure)

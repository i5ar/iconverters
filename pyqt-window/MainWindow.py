import webbrowser

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
        self.setupExtra()

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

    # External link [2]
    # [2]: http://stackoverflow.com/questions/3684857/pyqt4-open-website-in-standard-browser-on-button-click
    def linkUrl(self):
        print("The web page!")
        webbrowser.open('https://github.com/i5ar/isarchon/blob/master/docs/stress.rst')

    def showDialog(self):
        QtGui.QMessageBox.about(self, 'About', '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }</style></head>'
                                               '<body style=" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;">'
                                               '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt;">A simple unit converter for architects.</span></p>'
                                               '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt;">Version 0.0.1</span></p>'
                                               '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt;">Copyright (c) 2015, </span><span style=" font-size:10pt; font-weight:600;">iSar</span></p>'
                                               '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><a href="http://three.isarch.it"><span style=" font-size:10pt; text-decoration: underline; color:#0000ff;">www.isarch.it</span></a></p>'
                                               '</body></html>')

    def showQuote(self):
        QtGui.QMessageBox.about(self, 'Quote', 'Los que buscan las leyes de la Naturaleza como un apoyo para sus nuevas obras colaboran con el creador. [Antoni Gaudi]')

    # Signal and Slot Support [3]
    # [3]: http://pyqt.sourceforge.net/Docs/PyQt4/new_style_signals_slots.html
    def setupConnections(self):
        self.connect(self.ui.lineEdit, QtCore.SIGNAL('textEdited(QString)'), self.convertPascalPressure)
        self.connect(self.ui.lineEdit_2, QtCore.SIGNAL('textEdited(QString)'), self.convertNewtonPressure)
        # Click button
        self.connect(self.ui.pushButton_5, QtCore.SIGNAL('clicked()'), self.linkUrl)
        # Trig dialog About
        self.connect(self.ui.actionAbout, QtCore.SIGNAL('triggered()'), self.showDialog)
        # Trig dialog Quit MainWindow
        self.connect(self.ui.actionQuit, QtCore.SIGNAL('triggered()'), self.deleteLater)
        # Trig dialog Quote
        self.connect(self.ui.actionQuote, QtCore.SIGNAL('triggered()'), self.showQuote)

    def setupExtra(self):
        #self.ui.pushButton_5.clicked.connect(self.linkUrl)
        #self.ui.actionAbout.triggered.connect(self.showDialog)
        self.ui.actionAbout.setShortcut('F1')
        self.ui.actionAbout.setStatusTip('About')
        self.ui.actionQuit.setShortcut('Ctrl+Q')
        self.ui.actionQuit.setStatusTip('Quit')

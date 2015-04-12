import webbrowser

from PyQt4 import QtCore, QtGui
from MainWindowUi import Ui_MainWindow
from ChildDialogUi import Ui_ChildDialog
from DialogUi import Ui_Dialog

isarchon_info = {
    "name": "iSarchon",
    "author": "Pierpaolo Rasicci",
    "version": (0, 0, 1),
    "python": (3, 4),
    "description": "Converter",
    "licence": "GPL" }

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
        self.ui.lineEdit_Newton.setValidator(iSarValidator)

        # Signal/slot connections
        self.setupConnections()
        self.setupExtra()

        # Trig dialog Quote
        self.dialogQuoteBrowser = Ui_ChildDialog(self)

        # Trig dialog Tip
        #self.dialog = Ui_Dialog(self)

    def convertPascalPressure(self, text):
        '''The measure to insert'''

        if len(text) == 0:
            self.ui.lineEdit_Newton.clear()
            return

        # QComboBox Class Reference [1]
        # [1]: http://pyqt.sourceforge.net/Docs/PyQt4/qcombobox.html
        index_Pascal = int(self.ui.comboBox_Pascal.currentIndex())
        index_NewtonSquareMeter = int(self.ui.comboBox_NewtonSquareMeter.currentIndex())
        index_GramSquareMeter = int(self.ui.comboBox_GramSquareMeter.currentIndex())
        index_PoundSquareFoot = int(self.ui.comboBox_PoundSquareFoot.currentIndex())

        if index_Pascal == 0 and index_NewtonSquareMeter == 0 and index_GramSquareMeter == 0 and index_PoundSquareFoot == 0:
            mpascal = float(text)
            newton_per_smm = mpascal
            kg_per_smm = mpascal / 9.8
            pound_per_sf = mpascal * 20885.4342730
            self.ui.lineEdit_Newton.setText(str(newton_per_smm))
            self.ui.lineEdit_Gram.setText(str(kg_per_smm))
            self.ui.lineEdit_Pound.setText(str(pound_per_sf))

        if index_Pascal == 1 and index_NewtonSquareMeter == 0: # Pa - N/smm
            pascal = float(text)
            newton_per_smm = pascal / 1000000.
            self.ui.lineEdit_Newton.setText(str(newton_per_smm))

        if index_Pascal == 0 and index_NewtonSquareMeter == 1: # MPa - kN/smm
            mpascal = float(text)
            knewton_per_smm = mpascal * 1000.
            self.ui.lineEdit_Newton.setText(str(knewton_per_smm))

        if index_Pascal == 1 and index_NewtonSquareMeter == 1: # Pa - kN/sm
            pascal = float(text)
            knewton_per_sm = pascal / 1000.
            self.ui.lineEdit_Newton.setText(str(knewton_per_sm))

    def convertNewtonPressure(self, text):

        if len(text) == 0:
            self.ui.lineEdit.clear()
            return

        index_Pascal = int(self.ui.comboBox_Pascal.currentIndex())
        index_NewtonSquareMeter = int(self.ui.comboBox_NewtonSquareMeter.currentIndex())
        index_GramSquareMeter = int(self.ui.comboBox_GramSquareMeter.currentIndex())
        index_PoundSquareFoot = int(self.ui.comboBox_PoundSquareFoot.currentIndex())

        if index_Pascal == 0 and index_NewtonSquareMeter == 0 and index_GramSquareMeter == 0 and index_PoundSquareFoot == 0:
            newton_per_smm = float(text)
            mpascal = newton_per_smm
            kg_per_smm = newton_per_smm / 9.8
            pound_per_sf = newton_per_smm * 20890
            self.ui.lineEdit.setText(str(mpascal))
            self.ui.lineEdit_Gram.setText(str(kg_per_smm))
            self.ui.lineEdit_Pound.setText(str(pound_per_sf))

        if index_Pascal == 1 and index_NewtonSquareMeter == 0:
            newton_per_smm = float(text)
            pascal = newton_per_smm * 1000000.
            self.ui.lineEdit.setText(str(pascal))

        if index_Pascal == 0 and index_NewtonSquareMeter == 1:
            knewton_per_smm = float(text)
            mpascal = knewton_per_smm / 1000.
            self.ui.lineEdit.setText(str(mpascal))

        if index_Pascal == 1 and index_NewtonSquareMeter == 1:
            knewton_per_sm = float(text)
            pascal = knewton_per_sm * 1000.
            self.ui.lineEdit.setText(str(pascal))

        if index_Pascal == 0 and index_NewtonSquareMeter == 1 and index_GramSquareMeter == 0 and index_PoundSquareFoot == 0:
            knewton_per_sm = float(text)
            mpascal = knewton_per_sm / 1000
            kg_per_smm = knewton_per_sm / 9.8 / 1000
            pound_per_sf = knewton_per_sm * 20890 / 1000
            self.ui.lineEdit.setText(str(mpascal))
            self.ui.lineEdit_Gram.setText(str(kg_per_smm))
            self.ui.lineEdit_Pound.setText(str(pound_per_sf))

    def convertKgSquareMeterPressure(self, text):

        if len(text) == 0:
            self.ui.lineEdit_Gram.clear()
            return

        index_Pascal = int(self.ui.comboBox_Pascal.currentIndex())
        index_NewtonSquareMeter = int(self.ui.comboBox_NewtonSquareMeter.currentIndex())
        index_GramSquareMeter = int(self.ui.comboBox_GramSquareMeter.currentIndex())
        index_PoundSquareFoot = int(self.ui.comboBox_PoundSquareFoot.currentIndex())

        if index_Pascal == 0 and index_NewtonSquareMeter == 0 and index_GramSquareMeter == 0 and index_PoundSquareFoot == 0:
            kg_per_smm = float(text)
            mpascal = kg_per_smm * 9.8
            newton_per_smm = kg_per_smm * 9.8
            pound_per_sf = kg_per_smm * 204816.182037424
            self.ui.lineEdit.setText(str(newton_per_smm))
            self.ui.lineEdit_Newton.setText(str(mpascal))
            self.ui.lineEdit_Pound.setText(str(pound_per_sf))

    def convertPoundSquareFootPressure(self, text):

        if len(text) == 0:
            self.ui.lineEdit_Gram.clear()
            return

        index_Pascal = int(self.ui.comboBox_Pascal.currentIndex())
        index_NewtonSquareMeter = int(self.ui.comboBox_NewtonSquareMeter.currentIndex())
        index_GramSquareMeter = int(self.ui.comboBox_GramSquareMeter.currentIndex())
        index_PoundSquareFoot = int(self.ui.comboBox_PoundSquareFoot.currentIndex())

        if index_Pascal == 0 and index_NewtonSquareMeter == 0 and index_GramSquareMeter == 0 and index_PoundSquareFoot == 0:
            pound_per_sf = float(text)
            mpascal = pound_per_sf * 1 / 204816.182037424 * 9.8
            newton_per_smm = pound_per_sf * 1 / 204816.182037424 * 9.8
            kg_per_smm = pound_per_sf * 1 / 204816.182037424
            self.ui.lineEdit.setText(str(mpascal))
            self.ui.lineEdit_Newton.setText(str(newton_per_smm))
            self.ui.lineEdit_Gram.setText(str(kg_per_smm))

    # External link [2]
    # [2]: http://stackoverflow.com/questions/3684857/pyqt4-open-website-in-standard-browser-on-button-click
    def linkStress(self):
        print("The web page!")
        webbrowser.open('https://github.com/i5ar/isarchon/blob/master/docs/stress.rst')

    def linkLighting(self):
        webbrowser.open('https://github.com/i5ar/isarchon/blob/master/docs/lighting.md')

    def showAboutDialog(self):
        QtGui.QMessageBox.about(self, 'About', '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }</style></head>'
                                               '<body style=" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;">'
                                               '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt;">A simple unit converter for architects.</span></p>'
                                               '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt;">Version 0.0.1</span></p>'
                                               '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:10pt;">Copyright (c) 2015, iSar</span></p>'
                                               '<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><a href="http://isarch.it"><span style=" font-size:10pt; text-decoration: underline; color:#0000ff;">www.isarch.it</span></a></p>'
                                               '</body></html>')

    # Trig dialog Quote
    @QtCore.pyqtSlot()
    def showQuoteDialog(self):
        self.dialogQuoteBrowser.exec_()

    # Trig dialog Tip
    @QtCore.pyqtSlot()
    def showTipDialog(self):
        dialog = QtGui.QDialog()
        dialog.ui = Ui_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()

    '''
    # Trig dialog Tip [5]
    # [5]: http://stackoverflow.com/questions/1807299/open-a-second-window-in-pyqt
    def on_actionTip_triggered(self, checked=None):
        if checked==None: return
        dialog = QtGui.QDialog()
        dialog.ui = Ui_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()
    '''

    # Signal and Slot Support [3]
    # [3]: http://pyqt.sourceforge.net/Docs/PyQt4/new_style_signals_slots.html
    def setupConnections(self):
        self.connect(self.ui.lineEdit, QtCore.SIGNAL('textEdited(QString)'), self.convertPascalPressure)
        self.connect(self.ui.lineEdit_Newton, QtCore.SIGNAL('textEdited(QString)'), self.convertNewtonPressure)
        self.connect(self.ui.lineEdit_Gram, QtCore.SIGNAL('textEdited(QString)'), self.convertKgSquareMeterPressure)
        self.connect(self.ui.lineEdit_Pound, QtCore.SIGNAL('textEdited(QString)'), self.convertPoundSquareFootPressure)
        # Click button
        self.connect(self.ui.pushButton_Stress, QtCore.SIGNAL('clicked()'), self.linkStress)
        self.connect(self.ui.pushButton_Illuminance, QtCore.SIGNAL('clicked()'), self.linkLighting)
        # Trig dialog About
        self.connect(self.ui.actionAbout, QtCore.SIGNAL('triggered()'), self.showAboutDialog)
        # Trig dialog Quit iSarchon
        self.connect(self.ui.actionQuit, QtCore.SIGNAL('triggered()'), self.deleteLater)
        # Trig dialog Quote [4]
        # [4] http://stackoverflow.com/questions/14410152/pyqt-on-click-open-new-window
        self.connect(self.ui.actionQuote, QtCore.SIGNAL('triggered()'), self.showQuoteDialog)
        # Trig dialog Tip
        self.connect(self.ui.actionTip, QtCore.SIGNAL('triggered()'), self.showTipDialog)

    def setupExtra(self):
        '''Pythonist'''
        #self.ui.pushButton_Illuminance.clicked.connect(self.linkLighting)
        #self.ui.actionAbout.triggered.connect(self.showDialog)
        #self.ui.actionQuote.triggered.connect(self.showTipDialog)
        self.ui.actionAbout.setShortcut('F1')
        self.ui.actionAbout.setStatusTip('About')
        self.ui.actionQuit.setShortcut('Ctrl+Q')

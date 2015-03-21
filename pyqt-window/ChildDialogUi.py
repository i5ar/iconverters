from PyQt4 import QtCore, QtGui

class Ui_ChildDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Ui_ChildDialog, self).__init__(parent)

        #self.buttonBox = QtGui.QDialogButtonBox(self)
        #self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        #self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)

        self.textBrowser = QtGui.QTextBrowser(self)
        self.textBrowser.append("\"An architect is the drawer of dreams.\" Grace McGarvie")

        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.addWidget(self.textBrowser)
        #self.verticalLayout.addWidget(self.buttonBox)

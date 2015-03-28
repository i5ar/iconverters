# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Widget.ui'
#
# Created: Sun Mar 22 09:23:23 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_Previous = QtGui.QPushButton(Dialog)
        self.pushButton_Previous.setObjectName(_fromUtf8("pushButton_Previous"))
        self.gridLayout.addWidget(self.pushButton_Previous, 0, 0, 1, 1)
        self.pushButton_Next = QtGui.QPushButton(Dialog)
        self.pushButton_Next.setObjectName(_fromUtf8("pushButton_Next"))
        self.gridLayout.addWidget(self.pushButton_Next, 0, 1, 1, 1)
        self.pushButton_Close = QtGui.QPushButton(Dialog)
        self.pushButton_Close.setObjectName(_fromUtf8("pushButton_Close"))
        self.gridLayout.addWidget(self.pushButton_Close, 0, 2, 1, 1)
        #self.pushButton_Close = QtGui.QDialogButtonBox(Dialog)                                                  #
        #self.pushButton_Close.setOrientation(QtCore.Qt.Horizontal)                                              #
        #self.pushButton_Close.setStandardButtons(QtGui.QDialogButtonBox.Close)                                  #
        #self.pushButton_Close.setObjectName(_fromUtf8("buttonBox"))                                             #
        #self.gridLayout.addWidget(self.pushButton_Close, 0, 2, 1, 1)                                            #

        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.retranslateUi(Dialog)
        #QtCore.QObject.connect(self.pushButton_Close, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)    #
        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lineEdit.setText(_translate("Dialog", "Test", None))
        self.pushButton_Previous.setText(_translate("Dialog", "Previous Tip", None))
        self.pushButton_Next.setText(_translate("Dialog", "Next Tip", None))
        self.pushButton_Close.setText(_translate("Dialog", "Close", None))

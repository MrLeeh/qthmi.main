# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'numpad.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_numPad(object):
    def setupUi(self, numPad):
        numPad.setObjectName("numPad")
        numPad.resize(290, 322)
        numPad.setWindowTitle("")
        self.gridLayout_2 = QtWidgets.QGridLayout(numPad)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonOK = QtWidgets.QPushButton(numPad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonOK.sizePolicy().hasHeightForWidth())
        self.buttonOK.setSizePolicy(sizePolicy)
        self.buttonOK.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonOK.setFont(font)
        self.buttonOK.setDefault(True)
        self.buttonOK.setObjectName("buttonOK")
        self.gridLayout_2.addWidget(self.buttonOK, 2, 0, 1, 1)
        self.buttonCancel = QtWidgets.QPushButton(numPad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonCancel.sizePolicy().hasHeightForWidth())
        self.buttonCancel.setSizePolicy(sizePolicy)
        self.buttonCancel.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonCancel.setFont(font)
        self.buttonCancel.setObjectName("buttonCancel")
        self.gridLayout_2.addWidget(self.buttonCancel, 2, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.button1 = QtWidgets.QPushButton(numPad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button1.sizePolicy().hasHeightForWidth())
        self.button1.setSizePolicy(sizePolicy)
        self.button1.setMinimumSize(QtCore.QSize(0, 0))
        self.button1.setMaximumSize(QtCore.QSize(10000, 10000))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        self.gridLayout.addWidget(self.button1, 2, 0, 1, 1)
        self.button5 = QtWidgets.QPushButton(numPad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button5.sizePolicy().hasHeightForWidth())
        self.button5.setSizePolicy(sizePolicy)
        self.button5.setMinimumSize(QtCore.QSize(0, 0))
        self.button5.setMaximumSize(QtCore.QSize(10000, 10000))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button5.setFont(font)
        self.button5.setObjectName("button5")
        self.gridLayout.addWidget(self.button5, 3, 1, 1, 1)
        self.button6 = QtWidgets.QPushButton(numPad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button6.sizePolicy().hasHeightForWidth())
        self.button6.setSizePolicy(sizePolicy)
        self.button6.setMinimumSize(QtCore.QSize(0, 0))
        self.button6.setMaximumSize(QtCore.QSize(10000, 10000))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button6.setFont(font)
        self.button6.setObjectName("button6")
        self.gridLayout.addWidget(self.button6, 3, 2, 1, 1)
        self.button9 = QtWidgets.QPushButton(numPad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button9.sizePolicy().hasHeightForWidth())
        self.button9.setSizePolicy(sizePolicy)
        self.button9.setMinimumSize(QtCore.QSize(0, 0))
        self.button9.setMaximumSize(QtCore.QSize(10000, 10000))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button9.setFont(font)
        self.button9.setObjectName("button9")
        self.gridLayout.addWidget(self.button9, 4, 2, 1, 1)
        self.button4 = QtWidgets.QPushButton(numPad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button4.sizePolicy().hasHeightForWidth())
        self.button4.setSizePolicy(sizePolicy)
        self.button4.setMinimumSize(QtCore.QSize(0, 0))
        self.button4.setMaximumSize(QtCore.QSize(10000, 10000))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button4.setFont(font)
        self.button4.setObjectName("button4")
        self.gridLayout.addWidget(self.button4, 3, 0, 1, 1)
        self.button2 = QtWidgets.QPushButton(numPad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button2.sizePolicy().hasHeightForWidth())
        self.button2.setSizePolicy(sizePolicy)
        self.button2.setMinimumSize(QtCore.QSize(0, 0))
        self.button2.setMaximumSize(QtCore.QSize(10000, 10000))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button2.setFont(font)
        self.button2.setObjectName("button2")
        self.gridLayout.addWidget(self.button2, 2, 1, 1, 1)
        self.button7 = QtWidgets.QPushButton(numPad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button7.sizePolicy().hasHeightForWidth())
        self.button7.setSizePolicy(sizePolicy)
        self.button7.setMinimumSize(QtCore.QSize(0, 0))
        self.button7.setMaximumSize(QtCore.QSize(10000, 10000))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button7.setFont(font)
        self.button7.setObjectName("button7")
        self.gridLayout.addWidget(self.button7, 4, 0, 1, 1)
        self.outputLineEdit = QtWidgets.QLineEdit(numPad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputLineEdit.sizePolicy().hasHeightForWidth())
        self.outputLineEdit.setSizePolicy(sizePolicy)
        self.outputLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.outputLineEdit.setFont(font)
        self.outputLineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLineEdit.setObjectName("outputLineEdit")
        self.gridLayout.addWidget(self.outputLineEdit, 0, 0, 1, 3)
        self.buttonDecimal = QtWidgets.QPushButton(numPad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonDecimal.sizePolicy().hasHeightForWidth())
        self.buttonDecimal.setSizePolicy(sizePolicy)
        self.buttonDecimal.setMinimumSize(QtCore.QSize(0, 0))
        self.buttonDecimal.setMaximumSize(QtCore.QSize(10000, 10000))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonDecimal.setFont(font)
        self.buttonDecimal.setObjectName("buttonDecimal")
        self.gridLayout.addWidget(self.buttonDecimal, 5, 0, 1, 1)
        self.buttonDel = QtWidgets.QPushButton(numPad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonDel.sizePolicy().hasHeightForWidth())
        self.buttonDel.setSizePolicy(sizePolicy)
        self.buttonDel.setMinimumSize(QtCore.QSize(0, 0))
        self.buttonDel.setMaximumSize(QtCore.QSize(10000, 10000))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttonDel.setFont(font)
        self.buttonDel.setObjectName("buttonDel")
        self.gridLayout.addWidget(self.buttonDel, 5, 2, 1, 1)
        self.button0 = QtWidgets.QPushButton(numPad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button0.sizePolicy().hasHeightForWidth())
        self.button0.setSizePolicy(sizePolicy)
        self.button0.setMinimumSize(QtCore.QSize(0, 0))
        self.button0.setMaximumSize(QtCore.QSize(10000, 10000))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button0.setFont(font)
        self.button0.setObjectName("button0")
        self.gridLayout.addWidget(self.button0, 5, 1, 1, 1)
        self.button8 = QtWidgets.QPushButton(numPad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button8.sizePolicy().hasHeightForWidth())
        self.button8.setSizePolicy(sizePolicy)
        self.button8.setMinimumSize(QtCore.QSize(0, 0))
        self.button8.setMaximumSize(QtCore.QSize(10000, 10000))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button8.setFont(font)
        self.button8.setObjectName("button8")
        self.gridLayout.addWidget(self.button8, 4, 1, 1, 1)
        self.button3 = QtWidgets.QPushButton(numPad)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button3.sizePolicy().hasHeightForWidth())
        self.button3.setSizePolicy(sizePolicy)
        self.button3.setMinimumSize(QtCore.QSize(0, 0))
        self.button3.setMaximumSize(QtCore.QSize(10000, 10000))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button3.setFont(font)
        self.button3.setObjectName("button3")
        self.gridLayout.addWidget(self.button3, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)

        self.retranslateUi(numPad)
        QtCore.QMetaObject.connectSlotsByName(numPad)

    def retranslateUi(self, numPad):
        _translate = QtCore.QCoreApplication.translate
        self.buttonOK.setText(_translate("numPad", "OK"))
        self.buttonCancel.setText(_translate("numPad", "Abbrechen"))
        self.button1.setText(_translate("numPad", "1"))
        self.button5.setText(_translate("numPad", "5"))
        self.button6.setText(_translate("numPad", "6"))
        self.button9.setText(_translate("numPad", "9"))
        self.button4.setText(_translate("numPad", "4"))
        self.button2.setText(_translate("numPad", "2"))
        self.button7.setText(_translate("numPad", "7"))
        self.buttonDecimal.setText(_translate("numPad", ","))
        self.buttonDel.setText(_translate("numPad", "DEL"))
        self.button0.setText(_translate("numPad", "0"))
        self.button8.setText(_translate("numPad", "8"))
        self.button3.setText(_translate("numPad", "3"))


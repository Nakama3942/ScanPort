# Form implementation generated from reading ui file 'ScanPort.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ScanPort(object):
    def setupUi(self, ScanPort):
        ScanPort.setObjectName("ScanPort")
        ScanPort.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(ScanPort)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineHost = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineHost.setFont(font)
        self.lineHost.setObjectName("lineHost")
        self.horizontalLayout_2.addWidget(self.lineHost)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.linePorts = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.linePorts.setFont(font)
        self.linePorts.setObjectName("linePorts")
        self.horizontalLayout_2.addWidget(self.linePorts)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttScan = QtWidgets.QPushButton(self.centralwidget)
        self.buttScan.setEnabled(False)
        self.buttScan.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.buttScan.setFont(font)
        self.buttScan.setObjectName("buttScan")
        self.verticalLayout.addWidget(self.buttScan)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.textResult = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textResult.setFont(font)
        self.textResult.setTabChangesFocus(False)
        self.textResult.setDocumentTitle("")
        self.textResult.setObjectName("textResult")
        self.verticalLayout.addWidget(self.textResult)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.toolClear = QtWidgets.QToolButton(self.centralwidget)
        self.toolClear.setEnabled(False)
        self.toolClear.setMinimumSize(QtCore.QSize(35, 35))
        self.toolClear.setObjectName("toolClear")
        self.horizontalLayout_3.addWidget(self.toolClear)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.toolDelete = QtWidgets.QToolButton(self.centralwidget)
        self.toolDelete.setMinimumSize(QtCore.QSize(75, 25))
        self.toolDelete.setObjectName("toolDelete")
        self.horizontalLayout.addWidget(self.toolDelete)
        self.buttOpen = QtWidgets.QPushButton(self.centralwidget)
        self.buttOpen.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttOpen.setFont(font)
        self.buttOpen.setObjectName("buttOpen")
        self.horizontalLayout.addWidget(self.buttOpen)
        self.buttSave = QtWidgets.QPushButton(self.centralwidget)
        self.buttSave.setEnabled(False)
        self.buttSave.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.buttSave.setFont(font)
        self.buttSave.setObjectName("buttSave")
        self.horizontalLayout.addWidget(self.buttSave)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        ScanPort.setCentralWidget(self.centralwidget)

        self.retranslateUi(ScanPort)
        QtCore.QMetaObject.connectSlotsByName(ScanPort)
        ScanPort.setTabOrder(self.linePorts, self.lineHost)
        ScanPort.setTabOrder(self.lineHost, self.buttScan)
        ScanPort.setTabOrder(self.buttScan, self.buttSave)
        ScanPort.setTabOrder(self.buttSave, self.buttOpen)
        ScanPort.setTabOrder(self.buttOpen, self.textResult)

    def retranslateUi(self, ScanPort):
        _translate = QtCore.QCoreApplication.translate
        ScanPort.setWindowTitle(_translate("ScanPort", "ScanPort"))
        self.label.setText(_translate("ScanPort", "Host:"))
        self.lineHost.setPlaceholderText(_translate("ScanPort", "localhost"))
        self.label_2.setText(_translate("ScanPort", "Port:"))
        self.linePorts.setPlaceholderText(_translate("ScanPort", "1,80,21,1000-1010"))
        self.buttScan.setToolTip(_translate("ScanPort", "If ports are not entered, the program will scan ports from 0 to 49151."))
        self.buttScan.setText(_translate("ScanPort", "Scan"))
        self.toolClear.setText(_translate("ScanPort", "Clear"))
        self.toolDelete.setText(_translate("ScanPort", "Delete save"))
        self.buttOpen.setText(_translate("ScanPort", "Open"))
        self.buttSave.setText(_translate("ScanPort", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ScanPort = QtWidgets.QMainWindow()
    ui = Ui_ScanPort()
    ui.setupUi(ScanPort)
    ScanPort.show()
    sys.exit(app.exec())

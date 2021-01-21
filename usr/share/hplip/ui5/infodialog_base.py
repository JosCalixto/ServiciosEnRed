# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infodialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 500)
        self.gridlayout = QtWidgets.QGridLayout(Dialog)
        self.gridlayout.setObjectName("gridlayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridlayout.addWidget(self.line, 1, 0, 1, 2)
        self.DeviceComboBox = DeviceUriComboBox(Dialog)
        self.DeviceComboBox.setObjectName("DeviceComboBox")
        self.gridlayout.addWidget(self.DeviceComboBox, 2, 0, 1, 2)
        self.TabWidget = QtWidgets.QTabWidget(Dialog)
        self.TabWidget.setObjectName("TabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridlayout1 = QtWidgets.QGridLayout(self.tab_2)
        self.gridlayout1.setObjectName("gridlayout1")
        self.StaticTableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.StaticTableWidget.setAlternatingRowColors(True)
        self.StaticTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.StaticTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.StaticTableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.StaticTableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.StaticTableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.StaticTableWidget.setObjectName("StaticTableWidget")
        self.StaticTableWidget.setColumnCount(0)
        self.StaticTableWidget.setRowCount(0)
        self.gridlayout1.addWidget(self.StaticTableWidget, 0, 0, 1, 1)
        self.TabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridlayout2 = QtWidgets.QGridLayout(self.tab)
        self.gridlayout2.setObjectName("gridlayout2")
        self.DynamicTableWidget = QtWidgets.QTableWidget(self.tab)
        self.DynamicTableWidget.setAlternatingRowColors(True)
        self.DynamicTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.DynamicTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.DynamicTableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.DynamicTableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.DynamicTableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.DynamicTableWidget.setObjectName("DynamicTableWidget")
        self.DynamicTableWidget.setColumnCount(0)
        self.DynamicTableWidget.setRowCount(0)
        self.gridlayout2.addWidget(self.DynamicTableWidget, 0, 0, 1, 1)
        self.TabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridlayout3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridlayout3.setObjectName("gridlayout3")
        self.HistoryTableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.HistoryTableWidget.setAlternatingRowColors(True)
        self.HistoryTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.HistoryTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.HistoryTableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.HistoryTableWidget.setGridStyle(QtCore.Qt.DotLine)
        self.HistoryTableWidget.setObjectName("HistoryTableWidget")
        self.HistoryTableWidget.setColumnCount(0)
        self.HistoryTableWidget.setRowCount(0)
        self.gridlayout3.addWidget(self.HistoryTableWidget, 0, 0, 1, 1)
        self.TabWidget.addTab(self.tab_3, "")
        self.gridlayout.addWidget(self.TabWidget, 3, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(470, 31, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.gridlayout.addItem(spacerItem, 4, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(361, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem1, 5, 0, 1, 1)
        self.CancelButton = QtWidgets.QPushButton(Dialog)
        self.CancelButton.setObjectName("CancelButton")
        self.gridlayout.addWidget(self.CancelButton, 5, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HP Device Manager - Device Information"))
        self.label.setText(_translate("Dialog", "Device Information"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab_2), _translate("Dialog", "Model Data (Static)"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab), _translate("Dialog", "Status Data (Dynamic)"))
        self.HistoryTableWidget.setSortingEnabled(False)
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab_3), _translate("Dialog", "Status History"))
        self.CancelButton.setText(_translate("Dialog", "Close"))

from .deviceuricombobox import DeviceUriComboBox

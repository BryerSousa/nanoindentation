# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'piuma_view.ui'
#
# Created: Thu Feb 18 22:22:02 2016
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_facewindow(object):
    def setupUi(self, facewindow):
        facewindow.setObjectName(_fromUtf8("facewindow"))
        facewindow.resize(1030, 655)
        facewindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../git/SiMPlE/smfsmanager/D_mica.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        facewindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(facewindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.grafo = PlotWidget(self.tab)
        self.grafo.setMinimumSize(QtCore.QSize(0, 0))
        self.grafo.setToolTip(_fromUtf8(""))
        self.grafo.setStatusTip(_fromUtf8(""))
        self.grafo.setWhatsThis(_fromUtf8(""))
        self.grafo.setObjectName(_fromUtf8("grafo"))
        self.verticalLayout_2.addWidget(self.grafo)
        self.labFilename = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labFilename.sizePolicy().hasHeightForWidth())
        self.labFilename.setSizePolicy(sizePolicy)
        self.labFilename.setObjectName(_fromUtf8("labFilename"))
        self.verticalLayout_2.addWidget(self.labFilename)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabProtocol = QtGui.QTableWidget(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabProtocol.sizePolicy().hasHeightForWidth())
        self.tabProtocol.setSizePolicy(sizePolicy)
        self.tabProtocol.setMinimumSize(QtCore.QSize(250, 0))
        self.tabProtocol.setRowCount(7)
        self.tabProtocol.setColumnCount(2)
        self.tabProtocol.setObjectName(_fromUtf8("tabProtocol"))
        item = QtGui.QTableWidgetItem()
        self.tabProtocol.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabProtocol.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabProtocol.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tabProtocol.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tabProtocol.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tabProtocol.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tabProtocol.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tabProtocol.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabProtocol.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tabProtocol.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tabProtocol.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tabProtocol.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tabProtocol.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tabProtocol.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tabProtocol.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tabProtocol.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tabProtocol.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tabProtocol.setItem(4, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tabProtocol.setItem(4, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tabProtocol.setItem(5, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tabProtocol.setItem(5, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tabProtocol.setItem(6, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tabProtocol.setItem(6, 1, item)
        self.tabProtocol.horizontalHeader().setVisible(False)
        self.tabProtocol.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tabProtocol)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.labK = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labK.sizePolicy().hasHeightForWidth())
        self.labK.setSizePolicy(sizePolicy)
        self.labK.setObjectName(_fromUtf8("labK"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.labK)
        self.labRadius = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labRadius.sizePolicy().hasHeightForWidth())
        self.labRadius.setSizePolicy(sizePolicy)
        self.labRadius.setObjectName(_fromUtf8("labRadius"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.labRadius)
        self.labCalib = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labCalib.sizePolicy().hasHeightForWidth())
        self.labCalib.setSizePolicy(sizePolicy)
        self.labCalib.setObjectName(_fromUtf8("labCalib"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.labCalib)
        self.label_7 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_8)
        self.labName = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labName.sizePolicy().hasHeightForWidth())
        self.labName.setSizePolicy(sizePolicy)
        self.labName.setObjectName(_fromUtf8("labName"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.labName)
        self.labDate = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labDate.sizePolicy().hasHeightForWidth())
        self.labDate.setSizePolicy(sizePolicy)
        self.labDate.setObjectName(_fromUtf8("labDate"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.labDate)
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtGui.QLabel(self.tab)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_10)
        self.labScan = QtGui.QLabel(self.tab)
        self.labScan.setObjectName(_fromUtf8("labScan"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.labScan)
        self.labXi = QtGui.QLabel(self.tab)
        self.labXi.setObjectName(_fromUtf8("labXi"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.labXi)
        self.labYi = QtGui.QLabel(self.tab)
        self.labYi.setObjectName(_fromUtf8("labYi"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.labYi)
        self.labDx = QtGui.QLabel(self.tab)
        self.labDx.setObjectName(_fromUtf8("labDx"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.labDx)
        self.labDy = QtGui.QLabel(self.tab)
        self.labDy.setObjectName(_fromUtf8("labDy"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.labDy)
        self.verticalLayout.addLayout(self.formLayout)
        self.bLoadScan = QtGui.QPushButton(self.tab)
        self.bLoadScan.setObjectName(_fromUtf8("bLoadScan"))
        self.verticalLayout.addWidget(self.bLoadScan)
        self.bSingleCurve = QtGui.QPushButton(self.tab)
        self.bSingleCurve.setObjectName(_fromUtf8("bSingleCurve"))
        self.verticalLayout.addWidget(self.bSingleCurve)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tabWork = QtGui.QWidget()
        self.tabWork.setObjectName(_fromUtf8("tabWork"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.tabWork)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.graCurva = PlotWidget(self.tabWork)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graCurva.sizePolicy().hasHeightForWidth())
        self.graCurva.setSizePolicy(sizePolicy)
        self.graCurva.setMinimumSize(QtCore.QSize(0, 0))
        self.graCurva.setToolTip(_fromUtf8(""))
        self.graCurva.setStatusTip(_fromUtf8(""))
        self.graCurva.setWhatsThis(_fromUtf8(""))
        self.graCurva.setObjectName(_fromUtf8("graCurva"))
        self.verticalLayout_8.addWidget(self.graCurva)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.bLoad = QtGui.QPushButton(self.tabWork)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bLoad.sizePolicy().hasHeightForWidth())
        self.bLoad.setSizePolicy(sizePolicy)
        self.bLoad.setObjectName(_fromUtf8("bLoad"))
        self.horizontalLayout_4.addWidget(self.bLoad)
        self.bSaveMap = QtGui.QPushButton(self.tabWork)
        self.bSaveMap.setObjectName(_fromUtf8("bSaveMap"))
        self.horizontalLayout_4.addWidget(self.bSaveMap)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_15 = QtGui.QLabel(self.tabWork)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.verticalLayout_5.addWidget(self.label_15)
        self.winSlider = QtGui.QSlider(self.tabWork)
        self.winSlider.setMinimum(1)
        self.winSlider.setMaximum(1000)
        self.winSlider.setSingleStep(1)
        self.winSlider.setPageStep(100)
        self.winSlider.setProperty("value", 500)
        self.winSlider.setOrientation(QtCore.Qt.Horizontal)
        self.winSlider.setTickPosition(QtGui.QSlider.TicksAbove)
        self.winSlider.setTickInterval(100)
        self.winSlider.setObjectName(_fromUtf8("winSlider"))
        self.verticalLayout_5.addWidget(self.winSlider)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.label_14 = QtGui.QLabel(self.tabWork)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.verticalLayout_6.addWidget(self.label_14)
        self.cbViewMode = QtGui.QComboBox(self.tabWork)
        self.cbViewMode.setObjectName(_fromUtf8("cbViewMode"))
        self.cbViewMode.addItem(_fromUtf8(""))
        self.cbViewMode.addItem(_fromUtf8(""))
        self.cbViewMode.addItem(_fromUtf8(""))
        self.cbViewMode.addItem(_fromUtf8(""))
        self.cbViewMode.addItem(_fromUtf8(""))
        self.verticalLayout_6.addWidget(self.cbViewMode)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_12 = QtGui.QLabel(self.tabWork)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.verticalLayout_7.addWidget(self.label_12)
        self.wSegment = QtGui.QSlider(self.tabWork)
        self.wSegment.setMinimum(0)
        self.wSegment.setMaximum(4)
        self.wSegment.setOrientation(QtCore.Qt.Horizontal)
        self.wSegment.setObjectName(_fromUtf8("wSegment"))
        self.verticalLayout_7.addWidget(self.wSegment)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_8)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tabWidget_2 = QtGui.QTabWidget(self.tabWork)
        self.tabWidget_2.setObjectName(_fromUtf8("tabWidget_2"))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.tab_5)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.cubo = QtGui.QGridLayout()
        self.cubo.setSpacing(0)
        self.cubo.setObjectName(_fromUtf8("cubo"))
        self.horizontalLayout_8.addLayout(self.cubo)
        self.tabWidget_2.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.tabWidget_2.addTab(self.tab_6, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget_2)
        self.tabMode = QtGui.QTabWidget(self.tabWork)
        self.tabMode.setObjectName(_fromUtf8("tabMode"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.togFlat = QtGui.QCheckBox(self.tab_2)
        self.togFlat.setGeometry(QtCore.QRect(40, 60, 81, 22))
        self.togFlat.setObjectName(_fromUtf8("togFlat"))
        self.tabMode.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label_11 = QtGui.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(20, 20, 91, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.fLevel = QtGui.QDoubleSpinBox(self.tab_3)
        self.fLevel.setGeometry(QtCore.QRect(20, 50, 111, 27))
        self.fLevel.setObjectName(_fromUtf8("fLevel"))
        self.bSetLevel = QtGui.QPushButton(self.tab_3)
        self.bSetLevel.setGeometry(QtCore.QRect(20, 100, 85, 27))
        self.bSetLevel.setObjectName(_fromUtf8("bSetLevel"))
        self.tabMode.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.label_13 = QtGui.QLabel(self.tab_4)
        self.label_13.setText(_fromUtf8(""))
        self.label_13.setPixmap(QtGui.QPixmap(_fromUtf8("hertzsmall.png")))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_9.addWidget(self.label_13)
        self.label_16 = QtGui.QLabel(self.tab_4)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.verticalLayout_9.addWidget(self.label_16)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.contactThresh = QtGui.QDoubleSpinBox(self.tab_4)
        self.contactThresh.setDecimals(6)
        self.contactThresh.setMinimum(-100.0)
        self.contactThresh.setMaximum(100.0)
        self.contactThresh.setSingleStep(0.0001)
        self.contactThresh.setProperty("value", 0.0002)
        self.contactThresh.setObjectName(_fromUtf8("contactThresh"))
        self.horizontalLayout_7.addWidget(self.contactThresh)
        self.vFitLimit = QtGui.QDoubleSpinBox(self.tab_4)
        self.vFitLimit.setDecimals(2)
        self.vFitLimit.setMinimum(-10000.0)
        self.vFitLimit.setMaximum(10000.0)
        self.vFitLimit.setSingleStep(10.0)
        self.vFitLimit.setProperty("value", 500.0)
        self.vFitLimit.setObjectName(_fromUtf8("vFitLimit"))
        self.horizontalLayout_7.addWidget(self.vFitLimit)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.groupBox = QtGui.QGroupBox(self.tab_4)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(_fromUtf8("background-color: silver;"))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.radIndentation = QtGui.QRadioButton(self.groupBox)
        self.radIndentation.setStyleSheet(_fromUtf8("border: none;"))
        self.radIndentation.setChecked(True)
        self.radIndentation.setObjectName(_fromUtf8("radIndentation"))
        self.verticalLayout_4.addWidget(self.radIndentation)
        self.radForce = QtGui.QRadioButton(self.groupBox)
        self.radForce.setStyleSheet(_fromUtf8("border: none;"))
        self.radForce.setChecked(False)
        self.radForce.setObjectName(_fromUtf8("radForce"))
        self.verticalLayout_4.addWidget(self.radForce)
        self.verticalLayout_9.addWidget(self.groupBox)
        self.labEcurrent = QtGui.QLabel(self.tab_4)
        self.labEcurrent.setAlignment(QtCore.Qt.AlignCenter)
        self.labEcurrent.setObjectName(_fromUtf8("labEcurrent"))
        self.verticalLayout_9.addWidget(self.labEcurrent)
        self.bEMap = QtGui.QPushButton(self.tab_4)
        self.bEMap.setObjectName(_fromUtf8("bEMap"))
        self.verticalLayout_9.addWidget(self.bEMap)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.tabMode.addTab(self.tab_4, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabMode)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tabWork, _fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.tabWidget)
        facewindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(facewindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabMode.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(facewindow)

    def retranslateUi(self, facewindow):
        facewindow.setWindowTitle(_translate("facewindow", "MainWindow", None))
        self.labFilename.setText(_translate("facewindow", "XXX", None))
        item = self.tabProtocol.verticalHeaderItem(0)
        item.setText(_translate("facewindow", "1", None))
        item = self.tabProtocol.verticalHeaderItem(1)
        item.setText(_translate("facewindow", "2", None))
        item = self.tabProtocol.verticalHeaderItem(2)
        item.setText(_translate("facewindow", "3", None))
        item = self.tabProtocol.verticalHeaderItem(3)
        item.setText(_translate("facewindow", "4", None))
        item = self.tabProtocol.verticalHeaderItem(4)
        item.setText(_translate("facewindow", "5", None))
        item = self.tabProtocol.verticalHeaderItem(5)
        item.setText(_translate("facewindow", "6", None))
        item = self.tabProtocol.verticalHeaderItem(6)
        item.setText(_translate("facewindow", "7", None))
        item = self.tabProtocol.horizontalHeaderItem(0)
        item.setText(_translate("facewindow", "D [nm]", None))
        item = self.tabProtocol.horizontalHeaderItem(1)
        item.setText(_translate("facewindow", "t [s]", None))
        __sortingEnabled = self.tabProtocol.isSortingEnabled()
        self.tabProtocol.setSortingEnabled(False)
        item = self.tabProtocol.item(0, 0)
        item.setText(_translate("facewindow", "//", None))
        item = self.tabProtocol.item(0, 1)
        item.setText(_translate("facewindow", "//", None))
        item = self.tabProtocol.item(1, 0)
        item.setText(_translate("facewindow", "//", None))
        item = self.tabProtocol.item(1, 1)
        item.setText(_translate("facewindow", "//", None))
        item = self.tabProtocol.item(2, 0)
        item.setText(_translate("facewindow", "//", None))
        item = self.tabProtocol.item(2, 1)
        item.setText(_translate("facewindow", "//", None))
        item = self.tabProtocol.item(3, 0)
        item.setText(_translate("facewindow", "//", None))
        item = self.tabProtocol.item(3, 1)
        item.setText(_translate("facewindow", "//", None))
        item = self.tabProtocol.item(4, 0)
        item.setText(_translate("facewindow", "//", None))
        item = self.tabProtocol.item(4, 1)
        item.setText(_translate("facewindow", "//", None))
        item = self.tabProtocol.item(5, 0)
        item.setText(_translate("facewindow", "//", None))
        item = self.tabProtocol.item(5, 1)
        item.setText(_translate("facewindow", "//", None))
        item = self.tabProtocol.item(6, 0)
        item.setText(_translate("facewindow", "//", None))
        item = self.tabProtocol.item(6, 1)
        item.setText(_translate("facewindow", "//", None))
        self.tabProtocol.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("facewindow", "k [N/m]", None))
        self.label_2.setText(_translate("facewindow", "Tip radius [um]", None))
        self.label_3.setText(_translate("facewindow", "Calibration factor", None))
        self.labK.setText(_translate("facewindow", "--", None))
        self.labRadius.setText(_translate("facewindow", "--", None))
        self.labCalib.setText(_translate("facewindow", "--", None))
        self.label_7.setText(_translate("facewindow", "Basename", None))
        self.label_8.setText(_translate("facewindow", "Date", None))
        self.labName.setText(_translate("facewindow", "--", None))
        self.labDate.setText(_translate("facewindow", "--", None))
        self.label_4.setText(_translate("facewindow", "Scan", None))
        self.label_5.setText(_translate("facewindow", "X Points", None))
        self.label_6.setText(_translate("facewindow", "Y Points", None))
        self.label_9.setText(_translate("facewindow", "X increment [um]", None))
        self.label_10.setText(_translate("facewindow", "Y increment [um]", None))
        self.labScan.setText(_translate("facewindow", "0", None))
        self.labXi.setText(_translate("facewindow", "0", None))
        self.labYi.setText(_translate("facewindow", "0", None))
        self.labDx.setText(_translate("facewindow", "0", None))
        self.labDy.setText(_translate("facewindow", "0", None))
        self.bLoadScan.setText(_translate("facewindow", "Load Scan", None))
        self.bSingleCurve.setText(_translate("facewindow", "Load Single Curve", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("facewindow", "Header", None))
        self.bLoad.setText(_translate("facewindow", "Load curves", None))
        self.bSaveMap.setText(_translate("facewindow", "Save Map", None))
        self.label_15.setText(_translate("facewindow", "Filter window", None))
        self.label_14.setText(_translate("facewindow", "View mode", None))
        self.cbViewMode.setItemText(0, _translate("facewindow", "Curve", None))
        self.cbViewMode.setItemText(1, _translate("facewindow", "Derivative: 1", None))
        self.cbViewMode.setItemText(2, _translate("facewindow", "Derivative: 2", None))
        self.cbViewMode.setItemText(3, _translate("facewindow", "Derivative: 3", None))
        self.cbViewMode.setItemText(4, _translate("facewindow", "Derivative: 4", None))
        self.label_12.setText(_translate("facewindow", "Working Segment", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("facewindow", "Tab 1", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("facewindow", "Tab 2", None))
        self.togFlat.setText(_translate("facewindow", "Flatten", None))
        self.tabMode.setTabText(self.tabMode.indexOf(self.tab_2), _translate("facewindow", "Test", None))
        self.label_11.setText(_translate("facewindow", "Force level", None))
        self.bSetLevel.setText(_translate("facewindow", "Set level", None))
        self.tabMode.setTabText(self.tabMode.indexOf(self.tab_3), _translate("facewindow", "Force", None))
        self.label_16.setText(_translate("facewindow", "Contact thresh - fit limit", None))
        self.groupBox.setTitle(_translate("facewindow", "Threshold mode", None))
        self.radIndentation.setText(_translate("facewindow", "Indentation", None))
        self.radForce.setText(_translate("facewindow", "Force", None))
        self.labEcurrent.setText(_translate("facewindow", "n.a.", None))
        self.bEMap.setText(_translate("facewindow", "E Map", None))
        self.tabMode.setTabText(self.tabMode.indexOf(self.tab_4), _translate("facewindow", "Hertz", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWork), _translate("facewindow", "Work", None))

from pyqtgraph import PlotWidget

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MVGapp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import clustering
import crawling
import metrics
import modelo
import glob
import os
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QFileDialog, QMainWindow, QWidget, QTableWidgetItem
from PyQt5.QtWidgets import  QCheckBox, QHBoxLayout
import query_expansion
import PyQt5.QtCore as Qt

class Ui_MainWindow(object):
    def __init__(self):
        self.urls_seed = []
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(538, 740)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_16 = QtWidgets.QFrame(self.groupBox_7)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_select_directory = QtWidgets.QLineEdit(self.frame_16)
        self.lineEdit_select_directory.setObjectName("lineEdit_select_directory")
        self.horizontalLayout_5.addWidget(self.lineEdit_select_directory)
        self.toolButton_select_directory = QtWidgets.QToolButton(self.frame_16)
        self.toolButton_select_directory.setObjectName("toolButton_select_directory")
        self.horizontalLayout_5.addWidget(self.toolButton_select_directory)
        self.verticalLayout_13.addWidget(self.frame_16)
        self.indexing_label = QtWidgets.QLabel(self.groupBox_7)
        self.indexing_label.setText("")
        self.indexing_label.setObjectName("indexing_label")
        self.verticalLayout_13.addWidget(self.indexing_label)
        self.verticalLayout_9.addWidget(self.groupBox_7)
        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_9.addWidget(self.line)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_8.setObjectName("groupBox_8")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.groupBox_8)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_10 = QtWidgets.QFrame(self.groupBox_8)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_crawling = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_crawling.setObjectName("lineEdit_crawling")
        self.horizontalLayout_6.addWidget(self.lineEdit_crawling)
        self.pushButton_add_crawling = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_add_crawling.setObjectName("pushButton_add_crawling")
        self.horizontalLayout_6.addWidget(self.pushButton_add_crawling)
        self.verticalLayout_14.addWidget(self.frame_10)
        self.tableWidget_crawling = QtWidgets.QTableWidget(self.groupBox_8)
        self.tableWidget_crawling.setObjectName("tableWidget_crawling")
        self.tableWidget_crawling.setColumnCount(2)
        self.tableWidget_crawling.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_crawling.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_crawling.setHorizontalHeaderItem(1, item)
        self.verticalLayout_14.addWidget(self.tableWidget_crawling)
        self.frame_11 = QtWidgets.QFrame(self.groupBox_8)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.pushButton_delete_urls = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_delete_urls.setObjectName("pushButton_delete_urls")
        self.horizontalLayout_7.addWidget(self.pushButton_delete_urls)
        self.verticalLayout_14.addWidget(self.frame_11)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_13 = QtWidgets.QFrame(self.groupBox_4)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_5 = QtWidgets.QLabel(self.frame_13)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_10.addWidget(self.label_5)
        self.lineEdit_user_name = QtWidgets.QLineEdit(self.frame_13)
        self.lineEdit_user_name.setObjectName("lineEdit_user_name")
        self.horizontalLayout_10.addWidget(self.lineEdit_user_name)
        self.verticalLayout_10.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.groupBox_4)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_6 = QtWidgets.QLabel(self.frame_14)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_11.addWidget(self.label_6)
        self.lineEdit_password = QtWidgets.QLineEdit(self.frame_14)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_11.addWidget(self.lineEdit_password)
        self.verticalLayout_10.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.groupBox_4)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.frame_15)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.lineEdit_host = QtWidgets.QLineEdit(self.frame_15)
        self.lineEdit_host.setObjectName("lineEdit_host")
        self.horizontalLayout_9.addWidget(self.lineEdit_host)
        self.label_8 = QtWidgets.QLabel(self.frame_15)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.lineEdit_port = QtWidgets.QLineEdit(self.frame_15)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.horizontalLayout_9.addWidget(self.lineEdit_port)
        self.verticalLayout_10.addWidget(self.frame_15)
        self.verticalLayout_14.addWidget(self.groupBox_4)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_12 = QtWidgets.QFrame(self.groupBox_6)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.frame_12)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.spinBox_deep_search_crawler = QtWidgets.QSpinBox(self.frame_12)
        self.spinBox_deep_search_crawler.setObjectName("spinBox_deep_search_crawler")
        self.horizontalLayout_8.addWidget(self.spinBox_deep_search_crawler)
        self.pushButton_crawling = QtWidgets.QPushButton(self.frame_12)
        self.pushButton_crawling.setObjectName("pushButton_crawling")
        self.horizontalLayout_8.addWidget(self.pushButton_crawling)
        self.verticalLayout_6.addWidget(self.frame_12)
        self.label_in_proces_crawler = QtWidgets.QLabel(self.groupBox_6)
        self.label_in_proces_crawler.setText("")
        self.label_in_proces_crawler.setObjectName("label_in_proces_crawler")
        self.verticalLayout_6.addWidget(self.label_in_proces_crawler)
        self.verticalLayout_14.addWidget(self.groupBox_6)
        self.verticalLayout_9.addWidget(self.groupBox_8)
        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_8 = QtWidgets.QFrame(self.tab)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_8)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lineEdit_query = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_query.setObjectName("lineEdit_query")
        self.verticalLayout_8.addWidget(self.lineEdit_query)
        self.frame_2 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox_query = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox_query.setProperty("value", 5)
        self.spinBox_query.setObjectName("spinBox_query")
        self.gridLayout.addWidget(self.spinBox_query, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.pushButton_query = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_query.setObjectName("pushButton_query")
        self.gridLayout.addWidget(self.pushButton_query, 1, 2, 1, 1)
        self.verticalLayout_8.addWidget(self.frame_2)
        self.frame_7 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame_7)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_3.addWidget(self.comboBox, 0, 1, 1, 1)
        self.verticalLayout_8.addWidget(self.frame_7)
        self.label_query = QtWidgets.QLabel(self.groupBox_2)
        self.label_query.setText("")
        self.label_query.setObjectName("label_query")
        self.verticalLayout_8.addWidget(self.label_query)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.frame = QtWidgets.QFrame(self.frame_8)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_3)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")
        self.Results = QtWidgets.QWidget()
        self.Results.setObjectName("Results")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Results)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.Results)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget_results = QtWidgets.QTableWidget(self.frame_4)
        self.tableWidget_results.setObjectName("tableWidget_results")
        self.tableWidget_results.setColumnCount(3)
        self.tableWidget_results.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_results.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_results.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_results.setHorizontalHeaderItem(2, item)
        self.horizontalLayout.addWidget(self.tableWidget_results)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.tabWidget.addTab(self.Results, "")
        self.SelectRelevantDocument = QtWidgets.QWidget()
        self.SelectRelevantDocument.setObjectName("SelectRelevantDocument")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.SelectRelevantDocument)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.SelectRelevantDocument)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget_relevant = QtWidgets.QTableWidget(self.frame_5)
        self.tableWidget_relevant.setObjectName("tableWidget_relevant")
        self.tableWidget_relevant.setColumnCount(3)
        self.tableWidget_relevant.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_relevant.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_relevant.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_relevant.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_3.addWidget(self.tableWidget_relevant)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.tabWidget.addTab(self.SelectRelevantDocument, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.frame_3)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.groupBox_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lineEdit_beta = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_beta.setObjectName("lineEdit_beta")
        self.horizontalLayout_4.addWidget(self.lineEdit_beta)
        self.comboBox_medida = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_medida.setObjectName("comboBox_medida")
        self.comboBox_medida.addItem("")
        self.comboBox_medida.addItem("")
        self.comboBox_medida.addItem("")
        self.comboBox_medida.addItem("")
        self.comboBox_medida.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_medida)
        self.lineEdit_medida = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_medida.setReadOnly(True)
        self.lineEdit_medida.setObjectName("lineEdit_medida")
        self.horizontalLayout_4.addWidget(self.lineEdit_medida)
        self.pushButton_CalculateMedida = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_CalculateMedida.setObjectName("pushButton_CalculateMedida")
        self.horizontalLayout_4.addWidget(self.pushButton_CalculateMedida)
        self.gridLayout_2.addWidget(self.frame_6, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout_7.addWidget(self.frame_8)
        self.tabWidget_2.addTab(self.tab, "")
        self.horizontalLayout_2.addWidget(self.tabWidget_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 538, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionsasa = QtWidgets.QAction(MainWindow)
        self.actionsasa.setObjectName("actionsasa")

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.toolButton_select_directory.clicked.connect(self.selectDirectory)
        self.pushButton_query.clicked.connect(self.make_query)
        self.pushButton_CalculateMedida.clicked.connect(self.calculate_metrics)
        self.comboBox_medida.currentTextChanged['QString'].connect(self.enable_disable_beta)
        self.pushButton_add_crawling.clicked.connect(self.add_url_to_crawler)
        self.pushButton_delete_urls.clicked.connect(self.delete_url_to_crawler)
        self.pushButton_crawling.clicked.connect(self.execute_crawler)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_crawling, self.pushButton_add_crawling)
        MainWindow.setTabOrder(self.pushButton_add_crawling, self.pushButton_delete_urls)
        MainWindow.setTabOrder(self.pushButton_delete_urls, self.lineEdit_user_name)
        MainWindow.setTabOrder(self.lineEdit_user_name, self.lineEdit_password)
        MainWindow.setTabOrder(self.lineEdit_password, self.lineEdit_host)
        MainWindow.setTabOrder(self.lineEdit_host, self.lineEdit_port)
        MainWindow.setTabOrder(self.lineEdit_port, self.spinBox_deep_search_crawler)
        MainWindow.setTabOrder(self.spinBox_deep_search_crawler, self.pushButton_crawling)
        MainWindow.setTabOrder(self.pushButton_crawling, self.lineEdit_query)
        MainWindow.setTabOrder(self.lineEdit_query, self.spinBox_query)
        MainWindow.setTabOrder(self.spinBox_query, self.pushButton_query)
        MainWindow.setTabOrder(self.pushButton_query, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.tableWidget_results)
        MainWindow.setTabOrder(self.tableWidget_results, self.lineEdit_beta)
        MainWindow.setTabOrder(self.lineEdit_beta, self.comboBox_medida)
        MainWindow.setTabOrder(self.comboBox_medida, self.lineEdit_medida)
        MainWindow.setTabOrder(self.lineEdit_medida, self.pushButton_CalculateMedida)
        MainWindow.setTabOrder(self.pushButton_CalculateMedida, self.tableWidget_relevant)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vector Space Model"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Local Search"))
        self.toolButton_select_directory.setText(_translate("MainWindow", "..."))
        self.groupBox_8.setTitle(_translate("MainWindow", "Web Search"))
        self.pushButton_add_crawling.setText(_translate("MainWindow", "Add Url"))
        item = self.tableWidget_crawling.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Urls"))
        self.pushButton_delete_urls.setText(_translate("MainWindow", "Delete Urls"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Proxy Configuration"))
        self.label_5.setText(_translate("MainWindow", "User Name"))
        self.label_6.setText(_translate("MainWindow", "Password"))
        self.label_7.setText(_translate("MainWindow", "Host"))
        self.label_8.setText(_translate("MainWindow", "Port"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Execute Crawler"))
        self.label_4.setText(_translate("MainWindow", "Deep Search"))
        self.pushButton_crawling.setText(_translate("MainWindow", "Crawling"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Select Repositiry"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Query"))
        self.label.setText(_translate("MainWindow", "Number of results"))
        self.pushButton_query.setText(_translate("MainWindow", "Consult"))
        self.label_3.setText(_translate("MainWindow", "Similarity Techniques"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Cosine Similarity"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Inner Product"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Dice Similarity"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Jaccard Similarity"))
        item = self.tableWidget_results.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Group"))
        item = self.tableWidget_results.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Document"))
        item = self.tableWidget_results.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Relevance"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Results), _translate("MainWindow", "Results"))
        item = self.tableWidget_relevant.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Group"))
        item = self.tableWidget_relevant.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Document"))
        item = self.tableWidget_relevant.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Relevance"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SelectRelevantDocument), _translate("MainWindow", "Select Relevant Document"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Metrics"))
        self.label_2.setText(_translate("MainWindow", "Beta"))
        self.comboBox_medida.setItemText(0, _translate("MainWindow", "P"))
        self.comboBox_medida.setItemText(1, _translate("MainWindow", "R"))
        self.comboBox_medida.setItemText(2, _translate("MainWindow", "E"))
        self.comboBox_medida.setItemText(3, _translate("MainWindow", "F"))
        self.comboBox_medida.setItemText(4, _translate("MainWindow", "PR"))
        self.pushButton_CalculateMedida.setText(_translate("MainWindow", "Calculate"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Query"))
        self.actionsasa.setText(_translate("MainWindow", "sasa"))
        self.pushButton_crawling.setEnabled(False)
        self.pushButton_delete_urls.setEnabled(False)

    def selectDirectory(self):
        # TODO: vaciar listas
        # TODO: desabilitar botones y habilitarlos cuando termine el build
        self.indexing_label.setText("Indexing Directory")
        path = str(QFileDialog.getExistingDirectory())
        print(path)
        # self.indexing_queryt_label.setText("Indexing Directory")

        self.lineEdit_select_directory.setText(path)
        self.build_model(path)

    def build_model(self,path):
        docs = glob.glob(os.path.join(path + "/**", "*.txt"), recursive=True)
        print(docs)
        if not self.lineEdit_select_directory.text() == '':
            clustering.clustering(path,4)

            for i in reversed(range(self.tableWidget_relevant.rowCount())):
                self.tableWidget_relevant.removeRow(i)
            for item in docs:
                row_position = self.tableWidget_relevant.rowCount()

                qwidget = QWidget()
                checkbox = QCheckBox()
                checkbox.setChecked(False)

                qhboxlayout = QHBoxLayout(qwidget)
                qhboxlayout.addWidget(checkbox)
                # qhboxlayout.setAlignment(Qt.AlignCenter)
                qhboxlayout.setContentsMargins(0, 0, 0, 0)

                self.tableWidget_relevant.insertRow(row_position)
                self.tableWidget_relevant.setItem(row_position, 0, clustering.all_label_from_cluster(os.path.basename(path)))
                self.tableWidget_relevant.setItem(row_position, 1, QTableWidgetItem(os.path.basename(item)))
                self.tableWidget_relevant.setCellWidget(row_position, 2, qwidget)

            self.disable_buttons()

            json_value = json.dumps({'action': 'build', 'path': path})

            modelo.model(json_value)

            self.enable_buttons()
            self.indexing_label.setText("")
            # if not self.lineEdit_select_directory.text() == '':
            #     self.make_table2()
            #     self.indexing_label.setText("Indexing Directory")
            #     self.disable_buttons()

    def make_query(self):

        for i in reversed(range(self.tableWidget_results.rowCount())):
            self.tableWidget_results.removeRow(i)
        query = self.lineEdit_query.text()
        count_docs = self.spinBox_query.value()
        similarity_techniques = self.comboBox.currentIndex()

        # TODO: llamar query_request
        # TODO: poner campo con similaridad
        # TODO: ponerle el count
        # TODO: poner label de procesamiento de texto
        # TODO:cuando la consulta sta vacia arreglar el error
        self.disable_buttons()
        self.label_query.setText("execcuting query")

        json_value = json.dumps({'action': 'query', 'query': query, 'count': count_docs, 'similarity_techniques': similarity_techniques})

        json_result = json.loads(query_expansion.start(json_value))

        for pair in json_result['results']:
            row_position = self.tableWidget_results.rowCount()
            print(type(row_position))
            self.tableWidget_results.insertRow(row_position)

            self.tableWidget_results.setItem(row_position, 1, QTableWidgetItem(str(pair["document"])))
            self.tableWidget_results.setItem(row_position, 2, QTableWidgetItem(str(pair["match"])))
        self.enable_buttons()
        self.label_query.setText("")


    def disable_buttons(self):
        self.toolButton_select_directory.setEnabled(False)

        self.spinBox_query.setEnabled(False)
        self.spinBox_deep_search_crawler.setEnabled(False)

        self.pushButton_query.setEnabled(False)
        self.pushButton_CalculateMedida.setEnabled(False)
        self.pushButton_add_crawling.setEnabled(False)
        self.pushButton_crawling.setEnabled(False)
        self.pushButton_delete_urls.setEnabled(False)

        self.lineEdit_crawling.setEnabled(False)
        self.lineEdit_host.setEnabled(False)
        self.lineEdit_password.setEnabled(False)
        self.lineEdit_port.setEnabled(False)
        self.lineEdit_user_name.setEnabled(False)
        self.lineEdit_query.setEnabled(False)

        self.comboBox.setEnabled(False)


        self.enable_disable_beta()

    def enable_buttons(self):
        self.toolButton_select_directory.setEnabled(True)

        self.spinBox_query.setEnabled(True)
        self.spinBox_deep_search_crawler.setEnabled(True)

        self.pushButton_query.setEnabled(True)
        self.pushButton_CalculateMedida.setEnabled(True)
        self.pushButton_add_crawling.setEnabled(True)
        self.pushButton_crawling.setEnabled(True)
        self.pushButton_delete_urls.setEnabled(True)

        self.lineEdit_crawling.setEnabled(True)
        self.lineEdit_host.setEnabled(True)
        self.lineEdit_password.setEnabled(True)
        self.lineEdit_port.setEnabled(True)
        self.lineEdit_user_name.setEnabled(True)
        self.lineEdit_query.setEnabled(True)

        self.comboBox.setEnabled(True)
        self.enable_disable_beta()



    def enable_disable_beta(self):
        if self.comboBox_medida.currentText() == "E":
            self.lineEdit_beta.setEnabled(True)
        else:
            self.lineEdit_beta.setEnabled(False)

    def calculate_metrics(self):
        #Documentos recuperados
        recovered_documents = []

        count_docs = self.tableWidget_results.rowCount()

        for item in range(count_docs):
            document = self.tableWidget_results.item(item, 1).text()
            recovered_documents.append(document)

        #Documentos Relevantes
        relevant_documents = []

        count_docs = self.tableWidget_relevant.rowCount()

        for item in range(count_docs):
            document = self.tableWidget_relevant.item(item, 1).text()
            relevant_box = self.tableWidget_relevant.cellWidget(item, 2)
            mark_box = relevant_box.findChildren(QCheckBox)[0]
            if mark_box.isChecked():
                relevant_documents.append(document)

        #Documentos Recuperados Relevantes
        rel = set(relevant_documents)
        rec = set(recovered_documents)
        recovered_relevant_documents = list(rel.intersection(rec))

        RR = len(recovered_relevant_documents)
        REC = len(recovered_documents)
        REL = len(relevant_documents)


        index = self.comboBox_medida.currentIndex()
        if index == 0:
            value = metrics.precision(RR, REC)
        elif index == 1:
            value = metrics.recobrado(RR,REL)
        elif index == 2:
            try:
                beta = float(self.lineEdit_beta.text())
                value = metrics.e_medida(RR, REL, REC, beta)
            except(Exception):
                self.lineEdit_beta.setText("0")
                value = metrics.e_medida(RR, REL, REC, 0)

        elif index == 3:
            value = metrics.f_medida(RR, REL, REC)
        else:
            value = metrics.r_presicion(RR, REC, REL)

        self.lineEdit_medida.setText(str(value))

    def add_url_to_crawler(self):
        row_position = self.tableWidget_relevant.rowCount()
        if self.lineEdit_crawling.text() != "":
            self.tableWidget_crawling.insertRow(row_position)
            self.tableWidget_crawling.setItem(row_position, 1, QTableWidgetItem(self.lineEdit_crawling.text()))
            self.urls_seed.append(self.lineEdit_crawling.text())
            self.lineEdit_crawling.setText("")
            self.pushButton_crawling.setEnabled(True)
            self.pushButton_delete_urls.setEnabled(True)




    def execute_crawler(self):
        deep = int(self.spinBox_deep_search_crawler.text())
        user_name = self.lineEdit_user_name.text()
        password = self.lineEdit_password.text()
        host = self.lineEdit_host.text()
        port = self.lineEdit_port.text()

        if user_name == "" and password== "" and host == "" and port == "":
            crawling.crawler(self.urls_seed, deep, True)
        else:
            crawling.crawler(self.urls_seed,deep,False,user_name=user_name, password = password, host_ip = host, port = port)
        path = "path donde se pone el crawling"
        self.build_model(path)

    def delete_url_to_crawler(self):
        self.pushButton_crawling.setEnabled(False)
        self.pushButton_delete_urls.setEnabled(False)

        count_docs = self.tableWidget_crawling.rowCount()
        items_to_remove =[]

        for item in range(count_docs):
            self.tableWidget_crawling.removeRow(0)
        self.urls_seed = []
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


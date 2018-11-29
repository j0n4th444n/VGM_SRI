# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MVGapp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(538, 651)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.toolButton_select_directory = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_select_directory.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.toolButton_select_directory.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.toolButton_select_directory.setAutoRaise(False)
        self.toolButton_select_directory.setObjectName("toolButton_select_directory")
        self.gridLayout_8.addWidget(self.toolButton_select_directory, 0, 1, 1, 1)
        self.lineEdit_select_directory = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_select_directory.setReadOnly(True)
        self.lineEdit_select_directory.setObjectName("lineEdit_select_directory")
        self.gridLayout_8.addWidget(self.lineEdit_select_directory, 0, 0, 1, 1)
        self.indexing_label = QtWidgets.QLabel(self.groupBox)
        self.indexing_label.setEnabled(True)
        self.indexing_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.indexing_label.setText("")
        self.indexing_label.setIndent(0)
        self.indexing_label.setObjectName("indexing_label")
        self.gridLayout_8.addWidget(self.indexing_label, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_query = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_query.setObjectName("lineEdit_query")
        self.verticalLayout_2.addWidget(self.lineEdit_query)
        self.frame_2 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox_query = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox_query.setProperty("value", 5)
        self.spinBox_query.setObjectName("spinBox_query")
        self.gridLayout.addWidget(self.spinBox_query, 0, 1, 1, 1)
        self.pushButton_query = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_query.setObjectName("pushButton_query")
        self.gridLayout.addWidget(self.pushButton_query, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_2)
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
        self.verticalLayout_2.addWidget(self.frame_7)
        self.label_query = QtWidgets.QLabel(self.groupBox_2)
        self.label_query.setText("gghhhhhhhh")
        self.label_query.setObjectName("label_query")
        self.verticalLayout_2.addWidget(self.label_query)
        self.verticalLayout.addWidget(self.groupBox_2)
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
        self.tableWidget_results.setColumnCount(2)
        self.tableWidget_results.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_results.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_results.setHorizontalHeaderItem(1, item)
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
        self.tableWidget_relevant.setColumnCount(2)
        self.tableWidget_relevant.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_relevant.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_relevant.setHorizontalHeaderItem(1, item)
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
        self.horizontalLayout_2.addWidget(self.frame)
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
        self.tabWidget.setCurrentIndex(0)
        self.toolButton_select_directory.clicked.connect(self.selectDirectory)
        self.pushButton_query.clicked.connect(self.make_query)
        self.pushButton_CalculateMedida.clicked.connect(self.calculate_metrics)
        self.comboBox_medida.currentTextChanged['QString'].connect(self.enable_disable_beta)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vector Space Model"))
        self.groupBox.setTitle(_translate("MainWindow", "Directory"))
        self.toolButton_select_directory.setText(_translate("MainWindow", "..."))
        self.groupBox_2.setTitle(_translate("MainWindow", "Query"))
        self.pushButton_query.setText(_translate("MainWindow", "Consult"))
        self.label.setText(_translate("MainWindow", "Number of results"))
        self.label_3.setText(_translate("MainWindow", "Similarity Techniques"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Cosine Similarity"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Inner Product"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Dice Similarity"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Jaccard Similarity"))
        item = self.tableWidget_results.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Document"))
        item = self.tableWidget_results.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Relevance"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Results), _translate("MainWindow", "Results"))
        item = self.tableWidget_relevant.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Document"))
        item = self.tableWidget_relevant.horizontalHeaderItem(1)
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
        self.actionsasa.setText(_translate("MainWindow", "sasa"))

    def selectDirectory(self):
        # TODO: vaciar listas
        # TODO: desabilitar botones y habilitarlos cuando termine el build
        self.indexing_label.setText("Indexing Directory")
        path = str(QFileDialog.getExistingDirectory())
        print(path)
        # self.indexing_queryt_label.setText("Indexing Directory")

        self.lineEdit_select_directory.setText(path)

        docs = glob.glob(os.path.join(path + "/**", "*.txt"), recursive=True)
        print(docs)
        if not self.lineEdit_select_directory.text() == '':
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
                self.tableWidget_relevant.setItem(row_position, 0, QTableWidgetItem(os.path.basename(item)))
                self.tableWidget_relevant.setCellWidget(row_position, 1, qwidget)

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

        # print(self.comboBox.currentText())
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

        # json_result = json.loads(modelo.model(json_value))
        print(json_result['results'])
        # self.tableWidget_results.insertRow(0)
        #
        # self.tableWidget_results.setItem(0, 0, QTableWidgetItem("documento"))
        # self.tableWidget_results.setItem(0, 1, QTableWidgetItem(str(5)))

        for pair in json_result['results']:
            row_position = self.tableWidget_results.rowCount()
            print(type(row_position))
            self.tableWidget_results.insertRow(row_position)

            self.tableWidget_results.setItem(row_position, 0, QTableWidgetItem(str(pair["document"])))
            self.tableWidget_results.setItem(row_position, 1, QTableWidgetItem(str(pair["match"])))
        self.enable_buttons()
        self.label_query.setText("")


    def disable_buttons(self):
        self.toolButton_select_directory.setEnabled(False)
        self.lineEdit_query.setEnabled(False)
        self.spinBox_query.setEnabled(False)
        self.pushButton_query.setEnabled(False)
        self.comboBox.setEnabled(False)
        self.pushButton_CalculateMedida.setEnabled(False)
        self.enable_disable_beta()

    def enable_buttons(self):
        self.toolButton_select_directory.setEnabled(True)
        self.lineEdit_query.setEnabled(True)
        self.spinBox_query.setEnabled(True)
        self.pushButton_query.setEnabled(True)
        self.comboBox.setEnabled(True)
        self.pushButton_CalculateMedida.setEnabled(True)
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
            document = self.tableWidget_results.item(item, 0).text()
            recovered_documents.append(document)

        #Documentos Relevantes
        relevant_documents = []

        count_docs = self.tableWidget_relevant.rowCount()

        for item in range(count_docs):
            document = self.tableWidget_relevant.item(item, 0).text()
            relevant_box = self.tableWidget_relevant.cellWidget(item, 1)
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


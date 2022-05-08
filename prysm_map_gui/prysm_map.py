# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'switch-window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import io
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtQuickWidgets import QQuickWidget
from PySide2 import QtCore, QtQml
import csv
import os

class CSVHelper(QtCore.QObject):
    @QtCore.Slot("QAbstractItemModel*", str)
    def saveListModel(self, model, filename):
        headers = {v.data().decode(): k for k, v in model.roleNames().items()}
        with open(filename, mode="w") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers.keys())
            writer.writeheader()

            for i in range(model.rowCount()):
                row = dict()
                for name, role in headers.items():
                    value = model.index(i, 0).data(role)
                    row[name] = value
                writer.writerow(row)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(738, 697)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.mainpage = QPushButton(self.centralwidget)
        self.mainpage.setObjectName(u"mainpage")

        self.horizontalLayout_7.addWidget(self.mainpage)

        self.mapview = QPushButton(self.centralwidget)
        self.mapview.setObjectName(u"mapview")

        self.horizontalLayout_7.addWidget(self.mapview)


        self.gridLayout_2.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.homepage = QWidget()
        self.homepage.setObjectName(u"homepage")
        self.gridLayout_6 = QGridLayout(self.homepage)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(self.homepage)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_2 = QLabel(self.homepage)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.label_3 = QLabel(self.homepage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u"../../../Downloads/output-onlinepngtools.png"))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.homepage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_4)

        self.label_5 = QLabel(self.homepage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.homepage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_6)


        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_3 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 38, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)


        self.gridLayout.addLayout(self.verticalLayout_2, 3, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.homepage)
        self.map = QWidget()
        self.map.setObjectName(u"map")
        self.gridLayout_5 = QGridLayout(self.map)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.map)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.comboBox = QComboBox(self.map)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)

        # self.horizontalLayout_3 = QHBoxLayout()
        # self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        # self.label_8 = QLabel(self.map)
        # self.label_8.setObjectName(u"label_8")

        # self.horizontalLayout_3.addWidget(self.label_8)

        # self.lineEdit = QLineEdit(self.map)
        # self.lineEdit.setObjectName(u"lineEdit")

        # self.horizontalLayout_3.addWidget(self.lineEdit)


        # self.horizontalLayout_6.addLayout(self.horizontalLayout_3)

        # self.horizontalLayout_4 = QHBoxLayout()
        # self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        # self.label_9 = QLabel(self.map)
        # self.label_9.setObjectName(u"label_9")

        # self.horizontalLayout_4.addWidget(self.label_9)

        # self.lineEdit_2 = QLineEdit(self.map)
        # self.lineEdit_2.setObjectName(u"lineEdit_2")

        # self.horizontalLayout_4.addWidget(self.lineEdit_2)


        # self.horizontalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_10 = QLabel(self.map)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_5.addWidget(self.label_10)

        self.comboBox_2 = QComboBox(self.map)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_5.addWidget(self.comboBox_2)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.pushButton = QPushButton(self.map)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 0, 1, 1)

        self.map_widget = QQuickWidget(self.map)

        csv_helper = CSVHelper(self.map_widget)
        self.map_widget.rootContext().setContextProperty('CSVHelper', csv_helper)
        qml_path = os.path.join(os.path.dirname(__file__), "testmodel.qml")
        self.map_widget.setSource(QtCore.QUrl.fromLocalFile(qml_path))

        #url = QUrl("testmodel.qml")
        #self.map_widget.setSource(url)

        self.map_widget.setResizeMode(QQuickWidget.SizeRootObjectToView)

        self.maplayout = QVBoxLayout(self.map)
        self.maplayout.addWidget(self.map_widget)

        #self.setCentralWidget(self.main_widget)
        #self.maplayout = QVBoxLayout(self.map)
        #self.maplayout.setObjectName(u"mapView")

        #coordinate = (37.8199286, -122.4782551)
        #m = folium.Map(
        #	tiles='Stamen Terrain',
        #	zoom_start=3,
        #	location=coordinate
        #)
        #m.add_child(folium.LatLngPopup())
        #m.add_child(folium.ClickForMarker(popup="Waypoint"))
        #m

        # save map data to data object
        #data = io.BytesIO()
        #m.save(data, close_file=False)

        #webView = QWebEngineView()
        #webView.setHtml(data.getvalue().decode())
        #self.maplayout.addWidget(webView)

        self.gridLayout_4.addLayout(self.maplayout, 1, 0, 1, 1)

        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.map)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.mainpage.setText(QCoreApplication.translate("MainWindow", u"Homepage", None))
        self.mapview.setText(QCoreApplication.translate("MainWindow", u"Map View", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"PRYSM MAP GUI", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Proxy System Modelling Tools: Map Based Graphical User Interface", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Map based Graphical User Interface to visualise proxy variables using", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Climate Model Variables like Sea Surface temperature(SST), Sea Surface Salinity(SSS), etc.", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Just select the locations at the map along with the time period to get the observational output", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Select Proxy", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Coral", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Icecores", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Speleotherm", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Tree Ring Cellulose", None))

        # self.label_8.setText(QCoreApplication.translate("MainWindow", u"Longitude", None))
        # self.label_9.setText(QCoreApplication.translate("MainWindow", u"Latitude", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Time Period", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"1960-1970", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"1970-1980", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"1980-1990", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"1990-2000", None))

        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
    # retranslateUi
    


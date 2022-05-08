#################################
import os
os.environ['QT_MAC_WANTS_LAYER'] = '1' 
import os.path
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from prysm_map import Ui_MainWindow
#from prysm_map import CSVHelper
from output import Output_Window
from PySide2 import QtCore, QtQml
import csv


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.main_win.setWindowTitle("PRYSM MAP GUI")
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.homepage)

        self.ui.mainpage.clicked.connect(self.showHomepage)
        self.ui.mapview.clicked.connect(self.showMap)

        self.ui.pushButton.released.connect(self.btnpress)
        self.ui.pushButton.clicked.connect(self.outputwindow)


    def outputwindow(self):                                             # <===
        self.w = Output_Window()
        self.w.show()
        self.hide()

    def btnpress(self):

        with open("location.csv", 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                print(row)
                self.process = QProcess()
                self.process.readyReadStandardError.connect(self.handle_readyReadStandardError)
                self.process.readyReadStandardOutput.connect(
                    self.handle_readyReadStandardOutput
                )
                self.process.setProgram(sys.executable)
                content = self.ui.comboBox.currentText()
                contentVal = self.checkComboContent(content)
                script_path = os.path.join( CURRENT_DIR, contentVal + "_driver.py")
                arguments = row
                self.process.start(script_path, arguments)
                self.process.waitForFinished(-1)

                number = 3

                msg = "{}\n".format(number)
                self.process.write(msg.encode())


    def checkComboContent(self, content):
        if content == "Icecores":
            contentVal= "icecore"
        elif content == "Coral":
            contentVal = "coral"
        elif content == "Speleotherm":
            contentVal = "speleo"
        elif content == "Tree Ring Cellulose":
            contentVal = "cellulose"
        return contentVal


    def handle_readyReadStandardError(self):
        print(self.process.readAllStandardError().data().decode())

    def handle_readyReadStandardOutput(self):
        print(self.process.readAllStandardOutput().data().decode())

    def show(self):
        self.main_win.show()

    def showMap(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.map)

    def showHomepage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.homepage)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    #csv_helper = CSVHelper()

    #engine = QtQml.QQmlApplicationEngine()
    #engine.rootContext().setContextProperty("CSVHelper", csv_helper)
    #file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "testmodel.qml")
    #engine.load(QtCore.QUrl.fromLocalFile(file))
    #if not engine.rootObjects():
    #    sys.exit(-1)

    main_win = MainWindow()
    main_win.show()

    sys.exit(app.exec_())
#################################
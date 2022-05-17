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

# locate current directory
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        # setting the title for the application
        self.main_win.setWindowTitle("PRYSM MAP GUI")
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.homepage)
        
        # toggle to homepage when homepage button is clicked
        self.ui.mainpage.clicked.connect(self.showHomepage)
        # toggle to map view when mapview button is clicked
        self.ui.mapview.clicked.connect(self.showMap)

        self.ui.pushButton.released.connect(self.btnpress)
        self.ui.pushButton.clicked.connect(self.outputwindow)

    # defining previously created output window
    def outputwindow(self):                                             # <===
        self.w = Output_Window()
        self.w.show()
        #self.hide()

    # functional logic on opening of driver script after clicking submit button
    # 
    def btnpress(self):

        # opening the location file where location coordinates which have 
        # been clicked by user in user interface is store. Here, we go through 
        # this csv file and for each latitude and longitude value we start a process
        # to run a driver script passing time period and location coordinates
        # to driver script.
        with open("location.csv", 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                # starting the process
                self.process = QProcess()
                self.process.readyReadStandardError.connect(self.handle_readyReadStandardError)
                self.process.readyReadStandardOutput.connect(
                    self.handle_readyReadStandardOutput
                )
                self.process.setProgram(sys.executable)
                
                # extracting the selected time period in the GUI
                selectedTimePeriod = self.ui.comboBox_2.currentText()
                selectedTimePeriodVal= self.checkSelectedTimePeriod(selectedTimePeriod)

                script_path = os.path.join( CURRENT_DIR, "coral_driver/coral_driver.py")
                print(script_path, selectedTimePeriodVal)
                arguments = row
                # execution of process to run the driver script
                self.process.start(script_path, arguments)
                self.process.waitForFinished(-1)

                number = 3

                msg = "{}\n".format(number)
                self.process.write(msg.encode())

    # function to check the time period selected
    def checkSelectedTimePeriod(self, time_period):
        if time_period == "1955-1964":
            contentVal= "5564"
        elif time_period == "1965-1974":
            contentVal = "6574"
        elif time_period == "1975-1984":
            contentVal = "7584"
        elif time_period == "1985-1994":
            contentVal = "8594"
        elif time_period == "1995-2004":
            contentVal = "9504"
        elif time_period == "2005-2017":
            contentVal = "0517"
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
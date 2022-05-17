# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'output.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

# class to create output window to display download information
class Output_Window (QMainWindow):                           
    def __init__(self):
        super(Output_Window, self).__init__()
        self.setWindowTitle("Output Window")

        # creating progress bar 
        self.progressBar = QProgressBar(self) 

        # setting its size 
        self.progressBar.setGeometry(25, 45, 210, 30) 

        # creating push button to start download 
        self.button = QPushButton('Start', self) 

        # assigning position to button 
        self.button.move(50, 100) 

        # assigning activity to push button 
        self.button.clicked.connect(self.Download) 

        widget = QLabel("Output Proxy Downloaded")
        font = widget.font()
        font.setPointSize(12)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setCentralWidget(widget)

    def Download(self): 

        # specify the url of the file which is to be downloaded 
        down_url = 'https://images.unsplash.com/photo-1613929905911-96040610a54d?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=701&q=80' # specify download url here 

        # specify save location where the file is to be saved 
        save_loc = 'profile.jpg'

        # Dowloading using urllib 
        urllib.request.urlretrieve(down_url,save_loc, self.Handle_Progress) 


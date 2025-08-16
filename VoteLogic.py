from VoteGUI import Ui_MainWindow
from PyQt6.QtWidgets import *
from PyQt6 import QtCore
import csv
import os

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.pushButton.clicked.connect(lambda: self.check())

    def check(self):
        '''
         When Vote is clicked, checks to make sure all parameters are met
        :return:
        '''
        id = self.lineEdit.text().strip()
        with open('ID.txt', 'r') as readfile:
            readlines = [line.strip() for line in readfile.readlines()]
        if id == '':
            self.label_2.setGeometry(QtCore.QRect(35, 110, 120, 16))
            self.label_2.setText("Please enter an ID")
        elif id in readlines:
            self.label_2.setGeometry(QtCore.QRect(45, 110, 120, 16))
            self.label_2.setText("Already voted")
        elif not self.radioButton.isChecked() and not self.radioButton_2.isChecked():
            self.label_2.setGeometry(QtCore.QRect(15, 110, 135, 16))
            self.label_2.setText("Please select a candidate")
        else:
            self.label_2.setGeometry(QtCore.QRect(45, 110, 135, 16))
            self.label_2.setText("Are you sure?")
            self.pushButton_2.setVisible(True)
            self.pushButton_3.setVisible(True)
            try:
                self.pushButton_2.clicked.disconnect()
            except TypeError:
                pass
            try:
                self.pushButton_3.clicked.disconnect()
            except TypeError:
                pass

            self.pushButton_2.clicked.connect(lambda: self.confirm_vote())
            self.pushButton_3.clicked.connect(lambda: self.cancel_vote())

    def confirm_vote(self):
        '''
        When pushButton_2 is pressed, this appends ID to the text file and CSV file with the candidate they voted for
        :return:
        '''
        id = self.lineEdit.text().strip()
        candidate = ""
        if self.radioButton.isChecked():
            candidate = self.radioButton.text()
        elif self.radioButton_2.isChecked():
            candidate = self.radioButton_2.text()
        with open('ID.txt', 'a') as idfile:
            idfile.write(id + '\n')
        file_exists = os.path.isfile('votes.csv')
        with open('votes.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                writer.writerow(['Voter ID', 'Candidate'])
            writer.writerow([id, candidate])
        self.label_2.setGeometry(QtCore.QRect(40, 110, 135, 16))
        self.label_2.setText("Vote submitted!")
        self.pushButton_2.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.lineEdit.clear()
        self.reset_radio()

    def cancel_vote(self):
        '''
        Cancels vote, clears the radio buttons but keeps the ID
        :return:
        '''
        self.label_2.setGeometry(QtCore.QRect(40, 110, 135, 16))
        self.label_2.setText("Vote cancelled!")
        self.pushButton_2.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.reset_radio()

    def reset_radio(self):
        '''
        resets the radio buttons
        :return:
        '''
        self.radioButton.setAutoExclusive(False)
        self.radioButton_2.setAutoExclusive(False)

        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(False)

        self.radioButton.setAutoExclusive(True)
        self.radioButton_2.setAutoExclusive(True)


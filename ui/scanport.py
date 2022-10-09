#  Copyright © 2022 Kalynovsky Valentin. All rights reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import socket
from threading import Thread
from time import sleep
import pickle
import os

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtCore import QThread, pyqtSignal

from ui.raw.ui_scanport import Ui_ScanPort


class PortTestThread(QThread):
    attempt = pyqtSignal(bool, str, int)

    def __init__(self, host: str, port: int):
        super(PortTestThread, self).__init__()
        self.host: str = host
        self.port: int = port

    def run(self):
        s = socket.socket()
        try:
            s.connect((self.host, self.port))  # Connection attempt
            # s.settimeout(0.2)  # Timeout for a little more speed
        except:
            self.attempt.emit(False, self.host, self.port)  # Port is closed
        else:
            self.attempt.emit(True, self.host, self.port)  # Port is opened


class ScanPort(QMainWindow, Ui_ScanPort):
    def __init__(self):
        super(ScanPort, self).__init__()
        self.setupUi(self)
        self.FLAG_STOP: bool = False

        self.port_list: list[list] = []

        # Створюю валідатор для поля вводу списку портів
        total = '(\*)'
        number = '(\d|[1-9]\d{1,3}|[1-3]\d{4}|4[0-8]\d{3}|490\d{2}|491[0-4]\d|4915[01])'
        diapason = '(-)'
        separator = '(,)'
        volume = '{0,}'
        rx = QRegularExpression(f'^{total}|({number}{diapason}{number}{separator}|{number}{separator}){volume}$')
        validator = QRegularExpressionValidator(rx, self)
        self.linePorts.setValidator(validator)

        # It's a tracking of button clicks in the window
        self.buttScan.clicked.connect(self.buttScan_Clicked)
        self.linePorts.textChanged.connect(self.buttScan_Active)
        self.toolClear.clicked.connect(self.toolClear_Clicked)
        self.buttSave.clicked.connect(self.buttSave_Clicked)
        self.buttOpen.clicked.connect(self.buttOpen_Clicked)
        self.toolDelete.clicked.connect(self.toolDelete_Clicked)
        self.toolStop.clicked.connect(self.toolStop_Clicked)

        try:
            with open("data/LastPortsTest.save", "rb"):
                self.buttOpen.setEnabled(True)
                self.toolDelete.setEnabled(True)
        except IOError:
            pass

    def buttScan_Active(self):
        if self.linePorts.text() != '':
            self.buttScan.setEnabled(True)
        else:
            self.buttScan.setEnabled(False)

    def buttScan_Clicked(self):
        update = Thread(target=self.portscan, name='Tester', daemon=True)
        update.start()

    def portscan(self):
        self.lineHost.setEnabled(False)
        self.linePorts.setEnabled(False)
        self.buttScan.setEnabled(False)
        self.toolClear.setEnabled(False)
        self.buttSave.setEnabled(False)
        self.buttOpen.setEnabled(False)
        self.toolStop.setEnabled(True)

        if self.lineHost.text() == '':
            self.lineHost.setText(self.lineHost.placeholderText())
        host = self.lineHost.text()

        if self.linePorts.text() == '*':
            for item in range(1, 49152):
                if self.FLAG_STOP:
                    self.FLAG_STOP = False
                    break
                update_thread = PortTestThread(host, item)
                update_thread.start()
                update_thread.attempt.connect(self.publish_result)
                if self.radioOrder.isChecked():
                    update_thread.wait()
                sleep(0.1)
        else:
            if self.linePorts.text()[-1] == ',' or self.linePorts.text()[-1] == '-':
                self.linePorts.setText(self.linePorts.text()[:-1])

            self.port_list = self.linePorts.text().split(',')
            for i in range(len(self.port_list)):
                self.port_list[i] = self.port_list[i].split('-')

            for item in self.port_list:
                if self.FLAG_STOP:
                    self.FLAG_STOP = False
                    break
                if len(item) == 1:
                    update_thread = PortTestThread(host, int(item[0]))
                    update_thread.start()
                    update_thread.attempt.connect(self.publish_result)
                    if self.radioOrder.isChecked():
                        update_thread.wait()
                    sleep(0.1)
                elif len(item) == 2:
                    if int(item[0]) < int(item[1]):
                        for port in range(int(item[0]), int(item[1]) + 1, 1):
                            if self.FLAG_STOP:
                                break
                            update_thread = PortTestThread(host, port)
                            update_thread.start()
                            update_thread.attempt.connect(self.publish_result)
                            if self.radioOrder.isChecked():
                                update_thread.wait()
                            sleep(0.1)
                    else:
                        for port in range(int(item[0]), int(item[1]) - 1, -1):
                            if self.FLAG_STOP:
                                break
                            update_thread = PortTestThread(host, port)
                            update_thread.start()
                            update_thread.attempt.connect(self.publish_result)
                            if self.radioOrder.isChecked():
                                update_thread.wait()
                            sleep(0.1)

        self.lineHost.setEnabled(True)
        self.linePorts.setEnabled(True)
        self.buttScan.setEnabled(True)
        self.toolClear.setEnabled(True)
        self.buttSave.setEnabled(True)
        try:
            with open("data/LastPortsTest.save", "rb"):
                self.buttOpen.setEnabled(True)
        except IOError:
            self.buttOpen.setEnabled(False)
        self.toolStop.setEnabled(False)

    def publish_result(self, result: bool, host: str, port: int):
        # 10,21,50,100,1000-1100,45155,80
        if result:
            self.textResult.append(f"<span style='color: darkgreen;'>[+] {host} : {port} opened</span>")
        else:
            self.textResult.append(f"<span style='color: darkred;'>[!] {host} : {port} closed</span>")

    def toolClear_Clicked(self):
        self.lineHost.clear()
        self.linePorts.clear()
        self.textResult.clear()
        self.toolClear.setEnabled(False)
        self.buttSave.setEnabled(False)
        try:
            with open("data/LastPortsTest.save", "rb"):
                self.buttOpen.setEnabled(True)
        except IOError:
            self.buttOpen.setEnabled(False)

    def buttSave_Clicked(self):
        data = [str(self.lineHost.text()), str(self.linePorts.text()), str(self.textResult.toHtml())]
        if not os.path.exists('data'):
            os.makedirs('data')
        with open("data/LastPortsTest.save", "wb") as save:
            pickle.dump(data, save)
        self.buttSave.setEnabled(False)
        self.buttOpen.setEnabled(False)
        self.toolDelete.setEnabled(True)
        inform = QMessageBox()
        inform.setText("Save done")
        inform.setIcon(QMessageBox.Icon.Information)
        inform.setStandardButtons(QMessageBox.StandardButton.Ok)
        ret: int = inform.exec()
        match ret:
            case QMessageBox.StandardButton.Ok:
                return

    def buttOpen_Clicked(self):
        with open("data/LastPortsTest.save", "rb") as save:
            data = pickle.load(save)
            self.lineHost.setText(data[0])
            self.linePorts.setText(data[1])
            self.textResult.setText(data[2])
        self.toolClear.setEnabled(True)
        self.buttSave.setEnabled(False)
        self.buttOpen.setEnabled(False)

    def toolDelete_Clicked(self):
        os.remove("data/LastPortsTest.save")
        self.buttOpen.setEnabled(False)
        self.toolDelete.setEnabled(False)

    def toolStop_Clicked(self):
        self.FLAG_STOP = True

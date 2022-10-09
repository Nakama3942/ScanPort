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

        self.port_list: list[list] = []

        # Створюю валідатор для поля вводу списку портів
        rx = QRegularExpression('^(((4915[0-2]|491[0-4][0-9]|49[0][0-9][0-9]|4[0-8][0-9][0-9][0-9]|[0-3]?[0-9][0-9][0-9][0-9])(-)(4915[0-2]|491[0-4][0-9]|49[0][0-9][0-9]|4[0-8][0-9][0-9][0-9]|[0-3]?[0-9][0-9][0-9][0-9])(,))|((4915[0-2]|491[0-4][0-9]|49[0][0-9][0-9]|4[0-8][0-9][0-9][0-9]|[0-3]?[0-9][0-9][0-9][0-9])(,))){0,}$')
        validator = QRegularExpressionValidator(rx, self)
        self.linePorts.setValidator(validator)

        # It's a tracking of button clicks in the window
        self.buttScan.clicked.connect(self.buttScan_Clicked)
        self.linePorts.textChanged.connect(self.buttScan_Active)
        self.toolClear.clicked.connect(self.toolClear_Clicked)
        self.buttSave.clicked.connect(self.buttSave_Clicked)
        self.buttOpen.clicked.connect(self.buttOpen_Clicked)
        self.toolDelete.clicked.connect(self.toolDelete_Clicked)

        try:
            with open("data/LastPortsTest.save", "rb"):
                self.toolDelete.setEnabled(True)
        except IOError:
            self.toolDelete.setEnabled(False)

    def buttScan_Active(self):
        if self.linePorts.text() != '':
            self.buttScan.setEnabled(True)
        else:
            self.buttScan.setEnabled(False)

    def buttScan_Clicked(self):
        update = Thread(target=self.portscan, daemon=True)
        update.start()

    def portscan(self):
        self.buttScan.setEnabled(False)
        self.toolClear.setEnabled(False)
        self.buttSave.setEnabled(False)
        self.buttOpen.setEnabled(False)

        if self.lineHost.text() == '':
            self.lineHost.setText(self.lineHost.placeholderText())

        self.port_list = self.linePorts.text().split(',')
        for i in range(len(self.port_list)):
            self.port_list[i] = self.port_list[i].split('-')

        for item in self.port_list:
            host = self.lineHost.text()

            if len(item) == 1:
                update_thread = PortTestThread(host, int(item[0]))
                update_thread.start()
                update_thread.attempt.connect(self.publish_result)
                sleep(0.2)
            elif len(item) == 2:
                if int(item[0]) < int(item[1]):
                    for port in range(int(item[0]), int(item[1]) + 1, 1):
                        update_thread = PortTestThread(host, port)
                        update_thread.start()
                        update_thread.attempt.connect(self.publish_result)
                        sleep(0.2)
                else:
                    for port in range(int(item[0]), int(item[1]) - 1, -1):
                        update_thread = PortTestThread(host, port)
                        update_thread.start()
                        update_thread.attempt.connect(self.publish_result)
                        sleep(0.2)

        self.buttScan.setEnabled(True)
        self.toolClear.setEnabled(True)
        self.buttSave.setEnabled(True)
        self.buttOpen.setEnabled(True)

    def publish_result(self, result: bool, host: str, port: int):
        # 6311,6355-6455,5555
        # 6311,6355-6360,5555
        # 6311,6360-6355,5555
        if result:
            self.textResult.append(f"[+] {host}:{port} opened")
        else:
            self.textResult.append(f"[!] {host}:{port} closed")

    def toolClear_Clicked(self):
        self.textResult.clear()
        self.toolClear.setEnabled(False)
        self.buttSave.setEnabled(False)
        self.buttOpen.setEnabled(True)

    def buttSave_Clicked(self):
        data = [str(self.lineHost.text()), str(self.linePorts.text()), str(self.textResult.toPlainText())]
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
        try:
            with open("data/LastPortsTest.save", "rb") as save:
                data = pickle.load(save)
                self.lineHost.setText(data[0])
                self.linePorts.setText(data[1])
                self.textResult.setText(data[2])
            self.toolClear.setEnabled(True)
            self.buttSave.setEnabled(False)
            self.buttOpen.setEnabled(False)
        except:
            warning = QMessageBox()
            warning.setText("No save")
            warning.setIcon(QMessageBox.Icon.Warning)
            warning.setStandardButtons(QMessageBox.StandardButton.Ok)
            ret: int = warning.exec()
            match ret:
                case QMessageBox.StandardButton.Ok:
                    self.buttOpen.setEnabled(False)

    def toolDelete_Clicked(self):
        os.remove("data/LastPortsTest.save")
        self.buttOpen.setEnabled(False)
        self.toolDelete.setEnabled(False)

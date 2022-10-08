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

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator

from ui.raw.ui_scanport import Ui_ScanPort


class ScanPort(QMainWindow, Ui_ScanPort):
    def __init__(self):
        super(ScanPort, self).__init__()
        self.setupUi(self)

        self.port_list: list = []

        # Створюю валідатор для поля вводу списку портів
        rx = QRegularExpression('^(((4915[0-2]|491[0-4][0-9]|49[0][0-9][0-9]|4[0-8][0-9][0-9][0-9]|[0-3]?[0-9][0-9][0-9][0-9])(-)(4915[0-2]|491[0-4][0-9]|49[0][0-9][0-9]|4[0-8][0-9][0-9][0-9]|[0-3]?[0-9][0-9][0-9][0-9])(,))|((4915[0-2]|491[0-4][0-9]|49[0][0-9][0-9]|4[0-8][0-9][0-9][0-9]|[0-3]?[0-9][0-9][0-9][0-9])(,))){0,}$')
        validator = QRegularExpressionValidator(rx1, self)
        self.linePorts.setValidator(validator)

        # It's a tracking of button clicks in the window
        self.buttScan.clicked.connect(self.buttScan_Clicked)
        # self.listLetters.activated.connect(lambda: self.listLetters_Activated(self.listLetters.currentRow()))
        # self.actionRelogin.triggered.connect(lambda: self.actionRelogin_Triggered())
        # self.actionRedownload.triggered.connect(lambda: self.actionRedownload_Triggered())

    def buttScan_Clicked(self):
        # 6351,6352,1850,49152,8000-9000,987
        self.port_list = self.linePorts.text().split(',')
        for i in range(len(self.port_list)):
            self.port_list[i] = self.port_list[i].split('-')
        self.textResult.setText(str(self.port_list))  # Тест роботи сплітів

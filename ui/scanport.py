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

from ui.raw.ui_scanport import Ui_ScanPort


class ScanPort(QMainWindow, Ui_ScanPort):
    def __init__(self):
        super(ScanPort, self).__init__()
        self.setupUi(self)

        # # It's a tracking of button clicks in the window
        # self.buttSend.released.connect(lambda: self.buttSend_Released())
        # self.listLetters.activated.connect(lambda: self.listLetters_Activated(self.listLetters.currentRow()))
        # self.actionRelogin.triggered.connect(lambda: self.actionRelogin_Triggered())
        # self.actionRedownload.triggered.connect(lambda: self.actionRedownload_Triggered())

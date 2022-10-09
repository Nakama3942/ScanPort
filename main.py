import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication

from ui.scanport import ScanPort


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ScanPort()
    ui.show()
    sys.exit(app.exec())

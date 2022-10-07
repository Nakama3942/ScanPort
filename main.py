import socket
import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication

from ui.scanport import ScanPort


def is_port_open(host, port):
    s = socket.socket()
    try:
        s.connect((host, port))  # Connection attempt
        # s.settimeout(0.05)  # Timeout for a little more speed
    except:
        return False  # Port is closed
    else:
        return True  # Port is opened


if __name__ == '__main__':
    # host = input("Enter the host:")
    #
    # for port in range(1, 1025):
    #     if is_port_open(host, port):
    #         print(f"[+] {host}:{port} opened")
    #     else:
    #         print(f"[!] {host}:{port} closed")

    app = QApplication(sys.argv)
    ui = ScanPort()
    ui.show()
    sys.exit(app.exec())

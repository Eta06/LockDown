# Platforms: Windows, Linux

import os
import time
import json
import psutil
from PyQt5 import uic, QtWidgets, QtGui, QtNetwork, QtCore
from PyQt5.QtGui import QMovie, QTextOption
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from config import readAppConfig, updateAppConfig


def getAllDrives():
    system_drives = []
    usb_drives = []
    if os.name == 'nt':
        # Windows
        for drive in psutil.disk_partitions():
            if 'fixed' in drive.opts:
                system_drives.append(drive.device)
            else:
                usb_drives.append(drive.device)
    else:
        # Linux
        for part in psutil.disk_partitions():
            if 'loop' not in part.device:
                if 'rw,' in part.opts:
                    usb_drives.append(part.mountpoint)
                else:
                    system_drives.append(part.mountpoint)
    return system_drives, usb_drives

"""
while True:
    system_drives, usb_drives = getAllDrives()
    print("System Drives:", system_drives)
    print("USB Drives:", usb_drives)
    time.sleep(1)
"""

if __name__ == "__main__":
    localconfig = readAppConfig()
    if localconfig["app_language"] == "":
        print("Please select a language first.")
    app = QApplication([])
    window = uic.loadUi("../UI/anlamadim.ui")
    window.show()
    app.exec_()



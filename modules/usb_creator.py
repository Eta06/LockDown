# Platforms: Windows, Linux

import os
import time
import json
import psutil


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

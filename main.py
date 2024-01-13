from PyQt5 import uic, QtWidgets, QtGui, QtNetwork, QtCore
from PyQt5.QtGui import QMovie, QTextOption
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from modules.config import readAppConfig, updateAppConfig


if __name__ == "__main__":
    localconfig = readAppConfig()
    if localconfig["app_language"] == "":
        print("Please select a language first.")
    app = QApplication([])
    window = uic.loadUi("../UI/lang.ui")
    label = window.findChild(QtWidgets.QLabel, "label")
    comboBox = window.findChild(QtWidgets.QComboBox, "comboBox")

    # Add language options with emojis to the combo box
    comboBox.addItem("English 🇬🇧")
    comboBox.addItem("Turkish 🇹🇷")
    comboBox.addItem("Russian 🇷🇺")
    comboBox.addItem("Spanish 🇪🇸")

    # Update the label text for clarity
    label.setText("Select your language:")

    window.show()
    app.exec_()
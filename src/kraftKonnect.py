from src.core.CoreWindow import CoreWindow
from PyQt6 import QtWidgets


def run():
    app = QtWidgets.QApplication([])
    # TODO check for xml/yaml view configuration and pass as argument to CoreWindow which will take care of creation
    window = CoreWindow()
    app.exec()

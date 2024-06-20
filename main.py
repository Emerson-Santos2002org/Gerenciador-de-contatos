#dia 6

import sys
from PyQt6.QtWidgets import QApplication
from controller.controller import MainController

def main():
    app = QApplication(sys.argv)
    controller = MainController()
    controller.show_main_window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
from PyQt6.QtWidgets import QMainWindow, QStackedWidget
from PyQt6.QtGui import QIcon
from res.string import constants as consts

class MainWindow(QMainWindow):
    
    def __init__(self, controller) -> None:
        super().__init__()
        self.controller = controller
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle(consts.WINDOW_TITLE)
        self.setWindowIcon(QIcon(consts.ICON_PATH))
        self.resize(480,640)
        
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        
    def set_view(self, view):
        self.central_widget.addWidget(view)
        self.central_widget.setCurrentWidget(view)   
        

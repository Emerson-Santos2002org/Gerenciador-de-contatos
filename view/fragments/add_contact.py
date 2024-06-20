from PyQt6.QtWidgets import QWidget, QTextEdit, QVBoxLayout

class AddContact(QWidget):
    
    def __init__(self) -> None:
        
        layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(layout)
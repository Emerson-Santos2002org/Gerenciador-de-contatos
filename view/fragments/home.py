from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton

class HomeView(QWidget):
    
    def __init__(self, controller) -> None:
        super().__init__()
        self.controller = controller
        self.setup_ui()
        
    def setup_ui(self):
            
        layout = QVBoxLayout()
        
        self.button_names = ["Adicionar Contato", "Visualizar Contatos"]
        for name in self.button_names:
            button = QPushButton(name)
            button.clicked.connect(lambda checked, n=name: self.onClickListener(n))
            layout.addWidget(button)
            
        self.setLayout(layout)    
            
    def onClickListener(self, name):
        print(f"{name} clicado!")
from view.main_window import MainWindow
from view.fragments.home import HomeView

class MainController():
    
    def __init__(self) -> None:
        
        self.main_window = MainWindow(self)
        
        self.home_view = HomeView(self)
        
    def show_main_window(self):
        self.main_window.show()
        self.show_first_view()
        
    def show_first_view(self):
        self.main_window.set_view(self.home_view)    
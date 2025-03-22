from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
import sys
from main_window import Ui_MainWindow  # Assuming you have the main_window.py file with Ui_MainWindow class.
from subfolder.main_window import Ui_MainWindow

import sys
sys.path.append('path_to_the_folder_containing_main_window')

from main_window import Ui_MainWindow



class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.on_button_click)

    def on_button_click(self):
        self.ui.label.setText("Button Clicked!")

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()  # Uncomment this line to show the window
    sys.exit(app.exec_())

from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt

class SearchBar(QFrame):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("""
            QFrame {
                background-color: #007bff;
                border: 1px solid #dcdcdc;
                border-radius: 10px;
                margin: 10px;
                padding: 5px;
            }
        """)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setAlignment(Qt.AlignLeft)  # This aligns the entire layout to the left

        search_input = QLineEdit()
        search_input.setPlaceholderText("Search...")
        search_input.setFixedHeight(35)
        search_input.setFixedWidth(500)
        search_input.setStyleSheet(""" 
            QLineEdit {
                font-size: 10pt;
                padding: 0 10px;
                border: 1px solid #ccc;
                border-radius: 15px;
                background-color: #ffffff;
                color: #333;
                # text-align: left;  # This ensures text alignment within the input
            }
            QLineEdit:focus {
                border: 1px solid #007bff;
                box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
                
            }
        """)
        layout.addWidget(search_input, alignment=Qt.AlignLeft)  # This aligns the widget to the left
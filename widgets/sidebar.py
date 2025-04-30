from PyQt5.QtWidgets import QFrame, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Sidebar(QFrame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border-right: 2px solid #dcdcdc;
            }
        """)
        self.setFixedWidth(250)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Logo
        logo = QLabel("AUTOPYNET")
        logo.setFont(QFont("Arial", 16, QFont.Bold))
        logo.setAlignment(Qt.AlignCenter)
        logo.setStyleSheet("""
            QLabel {
                color: #343a40;
                margin-top: 20px;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(logo)

        # Divider
        divider = QFrame()
        divider.setFrameShape(QFrame.HLine)
        divider.setFrameShadow(QFrame.Sunken)
        divider.setStyleSheet("color: #dcdcdc;")
        layout.addWidget(divider)

        # Navigation buttons
        buttons = [
            ("Home", self.parent.open_main_page),
            ("Vendor", self.parent.open_choose_vendor_page),
            ("My Files", self.parent.open_my_files_page),
            # ("Status", self.parent.open_status_page),
            ("Logs", self.parent.open_log_window)  # New Logs button
        ]

        for text, callback in buttons:
            btn = QPushButton(text)
            btn.setFixedHeight(50)
            btn.setStyleSheet("""
                QPushButton {
                    text-align: left;
                    padding-left: 20px;
                    color: #343a40;
                    background-color: #ffffff;
                    font-size: 14pt;
                    font-family: Arial;
                    border: none;
                }
                QPushButton:hover {
                    background-color: #e9ecef;
                    border-left: 5px solid #007bff;
                }
                QPushButton:pressed {
                    background-color: #007bff;
                    color: #ffffff;
                }
            """)
            btn.clicked.connect(callback)
            layout.addWidget(btn)

        layout.addStretch()

        # Footer
        footer = QLabel("© 2024 AutoPyNet")
        footer.setFont(QFont("Arial", 10))
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("""
            QLabel {
                color: #6c757d;
                margin-bottom: 10px;
            }
        """)
        layout.addWidget(footer)

        self.setLayout(layout)
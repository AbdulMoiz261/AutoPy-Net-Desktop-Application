# pages/vendor_page.py
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class VendorPage(QFrame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent  # parent should be AutoPynetDashboard instance
        self.setup_ui()

    def setup_ui(self):
        vendor_layout = QVBoxLayout()
        vendor_layout.setSpacing(20)
        vendor_layout.addStretch()

        # Box Frame to hold heading + buttons
        box_frame = QFrame()
        box_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 2px solid #dee2e6;
                border-radius: 16px;
                padding: 40px;
            }
        """)
        box_layout = QVBoxLayout()
        box_layout.setSpacing(30)
        box_layout.setAlignment(Qt.AlignCenter)

        center_text = QLabel("Select Vendor")
        center_text.setFont(QFont("Arial", 24, QFont.Bold))
        center_text.setAlignment(Qt.AlignCenter)
        center_text.setStyleSheet("""
            font-size: 24pt;
            font-weight: bold;
            color: #343a40;
            font-family: 'Arial', sans-serif;
            border: none;
        """)
        box_layout.addWidget(center_text, alignment=Qt.AlignCenter)

        button_container = QHBoxLayout()
        button_container.setSpacing(50)
        button_container.setAlignment(Qt.AlignCenter)

        cisco_button = QPushButton("Cisco")
        cisco_button.setFixedSize(250, 150)
        cisco_button.setStyleSheet("""
            QPushButton {
                font-size: 16pt;
                font-family: 'Arial', sans-serif;
                padding: 20px;
                border: 2px solid #007bff;
                border-radius: 12px;
                background-color: white;
                color: #007bff;
            }
            QPushButton:hover {
                background-color: #007bff;
                color: white;
                border-color: #0056b3;
                box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
            }
            QPushButton:pressed {
                background-color: #0056b3;
                color: white;
            }
        """)
        cisco_button.clicked.connect(lambda: self.set_vendor_and_navigate("Cisco"))

        juniper_button = QPushButton("Juniper")
        juniper_button.setFixedSize(250, 150)
        juniper_button.setStyleSheet("""
            QPushButton {
                font-size: 16pt;
                font-family: 'Arial', sans-serif;
                padding: 20px;
                border: 2px solid #28a745;
                border-radius: 12px;
                background-color: white;
                color: #28a745;
            }
            QPushButton:hover {
                background-color: #28a745;
                color: white;
                border-color: #218838;
                box-shadow: 0 4px 8px rgba(40, 167, 69, 0.3);
            }
            QPushButton:pressed {
                background-color: #218838;
                color: white;
            }
        """)
        juniper_button.clicked.connect(lambda: self.set_vendor_and_navigate("Juniper"))

        button_container.addWidget(cisco_button)
        button_container.addWidget(juniper_button)

        box_layout.addLayout(button_container)
        box_frame.setLayout(box_layout)

        # Align the box frame to the top-left corner
        vendor_layout.addWidget(box_frame, alignment=Qt.AlignTop | Qt.AlignLeft)
        vendor_layout.addStretch()

        back_button = QPushButton("Back")
        back_button.setFixedSize(120, 40)
        back_button.setStyleSheet("""
            QPushButton {
                font-size: 14pt;
                font-family: 'Arial', sans-serif;
                background-color: #6c757d;
                color: white;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #5a6268;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            }
        """)
        back_button.clicked.connect(self.parent.open_main_page)

        back_button_layout = QHBoxLayout()
        back_button_layout.addWidget(back_button, alignment=Qt.AlignLeft)
        back_button_layout.setContentsMargins(20, 20, 20, 20)
        vendor_layout.addLayout(back_button_layout)

        self.setLayout(vendor_layout)
        self.setFixedSize(1680, 970)
        self.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;
                border-radius: 20px;
                border: 2px solid #dcdcdc;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            }
        """)

    def set_vendor_and_navigate(self, vendor):
        """Set the selected vendor and navigate to device type page."""
        self.parent.selected_vendor = vendor
        self.parent.open_device_type_page()

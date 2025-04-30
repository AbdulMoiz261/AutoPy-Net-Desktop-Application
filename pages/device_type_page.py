# pages/device_type_page.py
from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class DeviceTypePage(QFrame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.vendor = None
        self.init_ui()

    def set_vendor(self, vendor):
        self.vendor = vendor

    def init_ui(self):
        page_layout = QVBoxLayout()
        page_layout.setSpacing(30)
        page_layout.addStretch()

        # Box container
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

        title_label = QLabel("Select Type of Device")
        title_label.setFont(QFont("Arial", 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            QLabel {
                border: none;
                background: transparent;
                color: #343a40;
                font-family: 'Arial', sans-serif;
            }
        """)
        box_layout.addWidget(title_label, alignment=Qt.AlignCenter)

        button_container = QHBoxLayout()
        button_container.setSpacing(50)
        button_container.setAlignment(Qt.AlignCenter)

        self.switch_button = QPushButton("Switch")
        self.switch_button.setFixedSize(250, 150)
        self.switch_button.setStyleSheet("""
            QPushButton {
                font-size: 16pt;
                font-family: 'Arial', sans-serif;
                padding: 20px;
                border: 2px solid #007bff;
                border-radius: 12px;
                background-color: white;
                color: #007bff;
                transition: all 0.3s ease-in-out;
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
        self.switch_button.clicked.connect(lambda: self.set_device_type_and_navigate("switch"))

        self.router_button = QPushButton("Router")
        self.router_button.setFixedSize(250, 150)
        self.router_button.setStyleSheet("""
            QPushButton {
                font-size: 16pt;
                font-family: 'Arial', sans-serif;
                padding: 20px;
                border: 2px solid #28a745;
                border-radius: 12px;
                background-color: white;
                color: #28a745;
                transition: all 0.3s ease-in-out;
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
        self.router_button.clicked.connect(lambda: self.set_device_type_and_navigate("router"))

        button_container.addWidget(self.switch_button)
        button_container.addWidget(self.router_button)

        box_layout.addLayout(button_container)
        box_frame.setLayout(box_layout)

        # Align the box frame to the top-left corner
        page_layout.addWidget(box_frame, alignment=Qt.AlignTop | Qt.AlignLeft)
        page_layout.addStretch()

        back_button = QPushButton("Back")
        back_button.setFixedSize(120, 40)
        back_button.setStyleSheet("""
            QPushButton {
                font-size: 14pt;
                font-family: 'Arial', sans-serif;
                background-color: #6c757d;
                color: white;
                border-radius: 8px;
                transition: all 0.3s ease-in-out;
            }
            QPushButton:hover {
                background-color: #5a6268;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            }
        """)
        back_button.clicked.connect(self.parent.open_choose_vendor_page)

        back_button_layout = QHBoxLayout()
        back_button_layout.addWidget(back_button, alignment=Qt.AlignLeft)
        back_button_layout.setContentsMargins(20, 20, 20, 20)
        page_layout.addLayout(back_button_layout)

        self.setLayout(page_layout)
        self.setFixedSize(1680, 970)
        self.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;
                border-radius: 20px;
                border: 2px solid #dcdcdc;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            }
        """)

    def set_device_type_and_navigate(self, device_type):
        """Set the selected device type and navigate to device selection page."""
        device_type = device_type.lower()
        self.parent.selected_device_type = device_type

        print(f"Selected device type: {device_type}")
        print(f"Parent's selected_device_type: {self.parent.selected_device_type}")

        self.parent.open_device_selection_page()

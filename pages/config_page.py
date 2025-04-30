from PyQt5.QtWidgets import QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class ConfigPage(QFrame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.device_type = None
        self.setup_ui()

    def set_device_type(self, device_type):
        self.device_type = device_type

    def setup_ui(self):
        page_layout = QVBoxLayout()
        page_layout.setSpacing(0)
        page_layout.setContentsMargins(20, 20, 20, 20)  # Adds space from window edges

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
        box_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        center_text = QLabel("Select Device Configuration")
        center_text.setFont(QFont("Arial", 24, QFont.Bold))
        center_text.setAlignment(Qt.AlignLeft)
        center_text.setStyleSheet("""
            font-size: 24pt;
            font-weight: bold;
            color: #343a40;
            font-family: 'Arial', sans-serif;
            border: none;
        """)
        box_layout.addWidget(center_text, alignment=Qt.AlignLeft)

        button_container = QHBoxLayout()
        button_container.setSpacing(30)
        button_container.setAlignment(Qt.AlignLeft)

        single_device_button = QPushButton("Single Device")
        single_device_button.setFixedSize(250, 150)
        single_device_button.setStyleSheet("""
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
        single_device_button.clicked.connect(lambda: self.set_configuration_and_navigate("Single"))

        multiple_device_button = QPushButton("Multiple Devices")
        multiple_device_button.setFixedSize(250, 150)
        multiple_device_button.setStyleSheet("""
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
        multiple_device_button.clicked.connect(lambda: self.set_configuration_and_navigate("Multiple"))

        button_container.addWidget(single_device_button)
        button_container.addWidget(multiple_device_button)

        box_layout.addLayout(button_container)
        box_frame.setLayout(box_layout)

        # ✅ Align box to vertical center and horizontal left
        page_layout.addWidget(box_frame, alignment=Qt.AlignVCenter | Qt.AlignLeft)

        # Back button at bottom
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
        back_button.clicked.connect(self.parent.open_device_type_page)

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

    def set_configuration_and_navigate(self, configuration):
        """Set the selected configuration and navigate to appropriate page."""
        self.parent.selected_configuration = configuration
        if configuration == "Single":
            self.parent.open_single_device_page()
        else:
            self.parent.open_multiple_device_page()

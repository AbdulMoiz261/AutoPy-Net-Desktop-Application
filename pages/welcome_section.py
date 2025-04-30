import os
from PyQt5.QtWidgets import (QFrame, QHBoxLayout, QVBoxLayout, QLabel, 
                             QPushButton, QListWidget, QWidget, QFileDialog)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QSize

class YourParentClass(QWidget):  
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Your App Title')
        self.setGeometry(100, 100, 800, 600)

        # Create instance of WelcomeSection
        self.welcome_section = WelcomeSection(self)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.welcome_section)

    def open_choose_vendor_page(self):
        print("Choose Vendor Page Opened")

    def open_all_files_page(self):
        print("All Files Page Opened")

    def open_file_upload_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("All Files (*.*)")
        file_dialog.setViewMode(QFileDialog.List)

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            for file in selected_files:
                # Save to "My Files" directory
                my_files_directory = os.path.expanduser("~/My Files")
                if not os.path.exists(my_files_directory):
                    os.makedirs(my_files_directory)

                file_name = os.path.basename(file)
                destination_path = os.path.join(my_files_directory, file_name)

                # Prevent overwriting
                if not os.path.exists(destination_path):
                    os.rename(file, destination_path)  # Or use shutil.copy()
                    print(f"Uploaded: {file_name}")

                    # ✅ Corrected: Add to recent files
                    self.welcome_section.add_recent_file(file_name)


class WelcomeSection(QFrame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        welcome_frame = QFrame()
        welcome_frame.setStyleSheet("""QFrame { background-color: transparent; }""")
        welcome_layout = QHBoxLayout(welcome_frame)

        # Device Configuration Section
        device_section_frame = QFrame()
        device_section_frame.setStyleSheet(""" 
            QFrame {
                background-color: rgb(234, 235, 253);
                border: none;
                border-radius: 10px;
                padding: 15px;
                box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.2);
            }
        """)
        device_section_layout = QVBoxLayout(device_section_frame)

        network_label = QLabel("Network Device to\nconfigure?")
        network_label.setFont(QFont("Arial", 15, QFont.Bold))
        network_label.setAlignment(Qt.AlignLeft)
        network_label.setStyleSheet("""QLabel { border: none; margin-bottom: 15px; }""")

        choose_button = QPushButton("Choose Vendor")
        choose_button.setIcon(QIcon.fromTheme("network-server"))
        choose_button.setIconSize(QSize(24, 24))
        choose_button.setStyleSheet(""" 
            QPushButton {
                background-color: #007bff;
                color: white;
                border-radius: 20px;
                padding: 15px 20px;
                font-size: 11pt;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        choose_button.setFixedWidth(250)
        choose_button.clicked.connect(self.parent.open_choose_vendor_page)

        device_section_layout.addWidget(network_label)
        device_section_layout.addWidget(choose_button)
        device_section_layout.setAlignment(Qt.AlignCenter)
        device_section_frame.setFixedHeight(220)
        device_section_layout.setContentsMargins(0, 0, 0, 0)

        # Files Section
        files_section_frame = QFrame()
        files_section_frame.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border-radius: 10px;
            }
            QLabel {
                color: #343a40;
                font-weight: bold;
                padding: 10px 15px 5px 15px;
            }
        """)
        files_section_layout = QVBoxLayout(files_section_frame)
        files_section_layout.setContentsMargins(0, 0, 0, 0)
        files_section_layout.setSpacing(0)

        # Recent Files section
        recent_files_widget = QWidget()
        recent_files_widget.setStyleSheet("background-color: #f8f9fa; border-radius: 10px 10px 0 0;")
        recent_files_layout = QVBoxLayout(recent_files_widget)
        recent_files_layout.setContentsMargins(15, 0, 15, 5)
        recent_files_layout.setSpacing(0)

        files_label = QLabel("Recent Files")
        files_label.setFont(QFont("Arial", 20, QFont.Bold))
        recent_files_layout.addWidget(files_label)

        self.file_list = QListWidget()
        self.file_list.setStyleSheet(""" 
            QListWidget {
                background-color: #ffffff;
                border: none;
                border-radius: 0 0 10px 10px;
                padding: 5px 15px;
                border: 1px solid #e0e0e0;
            }
            QListWidget::item {
                padding: 8px;
                border-bottom: 1px solid #f0f0f0;
            }
            QListWidget::item:hover {
                background-color: #f8f9fa;
            }
            QListWidget::item:selected {
                background-color: #007bff;
                color: white;
            }
        """)

        # Load existing files from directory
        my_files_directory = os.path.expanduser("~/My Files")
        if os.path.exists(my_files_directory):
            file_names = os.listdir(my_files_directory)
            for file_name in file_names:
                full_path = os.path.join(my_files_directory, file_name)
                size = self.get_file_size(full_path)
                self.file_list.addItem(f"{file_name} ({size})")

        self.file_list.setFixedHeight(120)
        recent_files_layout.addWidget(self.file_list)

        # Action Buttons
        button_widget = QWidget()
        button_widget.setStyleSheet("background-color: #f8f9fa; border-radius: 0 0 10px 10px; padding: 10px 15px;")
        button_layout = QHBoxLayout(button_widget)
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setSpacing(10)

        see_all_button = QPushButton("View All")
        see_all_button.setIcon(QIcon.fromTheme("document-open"))
        see_all_button.setStyleSheet(""" 
            QPushButton {
                background-color: #6c757d;
                color: white;
                border-radius: 15px;
                padding: 8px 12px;
                font-size: 10pt;
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
        """)
        see_all_button.setFixedWidth(120)
        see_all_button.clicked.connect(self.parent.open_all_files_page)

        upload_button = QPushButton("Upload")
        upload_button.setIcon(QIcon.fromTheme("document-import"))
        upload_button.setStyleSheet(""" 
            QPushButton {
                background-color: #28a745;
                color: white;
                border-radius: 15px;
                padding: 8px 12px;
                font-size: 10pt;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        upload_button.setFixedWidth(120)
        upload_button.clicked.connect(self.parent.open_file_upload_dialog)

        button_layout.addStretch()
        button_layout.addWidget(see_all_button)
        button_layout.addWidget(upload_button)

        recent_files_layout.addWidget(button_widget)
        files_section_layout.addWidget(recent_files_widget)

        welcome_layout.addWidget(device_section_frame)
        welcome_layout.addWidget(files_section_frame)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(welcome_frame)

    def get_file_size(self, file_path):
        """Helper to return readable file size"""
        size = os.path.getsize(file_path)
        if size < 1024:
            return f"{size} B"
        elif size < 1048576:
            return f"{size / 1024:.2f} KB"
        else:
            return f"{size / 1048576:.2f} MB"

    def add_recent_file(self, file_name):
        """Add the uploaded file to recent list"""
        my_files_directory = os.path.expanduser("~/My Files")
        file_path = os.path.join(my_files_directory, file_name)
        size = self.get_file_size(file_path)
        self.file_list.addItem(f"{file_name} ({size})")

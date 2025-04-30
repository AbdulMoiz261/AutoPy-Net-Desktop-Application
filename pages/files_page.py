import os
from PyQt5.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
                            QListWidget, QFileDialog, QAbstractItemView, QListWidgetItem, QMessageBox, QTextEdit)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize, QDateTime


class FilesPage(QFrame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("""
            QFrame {
                background-color: #ffffff;
                border-radius: 10px;
            }
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Header
        header = QHBoxLayout()
        
        title = QLabel("My Files")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setStyleSheet("color: #343a40;")
        
        header.addWidget(title)
        header.addStretch()
        
        upload_btn = QPushButton("Upload Files")
        upload_btn.setIcon(QIcon.fromTheme("document-import"))
        upload_btn.setIconSize(QSize(20, 20))
        upload_btn.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                border-radius: 5px;
                padding: 8px 15px;
                font-size: 11pt;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        upload_btn.clicked.connect(self.open_file_upload_dialog)
        header.addWidget(upload_btn)
        
        layout.addLayout(header)

        # File list
        self.file_list = QListWidget()
        self.file_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.file_list.setStyleSheet("""
            QListWidget {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 5px;
                padding: 5px;
            }
            QListWidget::item {
                padding: 10px;
                border-bottom: 1px solid #e9ecef;
            }
            QListWidget::item:hover {
                background-color: #e9ecef;
            }
            QListWidget::item:selected {
                background-color: #007bff;
                color: white;
            }
        """)
        
        # Initialize file list
        self.files = []
        
        layout.addWidget(self.file_list)
        
        # Text Edit for file content preview
        self.file_content_display = QTextEdit()
        self.file_content_display.setReadOnly(True)  # Make it read-only
        layout.addWidget(self.file_content_display)

        layout.addStretch()
        
        # Action buttons
        action_buttons = QHBoxLayout()
        action_buttons.setSpacing(10)
        
        back_btn = QPushButton("Back")
        back_btn.setIcon(QIcon.fromTheme("go-previous"))
        back_btn.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border-radius: 5px;
                padding: 8px 15px;
                font-size: 11pt;
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
        """)
        back_btn.clicked.connect(self.parent.open_main_page)
        
        delete_btn = QPushButton("Delete Selected")
        delete_btn.setIcon(QIcon.fromTheme("edit-delete"))
        delete_btn.setStyleSheet("""
            QPushButton {
                background-color: #dc3545;
                color: white;
                border-radius: 5px;
                padding: 8px 15px;
                font-size: 11pt;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
        """)
        delete_btn.clicked.connect(self.delete_selected_files)
        
        action_buttons.addWidget(back_btn)
        action_buttons.addStretch()
        action_buttons.addWidget(delete_btn)
        
        layout.addLayout(action_buttons)
        
        self.setLayout(layout)

        # Connect double-click event on the list
        self.file_list.itemDoubleClicked.connect(self.open_file_content)

    def populate_file_list(self):
        self.file_list.clear()
        
        for file in self.files:
            item = QListWidgetItem()
            item.setText(f"{file['name']}\nSize: {file['size']} | Modified: {file['date']}")
            
            # Set different icons based on file type
            if file['type'] == "text":
                item.setIcon(QIcon.fromTheme("text-plain"))
            
            # Set the tooltip to display file info when hovered
            item.setToolTip(f"Name: {file['name']}\nType: {file['type']}\nSize: {file['size']}\nModified: {file['date']}")
            
            self.file_list.addItem(item)

    def open_file_upload_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Text Files (*.txt)")  # Only allow .txt files

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            for file_path in selected_files:
                if file_path.endswith(".txt"):
                    # Check if the file already exists in the list by comparing file paths
                    if not self.is_file_duplicate(file_path):
                        # Gather file details
                        file_name = os.path.basename(file_path)
                        file_size = self.get_file_size(file_path)
                        file_date = self.get_file_date(file_path)
                        
                        file_info = {
                            "name": file_name,
                            "type": "text",
                            "size": file_size,
                            "date": file_date,
                            "path": file_path  # Store the file path
                        }
                        
                        self.files.append(file_info)
                        self.populate_file_list()  # Refresh the list with the new file
                    else:
                        self.show_warning("Duplicate File", "This file has already been uploaded.")
                else:
                    # Show a warning if a non-txt file is selected
                    self.show_warning("Invalid File", "Only text files (.txt) can be uploaded.")

    def is_file_duplicate(self, file_path):
        """Check if the file already exists in the list by comparing the file path"""
        for file in self.files:
            if file['path'] == file_path:
                return True
        return False

    def get_file_size(self, file_path):
        try:
            size = os.path.getsize(file_path)
            return f"{size // 1024} KB"  # Convert to KB
        except Exception as e:
            return "Unknown"

    def get_file_date(self, file_path):
        try:
            timestamp = os.path.getmtime(file_path)
            return QDateTime.fromSecsSinceEpoch(timestamp).toString("yyyy-MM-dd HH:mm:ss")
        except Exception as e:
            return "Unknown"

    def show_warning(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec_()

    def delete_selected_files(self):
        selected_items = self.file_list.selectedItems()
        if not selected_items:
            return
        
        for item in selected_items:
            row = self.file_list.row(item)
            self.file_list.takeItem(row)
            
            # Remove the file from the list of files (self.files)
            file_name = item.text().split("\n")[0]  # Extract the file name from item text
            self.remove_file_from_list(file_name)
        
        # If the file content is currently displayed, clear the text
        self.clear_file_content_display()

    def remove_file_from_list(self, file_name):
        """Remove the file from self.files list by file name"""
        self.files = [file for file in self.files if file['name'] != file_name]

    def open_file_content(self, item):
        # Get the file path from the item
        selected_file_name = item.text().split("\n")[0]  # Get the file name from item text
        file_path = None
        
        # Find the file in the list by name and get the path
        for file in self.files:
            if file['name'] == selected_file_name:
                file_path = file['path']
                break
        
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                    self.file_content_display.setText(content)  # Display the content in QTextEdit
            except Exception as e:
                self.show_warning("Error", "Could not open the file.")
                
    def clear_file_content_display(self):
        """Clear the file content display area."""
        self.file_content_display.clear()

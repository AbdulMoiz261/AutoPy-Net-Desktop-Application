import importlib
import traceback
from PyQt5.QtWidgets import (QFrame, QVBoxLayout, QHBoxLayout, QPushButton,
                            QLabel, QTableWidget, QWidget, QMessageBox)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MultipleDevicePage(QFrame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.current_device_type = "switch"  # Track current device type
        self.current_vendor = None  # Track current vendor
        self.init_ui()

    def init_ui(self):
        content_layout = QVBoxLayout()

        device_selection_frame = QFrame()
        container_layout = QVBoxLayout()
        device_selection_frame.setLayout(container_layout)
        device_selection_frame.setFixedSize(1680, 970)
        device_selection_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 20px;
                border: 2px solid #dcdcdc;
            }
        """)

        title_label = QLabel("Multiple Devices")
        title_label.setFont(QFont("Arial", 18, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("margin: 20px 0; font-weight: bold;")
        container_layout.addWidget(title_label)

        # Create tab-like buttons for Switch/Router selection
        device_type_layout = QHBoxLayout()
        device_type_layout.setSpacing(0)

        self.switch_button = QPushButton("Switch")
        self.router_button = QPushButton("Router")

        for btn in [self.switch_button, self.router_button]:
            btn.setFixedHeight(40)
            btn.setFont(QFont("Arial", 12))

        self.switch_button.clicked.connect(lambda: self.set_active_device_type("switch"))
        self.router_button.clicked.connect(lambda: self.set_active_device_type("router"))

        device_type_layout.addWidget(self.switch_button)
        device_type_layout.addWidget(self.router_button)
        device_type_layout.addStretch()
        container_layout.addLayout(device_type_layout)

        # Create the table widget
        self.multiple_device_table = QTableWidget()
        self.multiple_device_table.setColumnCount(1)
        self.multiple_device_table.setHorizontalHeaderLabels(["Code ID and Description"])
        self.multiple_device_table.setColumnWidth(0, 1650)
        self.multiple_device_table.verticalHeader().setVisible(False)
        self.multiple_device_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.multiple_device_table.setEditTriggers(QTableWidget.NoEditTriggers)

        self.multiple_device_table.setStyleSheet("""
            QTableWidget {
                background-color: #f9f9f9;
                border: none;
                font-size: 12pt;
                gridline-color: #dcdcdc;
            }
            QHeaderView::section {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                border: none;
                padding: 8px;
            }
        """)

        container_layout.addWidget(self.multiple_device_table)

        back_button = QPushButton("Back")
        back_button.setFixedSize(100, 40)
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border-radius: 8px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
        """)
        back_button.clicked.connect(self.parent.open_device_selection_page)

        back_button_layout = QHBoxLayout()
        back_button_layout.addWidget(back_button)
        back_button_layout.setAlignment(Qt.AlignLeft)
        container_layout.addLayout(back_button_layout)

        content_layout.addWidget(device_selection_frame, alignment=Qt.AlignCenter)
        self.setLayout(content_layout)

    def set_selected_options(self, vendor, device_type):
        self.current_vendor = vendor
        self.current_device_type = device_type
        self.load_commands()

    def set_active_device_type(self, device_type):
        self.current_device_type = device_type
        self.parent.selected_device_type = device_type

        if device_type == "switch":
            self.switch_button.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    font-weight: bold;
                    border: none;
                    padding: 8px 20px;
                }
                QPushButton:hover {
                    background-color: #45a049;
                }
            """)
            self.router_button.setStyleSheet("""
                QPushButton {
                    background-color: #6c757d;
                    color: white;
                    border: none;
                    padding: 8px 20px;
                }
                QPushButton:hover {
                    background-color: #5a6268;
                }
            """)
        else:
            self.router_button.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    font-weight: bold;
                    border: none;
                    padding: 8px 20px;
                }
                QPushButton:hover {
                    background-color: #45a049;
                }
            """)
            self.switch_button.setStyleSheet("""
                QPushButton {
                    background-color: #6c757d;
                    color: white;
                    border: none;
                    padding: 8px 20px;
                }
                QPushButton:hover {
                    background-color: #5a6268;
                }
            """)

        self.load_commands()

    def load_commands(self):
        if self.current_device_type == "switch":
            self.load_switch_commands()
        elif self.current_device_type == "router":
            self.load_router_commands()

    def load_switch_commands(self):
        commands = [
            ("0001", "Configure VLANs Across Multiple Switches"),
            ("0002", "Configure Port Security on Multiple Switches"),
            ("0003", "Backup Configurations of Multiple Switches"),
            ("0004", "Update Firmware on Multiple Switches"),
            ("0005", "Configure Interfaces on Multiple Switches"),
            ("0006", "Configure SNMP on Multiple Switches"),
            ("0007", "Configure Syslog on Multiple Switches")
        ]
        self.populate_command_table(commands)

    def load_router_commands(self):
        commands = [
            ("1001", "Configure OSPF Across Multiple Routers"),
            ("1002", "Configure BGP Across Multiple Routers"),
            ("1003", "Deploy ACLs to Multiple Routers"),
            ("1004", "Backup Configurations of Multiple Routers"),
            ("1005", "Update Firmware on Multiple Routers"),
            ("1006", "Configure Interfaces on Multiple Routers"),
            ("1007", "Configure NTP on Multiple Routers")
        ]
        self.populate_command_table(commands)

    def populate_command_table(self, commands):
        self.multiple_device_table.clearContents()
        self.multiple_device_table.setRowCount(len(commands))

        for row, (code_id, description) in enumerate(commands):
            button = QPushButton(f"{code_id} - {description}")
            button.setStyleSheet("""
                QPushButton {
                    text-align: left;
                    padding: 10px;
                    font-size: 12pt;
                    background-color: #f0f0f0;
                    border: 1px solid #dcdcdc;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;
                }
            """)

            button.code_id = code_id
            button.description = description
            button.clicked.connect(lambda checked, b=button: self.handle_button_click(b))

            widget = QWidget()
            layout = QHBoxLayout(widget)
            layout.addWidget(button)
            layout.setContentsMargins(0, 0, 0, 0)

            self.multiple_device_table.setCellWidget(row, 0, widget)
            self.multiple_device_table.setRowHeight(row, 50)

    def handle_button_click(self, button):
        # Reset all buttons to default style
        for row in range(self.multiple_device_table.rowCount()):
            widget = self.multiple_device_table.cellWidget(row, 0)
            if widget:
                btn = widget.findChild(QPushButton)
                if btn:
                    btn.setStyleSheet("""
                        QPushButton {
                            text-align: left;
                            padding: 10px;
                            font-size: 12pt;
                            background-color: #f0f0f0;
                            border: 1px solid #dcdcdc;
                            border-radius: 5px;
                        }
                        QPushButton:hover {
                            background-color: #e0e0e0;
                        }
                    """)

        # Highlight the clicked button
        button.setStyleSheet("""
            QPushButton {
                text-align: left;
                padding: 10px;
                font-size: 12pt;
                background-color: #0056b3;
                color: white;
                border: 1px solid #003d7a;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #004494;
            }
        """)

        print("\n--- Selection Path ---")
        print(f"Vendor: {self.current_vendor}")
        print(f"Device Type: {self.current_device_type}")
        print(f"Configuration: {self.parent.selected_configuration}")
        print(f"Selected Code: {button.code_id} - {button.description}")
        print("----------------------\n")

        # Generate script name based on current device type
        script_name = f"scripts.multiple.{self.current_device_type}_{button.code_id}"
        try:
            script_module = importlib.import_module(script_name)
            if hasattr(script_module, "main"):
                script_module.main()
            else:
                print(f"Script {script_name} does not define a 'main' function.")
        except ModuleNotFoundError:
            print(f"Script not found: {script_name}")
            self.show_error_message(f"Script not found: {script_name}")
        except Exception as e:
            print(f"Error running script {script_name}: {e}")
            traceback.print_exc()
            self.show_error_message(f"Error running script {script_name}: {e}")

        self.parent.open_main_page()

    def show_error_message(self, message):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Critical)
        error_dialog.setWindowTitle("Error")
        error_dialog.setText(message)
        error_dialog.setStandardButtons(QMessageBox.Ok)
        error_dialog.exec_()

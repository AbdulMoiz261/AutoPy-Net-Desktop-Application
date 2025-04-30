# pages/device_status_page.py
from PyQt5.QtWidgets import (QFrame, QVBoxLayout, QTableWidget, 
                            QTableWidgetItem, QLabel, QSpacerItem, QSizePolicy)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class DeviceStatusPage(QFrame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)  # Consistent outer margins
        layout.setSpacing(20)  # Consistent spacing between widgets
        self.setLayout(layout)

        # Title with consistent styling
        title = QLabel("Device Status")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel {
                color: #343a40;
                margin-bottom: 10px;
            }
        """)
        layout.addWidget(title)

        # Add vertical spacer for consistent top margin
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed))

        # Device Status Table
        self.device_table = QTableWidget()
        self.device_table.setColumnCount(4)
        self.device_table.setHorizontalHeaderLabels([
            "Device Name", 
            "IP Address", 
            "Type", 
            "Status"
        ])
        
        # Style the table with consistent padding
        self.device_table.setStyleSheet("""
            QTableWidget {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 8px;
                padding: 10px;
            }
            QHeaderView::section {
                background-color: #007bff;
                color: white;
                padding: 12px;
                font-weight: bold;
                font-size: 12pt;
            }
            QTableWidget::item {
                padding: 10px;
            }
        """)
        
        # Configure table properties
        self.device_table.verticalHeader().setVisible(False)
        self.device_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.device_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.device_table.horizontalHeader().setStretchLastSection(True)
        
        # Set column widths with consistent spacing
        self.device_table.setColumnWidth(0, 250)  # Device Name
        self.device_table.setColumnWidth(1, 200)  # IP Address
        self.device_table.setColumnWidth(2, 150)  # Type
        
        # Add sample data with consistent row height
        self.update_device_table([
            {"name": "Core-Switch-01", "ip": "192.168.1.1", "type": "Switch", "status": "Online"},
            {"name": "Router-01", "ip": "192.168.1.2", "type": "Router", "status": "Online"},
            {"name": "Access-Switch-01", "ip": "192.168.1.3", "type": "Switch", "status": "Offline"},
            {"name": "Firewall-01", "ip": "192.168.1.4", "type": "Firewall", "status": "Online"},
        ])
        
        layout.addWidget(self.device_table)

        # Add bottom spacer for consistent layout
        layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

    def update_device_table(self, devices):
        """Update the table with device data"""
        self.device_table.setRowCount(len(devices))
        
        for row, device in enumerate(devices):
            # Set consistent row height
            self.device_table.setRowHeight(row, 40)
            
            # Create items with consistent styling
            name_item = QTableWidgetItem(device["name"])
            name_item.setFont(QFont("Arial", 11))
            
            ip_item = QTableWidgetItem(device["ip"])
            ip_item.setFont(QFont("Arial", 11))
            
            type_item = QTableWidgetItem(device["type"])
            type_item.setFont(QFont("Arial", 11))
            
            status_item = QTableWidgetItem(device["status"])
            status_item.setFont(QFont("Arial", 11, QFont.Bold))
            
            if device["status"] == "Online":
                status_item.setForeground(Qt.darkGreen)
            else:
                status_item.setForeground(Qt.red)
            
            # Center-align all items
            for item in [name_item, ip_item, type_item, status_item]:
                item.setTextAlignment(Qt.AlignCenter)
            
            self.device_table.setItem(row, 0, name_item)
            self.device_table.setItem(row, 1, ip_item)
            self.device_table.setItem(row, 2, type_item)
            self.device_table.setItem(row, 3, status_item)
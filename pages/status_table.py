# # pages/status_table.py
# from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
# from PyQt5.QtGui import QFont
# from PyQt5.QtCore import Qt

# class StatusTable(QTableWidget):
#     def __init__(self):
#         super().__init__(5, 2)
#         self.setup_ui()

#     def setup_ui(self):
#         self.setColumnWidth(0, 1100)
#         self.setColumnWidth(1, 400)
#         self.verticalHeader().setVisible(False)
#         self.horizontalHeader().setStretchLastSection(True)

#         devices = ["List of Devices", "Switch 1", "Router", "Router 2"]
#         statuses = ["Status", "🔴", "🟢", "🟠"]

#         for row, (device, status) in enumerate(zip(devices, statuses)):
#             device_item = QTableWidgetItem(device)
#             status_item = QTableWidgetItem(status)

#             device_item.setFont(QFont("Arial", 12, QFont.Bold))
#             status_item.setFont(QFont("Arial", 12, QFont.Bold))
            
#             device_item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
#             status_item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

#             self.setItem(row, 0, device_item)
#             self.setItem(row, 1, status_item)

#         self.setStyleSheet("""
#         QTableWidget {
#             background-color: #f5f5f5;
#             border: 1px solid #dcdcdc;
#             border-radius: 10px;
#             padding: 5px;
#             font-family: 'Arial';
#             font-size: 12pt;
#         }
#         """)

#         self.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
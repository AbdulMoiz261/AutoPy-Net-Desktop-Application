# log_window.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit
from PyQt5.QtCore import pyqtSignal, QObject

class LogEmitter(QObject):
    new_log = pyqtSignal(str)

class LogWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application Logs")
        self.resize(800, 400)
        
        layout = QVBoxLayout()
        self.log_display = QTextEdit()
        self.log_display.setReadOnly(True)
        self.log_display.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: #d4d4d4;
                font-family: Consolas;
                font-size: 10pt;
            }
        """)
        
        layout.addWidget(self.log_display)
        self.setLayout(layout)
        
        self.log_emitter = LogEmitter()
        self.log_emitter.new_log.connect(self.append_log)
    
    def append_log(self, message):
        self.log_display.append(message.strip())
        # Auto-scroll to bottom
        cursor = self.log_display.textCursor()
        cursor.movePosition(cursor.End)
        self.log_display.setTextCursor(cursor)
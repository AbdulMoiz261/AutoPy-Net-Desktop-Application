# main.py
from PyQt5.QtWidgets import QApplication
import sys
from datetime import datetime
from pages.main_page import AutoPynetDashboard
from pages.log_window import LogWindow, LogEmitter

class QtLogHandler:
    def __init__(self, log_emitter):
        self.log_emitter = log_emitter

    def write(self, message):
        if message.strip():  # Only emit non-empty messages
            self.log_emitter.new_log.emit(message)
    
    def flush(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Create main window
    dashboard = AutoPynetDashboard()
    
    # Create log window (but don't show yet)
    log_window = LogWindow()
    dashboard.log_window = log_window  # Make it accessible
    
    # Setup logging
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    
    qt_handler = QtLogHandler(log_window.log_emitter)
    sys.stdout = qt_handler
    sys.stderr = qt_handler
    
    print(f"\nSession started at {datetime.now()}\n")
    
    dashboard.showMaximized()

    try:
        sys.exit(app.exec_())
    except Exception as e:
        print(f"CRASHED: {e}", file=sys.stderr)
        raise
    finally:
        # Restore original stdout/stderr
        sys.stdout = original_stdout
        sys.stderr = original_stderr
        print(f"\nSession ended at {datetime.now()}\n")


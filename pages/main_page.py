# AutoPynetDashboard.py
from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QFrame,
                             QStackedWidget, QLabel, QPushButton)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QSize
from widgets.sidebar import Sidebar
from widgets.search_bar import SearchBar
from pages.welcome_section import WelcomeSection
from pages.device_status_page import DeviceStatusPage
from pages.files_page import FilesPage
from pages.log_window import LogWindow  # Import the LogWindow class

class AutoPynetDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.selected_vendor = None
        self.selected_device_type = None
        self.selected_configuration = None

        self.setWindowTitle("Autopynet Dashboard")
        self.setGeometry(100, 100, 600, 600)  # Fix resolution to 600x600

        # Initialize log window (but don't show yet)
        self.log_window = LogWindow()

        # Main Horizontal Layout
        main_layout = QHBoxLayout(self)

        # Sidebar (Left Navigation Bar)
        self.sidebar = Sidebar(self)
        main_layout.addWidget(self.sidebar)

        # Content Area with Stacked Pages
        self.pages = QStackedWidget()
        self.main_page = self.create_main_page()

        # Import other pages here to avoid circular imports
        from pages.vendor_page import VendorPage
        from pages.device_type_page import DeviceTypePage
        from pages.config_page import ConfigPage
        from pages.single_device import SingleDevicePage
        from pages.multiple_device import MultipleDevicePage

        self.choose_vendor_page = VendorPage(self)
        self.device_type_page = DeviceTypePage(self)
        self.device_selection_page = ConfigPage(self)
        self.single_device_page = SingleDevicePage(self)
        self.multiple_device_page = MultipleDevicePage(self)
        self.device_status_page = DeviceStatusPage(self)
        self.files_page = FilesPage(self)

        # Add all pages to stacked widget
        self.pages.addWidget(self.main_page)
        self.pages.addWidget(self.choose_vendor_page)
        self.pages.addWidget(self.device_type_page)
        self.pages.addWidget(self.device_selection_page)
        self.pages.addWidget(self.single_device_page)
        self.pages.addWidget(self.multiple_device_page)
        self.pages.addWidget(self.device_status_page)
        self.pages.addWidget(self.files_page)

        main_layout.addWidget(self.pages)
        self.setLayout(main_layout)

    # Add this new method to handle log window toggling
    def open_log_window(self):
        """Toggle visibility of the log window."""
        if self.log_window.isVisible():
            self.log_window.hide()
        else:
            self.log_window.show()

    # Navigation methods (keep all existing ones)
    def open_main_page(self):
        """Switch to the main page."""
        self.pages.setCurrentIndex(0)

    def open_choose_vendor_page(self):
        """Switch to the Choose Vendor page."""
        self.pages.setCurrentIndex(1)

    def open_my_files_page(self):
        """Switch to the My Files page."""
        self.pages.setCurrentWidget(self.files_page)

    def open_status_page(self):
        """Switch to the Status page."""
        self.pages.setCurrentWidget(self.device_status_page)

    def open_device_type_page(self):
        """Navigate to the device type page."""
        self.device_type_page.set_vendor(self.selected_vendor)
        self.pages.setCurrentIndex(2)

    def open_device_selection_page(self):
        """Navigate to the device selection page."""
        self.device_selection_page.set_device_type(self.selected_device_type)
        self.pages.setCurrentIndex(3)

    def open_single_device_page(self):
        """Navigate to the single device page."""
        self.single_device_page.set_selected_options(self.selected_vendor, self.selected_device_type)
        self.pages.setCurrentIndex(4)

    def open_multiple_device_page(self):
        """Navigate to the multiple device page."""
        self.multiple_device_page.set_selected_options(self.selected_vendor, self.selected_device_type)
        self.pages.setCurrentIndex(5)

    def open_all_files_page(self):
        """Open the full file list page when 'See All' is clicked."""
        self.pages.setCurrentWidget(self.files_page)

    def open_file_upload_dialog(self):
        """Open file upload dialog to choose a file to upload."""
        self.files_page.open_file_upload_dialog()

    def create_main_page(self):
        """Main page with welcome and table sections."""
        content_layout = QVBoxLayout()

        # 1. Search Bar (topmost element)
        search_bar = SearchBar()
        content_layout.addWidget(search_bar)

        # 2. Welcome to AutoPyNet heading
        heading_frame = QFrame()
        heading_layout = QVBoxLayout(heading_frame)

        welcome_label = QLabel("Welcome to")
        welcome_label.setFont(QFont("Arial", 25, QFont.Bold))
        welcome_label.setAlignment(Qt.AlignLeft)
        welcome_label.setStyleSheet("""
            QLabel {
                color: #333;
                margin-top: 20px;
                margin-bottom: 0;
            }
        """)

        autopynet_label = QLabel("AutoPyNet")
        autopynet_label.setFont(QFont("Arial", 40, QFont.Bold))
        autopynet_label.setAlignment(Qt.AlignLeft)
        autopynet_label.setStyleSheet("""
            QLabel {
                color: #007bff;
                margin-top: 0px;
                margin-bottom: 15px;
            }
        """)

        heading_layout.addWidget(welcome_label)
        heading_layout.addWidget(autopynet_label)
        content_layout.addWidget(heading_frame)

        # 3. Wrapper section with the rest of the content
        wrapper = self.create_wrapper_section()
        content_layout.addWidget(wrapper)

        content_frame = QFrame()
        content_frame.setLayout(content_layout)
        return content_frame

    def create_wrapper_section(self):
        """Creates a wrapper around welcome section and status table with a background."""
        wrapper_frame = QFrame()
        wrapper_frame.setStyleSheet("""
            QFrame {
                background-color:rgb(255, 255, 255);
                border-radius: 10px;
                padding: 20px;
                box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.1);
            }
        """)

        wrapper_layout = QVBoxLayout(wrapper_frame)

        welcome_section = WelcomeSection(self)
        wrapper_layout.addWidget(welcome_section)

        return wrapper_frame
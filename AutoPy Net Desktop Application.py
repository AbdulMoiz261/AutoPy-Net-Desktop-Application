from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QLineEdit, QListWidget, QTableWidget, QTableWidgetItem, QFrame, QStackedWidget
)
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys


class AutoPynetDashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Autopynet Dashboard")
        self.setGeometry(100, 100, 1000, 600)

        # Main Horizontal Layout
        main_layout = QHBoxLayout(self)

        # Sidebar (Left Navigation Bar)
        sidebar = self.create_sidebar()
        main_layout.addWidget(sidebar)

        # Content Area with Stacked Pages
        self.pages = QStackedWidget()
        self.main_page = self.create_main_page()
        self.choose_vendor_page = self.create_choose_vendor_page()
        self.device_type_page = self.create_device_type_page()
        # juniper or cisco
        self.device_selection_page = self.create_device_selection_page() 
        self.single_device_page = self.create_single_device_page()
        self.multiple_device_page = self.create_multiple_device_page()
        self.pages.addWidget(self.main_page) 
        self.pages.addWidget(self.choose_vendor_page)  
        self.pages.addWidget(self.device_type_page) 
        self.pages.addWidget(self.device_selection_page)  
        self.pages.addWidget(self.single_device_page)  
        self.pages.addWidget(self.multiple_device_page) 
        

        main_layout.addWidget(self.pages)
        self.setLayout(main_layout)

    def create_sidebar(self):
        """Creates the sidebar with navigation buttons and a modern design."""
        # Create the sidebar frame
        sidebar_frame = QFrame()
        sidebar_frame.setStyleSheet("""
            QFrame {
                background-color: #ffffff;    /* White background */
                border-right: 2px solid #dcdcdc;  /* Subtle light gray border */
            }
        """)
        sidebar_frame.setFixedWidth(250)

        # Sidebar layout
        sidebar_layout = QVBoxLayout()

        # Logo
        logo_label = QLabel("AUTOPYNET")
        logo_label.setFont(QFont("Arial", 16, QFont.Bold))
        logo_label.setAlignment(Qt.AlignCenter)
        logo_label.setStyleSheet("""
            QLabel {
                color: #343a40;    /* Dark gray text */
                margin-top: 20px;  /* Add space above the logo */
                margin-bottom: 20px;  /* Add space below the logo */
            }
        """)
        sidebar_layout.addWidget(logo_label)

        # Divider below the logo
        divider = QFrame()
        divider.setFrameShape(QFrame.HLine)
        divider.setFrameShadow(QFrame.Sunken)
        divider.setStyleSheet("color: #dcdcdc;")  # Subtle divider color
        sidebar_layout.addWidget(divider)

        # Navigation Buttons
        buttons = {
            "Home": self.open_main_page,  # Function for Home page
            "Vendor": self.open_choose_vendor_page,  # Function for Vendor page
            "My Files": self.open_my_files_page,  # Placeholder function for My Files
            "Status": self.open_status_page  # Placeholder function for Status
        }

        for btn_text, btn_function in buttons.items():
            button = QPushButton(btn_text)
            button.setFixedHeight(50)
            button.setStyleSheet("""
                QPushButton {
                    text-align: left;
                    padding-left: 20px;
                    color: #343a40;           /* Dark gray text */
                    background-color: #ffffff;  /* Match sidebar background */
                    font-size: 14pt;
                    font-family: Arial;
                    border: none;
                }
                QPushButton:hover {
                    background-color: #e9ecef;  /* Light gray on hover */
                    border-left: 5px solid #007bff;  /* Blue indicator on hover */
                }
                QPushButton:pressed {
                    background-color: #007bff;  /* Blue background when pressed */
                    color: #ffffff;             /* White text when pressed */
                }
            """)
            button.clicked.connect(btn_function)  # Connect button to function
            sidebar_layout.addWidget(button)

        # Stretch to push items to the top
        sidebar_layout.addStretch()

        # Footer Section
        footer_label = QLabel("© 2024 AutoPyNet")
        footer_label.setFont(QFont("Arial", 10))
        footer_label.setAlignment(Qt.AlignCenter)
        footer_label.setStyleSheet("""
            QLabel {
                color: #6c757d;  /* Medium gray text */
                margin-bottom: 10px;
            }
        """)
        sidebar_layout.addWidget(footer_label)

        sidebar_frame.setLayout(sidebar_layout)
        return sidebar_frame
    
    def open_main_page(self):
        """Switch to the main page."""
        self.central_widget.setCurrentWidget(self.main_page)  # Replace with the reference to your main page widget

    def open_choose_vendor_page(self):
        """Switch to the Choose Vendor page."""
        self.central_widget.setCurrentWidget(self.choose_vendor_page)  # Replace with the reference to your choose vendor page widget

    def open_my_files_page(self):
        """Switch to the My Files page."""
        self.central_widget.setCurrentWidget(self.my_files_page)  # Replace with the reference to your My Files page widget

    def open_status_page(self):
        """Switch to the Status page."""
        self.central_widget.setCurrentWidget(self.status_page)  # Replace with the reference to your Status page widget
        

    def create_main_page(self):
        """Main page with welcome and table sections."""
        content_layout = QVBoxLayout()
        

        # Search Bar
        search_bar = self.create_search_bar()
        content_layout.addWidget(search_bar)
        
        wrapper = self.create_wrapper_section()
        content_layout.addWidget(wrapper)

        # Add Content Layout to Frame
        content_frame = QFrame()
        content_frame.setLayout(content_layout)
        return content_frame

    def create_search_bar(self):
        """Creates the search bar at the top with its own background."""
        search_frame = QFrame()
        search_frame.setStyleSheet("""
            QFrame {
                background-color: #007bff;
                border: 1px solid #dcdcdc;
                border-radius: 10px;
                margin: 10px;
                padding: 5px;
            }
        """)
        search_layout = QHBoxLayout(search_frame)

        search_input = QLineEdit()
        search_input.setPlaceholderText("Search...")
        search_input.setFixedHeight(35)
        search_input.setFixedWidth(500)
        search_input.setAlignment(Qt.AlignLeft)
        search_input.setStyleSheet(""" 
            QLineEdit {
                font-size: 10pt;
                padding: 0 10px;
                border: 1px solid #ccc;
                border-radius: 15px;
                background-color: #ffffff;
                color: #333;
            }
            QLineEdit:focus {
                border: 1px solid #007bff;
                box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
            }
        """)
        search_layout.addWidget(search_input, alignment=Qt.AlignLeft)

        return search_frame



    def create_welcome_section(self):
        """Creates the welcome message and file section with separate backgrounds."""
        # Create a container frame for the entire section
        welcome_frame = QFrame()
        welcome_frame.setStyleSheet("""
            QFrame {
                background-color: transparent; /* Optional background for the frame itself */
            }
        """)
        welcome_layout = QHBoxLayout(welcome_frame)

        # Network Device Section (Container for label and button)
        device_section_frame = QFrame()
        device_section_frame.setStyleSheet("""
            QFrame {
                background-color: rgb(234, 235, 253);
                border: none; /* Removed the border */
                border-radius: 10px;
                padding: 10px;
                box-shadow: 3px 3px 8px rgba(0, 0, 0, 0.2);
            }
        """)
        device_section_layout = QVBoxLayout(device_section_frame)

        # Split the label into two lines
        network_label = QLabel("Network Device to\nconfigure?")
        network_label.setFont(QFont("Arial", 15, QFont.Bold))
        network_label.setAlignment(Qt.AlignLeft)  # Left-align the label
        network_label.setStyleSheet("""
            QLabel {
                border: none;  /* Ensure no border on label */
            }
        """)

        # "Choose Vendor" button
        choose_button = QPushButton("Choose Vendor")
        choose_button.setStyleSheet(""" 
            QPushButton {
                background-color: #007bff;
                color: white;
                border-radius: 20px; /* More rounded button */
                padding: 15px 20px; /* Increased padding for height */
                font-size: 11pt;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        choose_button.setFixedWidth(250)
        choose_button.clicked.connect(self.open_choose_vendor_page)

        # Add label and button to the Network Device Section
        device_section_layout.addWidget(network_label)
        device_section_layout.addWidget(choose_button)
        device_section_layout.setAlignment(Qt.AlignCenter)  # Center button beneath label

        # My Files Section
        files_section_frame = QFrame()
        files_section_frame.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;
                border: 1px solid #dcdcdc;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        files_section_layout = QVBoxLayout(files_section_frame)

        files_label = QLabel("My Files")
        files_label.setFont(QFont("Arial", 13, QFont.Bold))

        # Create a list of file names to display (replace this with dynamic file list)
        file_names = [
            "File.txt", "File1.txt", "File2.txt", "File3.txt", "File4.txt", "File5.txt"
        ]
        
        # Create QListWidget to display files
        file_list = QListWidget()
        file_list.addItems(file_names)  # Add file names to the list

        # Adjust file container size
        file_list.setFixedHeight(150)  # Reduced height
        file_list.setFixedWidth(1150)   # Increased width

        # Create a horizontal layout for "See All" and "Upload File" buttons
        button_layout = QHBoxLayout()

        # "See All" button
        see_all_button = QPushButton("See All")
        see_all_button.setStyleSheet("""
            QPushButton {
                background-color: #007bff;
                color: white;
                border-radius: 20px; /* Rounded button */
                padding: 15px 20px; /* Increased padding for height */
                font-size: 11pt;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)
        see_all_button.setFixedWidth(150)  # Adjust button width to match the "Upload File" button
        see_all_button.clicked.connect(self.open_all_files_page)

        # "Upload File" button
        upload_button = QPushButton("Upload File")
        upload_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                border-radius: 20px; /* Rounded button */
                padding: 15px 20px; /* Increased padding for height */
                font-size: 11pt;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        upload_button.setFixedWidth(150)  # Same width as "See All" button
        upload_button.clicked.connect(self.open_file_upload_dialog)

        # Add both buttons to the button layout
        button_layout.addWidget(see_all_button)
        button_layout.addWidget(upload_button)
        button_layout.setAlignment(Qt.AlignRight)  # Align the buttons to the right

        # Add the button layout to the files section layout
        files_section_layout.addWidget(files_label)
        files_section_layout.addWidget(file_list)
        files_section_layout.addLayout(button_layout)  # Add the layout with buttons

        # Add both sections to the welcome layout
        welcome_layout.addWidget(device_section_frame)  # Add Network Device Section with its background
        welcome_layout.addWidget(files_section_frame)  # Add My Files Section with its background

        return welcome_frame  # Return the frame instead of the layout

    def open_choose_vendor_page(self):
        """Method to handle 'Choose Vendor' button click."""
        # Implement the logic to open the vendor selection page here
        pass

    def open_all_files_page(self):
        """Open the full file list page when 'See All' is clicked."""
        all_files_page_window = QDialog(self)  # You can use QDialog to open a new window
        all_files_page_window.setWindowTitle("All Files")

        all_files_page_layout = QVBoxLayout(all_files_page_window)

        all_files_label = QLabel("All Files")
        all_files_label.setFont(QFont("Arial", 14, QFont.Bold))

        # Create a list widget to display all files
        all_files_list = QListWidget()
        all_files_list.addItem("File.txt")  # You can populate this list dynamically with all available files

        # Add some placeholder content for each file in the list
        for i in range(5):  # Example loop, assuming we have 5 files to show
            all_files_list.addItem(f"File {i+1}.txt")

        # When a file is selected from the list, show its content (optional)
        all_files_list.itemClicked.connect(self.open_file_content)

        all_files_page_layout.addWidget(all_files_label)
        all_files_page_layout.addWidget(all_files_list)

        # Show the all files details page
        all_files_page_window.exec_()  # Open the dialog window

    def open_file_content(self, item):
        """Open the content of the selected file."""
        file_content_window = QDialog(self)
        file_content_window.setWindowTitle(f"Content of {item.text()}")

        file_content_layout = QVBoxLayout(file_content_window)

        file_content_label = QLabel(f"Content of {item.text()}:")
        file_content_label.setFont(QFont("Arial", 14, QFont.Bold))

        # Placeholder content for file
        file_content = QLabel("This is the content of the file:\n\n[File content goes here...]")
        file_content.setFont(QFont("Arial", 12))

        file_content_layout.addWidget(file_content_label)
        file_content_layout.addWidget(file_content)

        file_content_window.exec_()  # Show the content of the selected file in a new dialog

    def open_file_upload_dialog(self):
        """Open file upload dialog to choose a file to upload."""
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Text Files (*.txt)")
        file_dialog.setViewMode(QFileDialog.List)

        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()
            # Handle file upload logic here (e.g., uploading to server or saving locally)
            print(f"Selected files: {file_paths}")
    
    def create_welcome_text(self):
        """Creates a welcome text with 'Welcome to' and 'AutoPyNet' in a larger size, blue color, and shine effect."""

        # Create a container for the text (QLabel)
        welcome_layout = QVBoxLayout()

        welcome_layout.setSpacing(0)  # Remove the default vertical spacing between widgets

        # Create the first label for 'Welcome to'
        welcome_label = QLabel("Welcome to")
        welcome_label.setFont(QFont("Arial", 15, QFont.Bold))  # Increased font size to 15pt
        welcome_label.setAlignment(Qt.AlignLeft)
        welcome_label.setStyleSheet("""
            QLabel {
                font-size: 20pt;  /* Increased font size */
                font-weight: bold;
                color: #333;  /* Dark text color for the first line */
                text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);  /* Subtle shadow for depth */
            }
        """)

        # Create the second label for 'AutoPyNet' with larger font size, blue color, and shine effect
        autopynet_label = QLabel("AutoPyNet")
        autopynet_label.setFont(QFont("Arial", 20, QFont.Bold))  # Increased font size to 20pt
        autopynet_label.setAlignment(Qt.AlignLeft)
        autopynet_label.setStyleSheet("""
            QLabel {
                font-size: 30pt;  /* Increased font size */
                font-weight: bold;
                color: #007bff;  /* Blue color */
                text-shadow: 3px 3px 8px rgba(0, 123, 255, 0.6);  /* Enhanced shine effect with stronger shadow */
                letter-spacing: 1px;  /* Slight letter-spacing for better readability */
            }
        """)

        # Adjust margins to remove vertical space between labels
        welcome_label.setContentsMargins(0, 0, 0, 0)  # Remove all margins from "Welcome to"
        autopynet_label.setContentsMargins(0, 0, 0, 0)  # Remove all margins from "AutoPyNet"

        # Add both labels to the layout
        welcome_layout.addWidget(welcome_label)
        welcome_layout.addWidget(autopynet_label)

        # Return the layout containing the labels
        return welcome_layout




    def create_wrapper_section(self):
        """Creates a wrapper around welcome section and status table with a background."""

        # Create the main wrapper frame
        wrapper_frame = QFrame()
        wrapper_frame.setStyleSheet("""
            QFrame {
                background-color:rgb(255, 255, 255);  /* Light gray background */
                border-radius: 10px;        /* Rounded corners for the wrapper */
                padding: 20px;              /* Add padding inside the wrapper */
                box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.1);  /* Optional shadow effect */
            }
        """)

        # Create a vertical layout for the wrapper
        wrapper_layout = QVBoxLayout(wrapper_frame)

        # Call the existing methods to create the welcome section and status table
        welcome_section = self.create_welcome_section()
        status_table = self.create_status_table()
        text = self.create_welcome_text()

        # Add both sections to the wrapper layout
        wrapper_layout.addLayout(text)
        wrapper_layout.addWidget(welcome_section)
        wrapper_layout.addWidget(status_table)

        # Return the wrapper frame
        return wrapper_frame

    # def create_status_table(self):
    #     """Creates the status bar table with visible and properly styled headings."""
    #     table = QTableWidget(5, 2)  # 3 rows, 2 columns
    #     # table.setHorizontalHeaderLabels(["List of Devices", "Status"])  # Correct headings
    #     table.setColumnWidth(0, 1100)  # Adjusted width for first column
    #     table.setColumnWidth(1, 400)   # Adjusted width for status column
    #     table.verticalHeader().setVisible(False)
    #     table.horizontalHeader().setStretchLastSection(True)  # Stretch the last column

    #     # Data for the table
    #     devices = ["List of Devices","Switch 1", "Router", "Router 2"]
    #     statuses = ["Status","🔴", "🟢", "🟠"]

    #     for row, (device, status) in enumerate(zip(devices, statuses)):
    #         device_item = QTableWidgetItem(device)
    #         status_item = QTableWidgetItem(status)

    #         # Make text in the cells bold for better readability
    #         device_item.setFont(QFont("Arial", 12, QFont.Bold))
    #         status_item.setFont(QFont("Arial", 12, QFont.Bold))
            
    #         # Align text in cells for a clean layout
    #         device_item.setTextAlignment(Qt.AlignVCenter | Qt.AlignLeft)
    #         status_item.setTextAlignment(Qt.AlignCenter)

    #         table.setItem(row, 0, device_item)
    #         table.setItem(row, 1, status_item)

    #     # Apply Styles
    #     table.setStyleSheet("""
    #     QTableWidget {
    #         background-color: #f5f5f5;     /* Light gray background */
    #         border: 1px solid #dcdcdc;     /* Subtle border */
    #         border-radius: 10px;           /* Rounded corners */
    #         padding: 5px;
    #         font-family: 'Arial';          /* Use professional font */
    #         font-size: 12pt;               /* Slightly larger font */
    #     }

    #     QHeaderView::section {
    #         background-color: #007bff;     /* Blue background for headers */
    #         color: white;                  /* White text color for headers */
    #         font-weight: bold;             /* Bold text for headers */
    #         font-size: 12pt;               /* Slightly larger font for headers */
    #         padding: 5px;                  /* Padding for spacing */
    #         border: none;                  /* No borders around header cells */
    #         text-align: center;            /* Center-align header text */
    #     }
    #     """)

    #     return table
    
    def create_status_table(self):
        """Creates the status bar table with visible and properly styled headings."""
        table = QTableWidget(5, 2)  # 5 rows, 2 columns
        table.setColumnWidth(0, 1100)  # Adjusted width for the first column
        table.setColumnWidth(1, 400)   # Adjusted width for the status column
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setStretchLastSection(True)  # Stretch the last column

        # Data for the table
        devices = ["List of Devices", "Switch 1", "Router", "Router 2"]
        statuses = ["Status", "🔴", "🟢", "🟠"]

        for row, (device, status) in enumerate(zip(devices, statuses)):
            device_item = QTableWidgetItem(device)
            status_item = QTableWidgetItem(status)

            # Make text in the cells bold for better readability
            device_item.setFont(QFont("Arial", 12, QFont.Bold))
            status_item.setFont(QFont("Arial", 12, QFont.Bold))
            
            # Align text in cells for a clean layout (center alignment)
            device_item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            status_item.setTextAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

            table.setItem(row, 0, device_item)
            table.setItem(row, 1, status_item)

        # Apply Styles
        table.setStyleSheet("""
        QTableWidget {
            background-color: #f5f5f5;     /* Light gray background */
            border: 1px solid #dcdcdc;     /* Subtle border */
            border-radius: 10px;           /* Rounded corners */
            padding: 5px;
            font-family: 'Arial';          /* Use professional font */
            font-size: 12pt;               /* Slightly larger font */
        }

        # QHeaderView::section {
        #     background-color: #007bff;     /* Blue background for headers */
        #     color: white;                  /* White text color for headers */
        #     font-weight: bold;             /* Bold text for headers */
        #     font-size: 12pt;               /* Slightly larger font for headers */
        #     padding: 5px;                  /* Padding for spacing */
        #     border: none;                  /* No borders around header cells */
        #     text-align: center;            /* Center-align header text */
        # }
        """)

        # Align the header text to center
        table.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        return table


    def create_center_text(self, text):
        """Creates a centered text label with a little space from the top."""
        # Create a label with the provided text
        label = QLabel(text)
        label.setFont(QFont("Arial", 16, QFont.Bold))  # Set font size and style
        label.setAlignment(Qt.AlignCenter)  # Horizontally center the text
        
        # Create a layout to position the text
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)  # Align the content to the top of the layout
        layout.addWidget(label)
    
        # Set a top margin to position it below the top of the screen
        layout.setContentsMargins(0, 30, 0, 0)  # Adjust the 30 value to position the text lower
    
        # Create a frame or return layout
        frame = QFrame()
        frame.setLayout(layout)
        return frame

    def create_two_buttons(self, button_text_1, button_text_2):
        """Creates two buttons with text passed as parameters."""
        button_container = QHBoxLayout()  # Horizontal layout for buttons
        button_container.setAlignment(Qt.AlignCenter)  # Center the container in the middle

        # Create the first button
        button_1 = QPushButton(button_text_1)
        button_1.setFixedHeight(150)
        button_1.setFixedWidth(250)  # Set the width of the button
        button_1.setStyleSheet("""
            QPushButton {
                font-size: 14pt;
                background-color: #007bff;
                color: white;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)

        # Create the second button
        button_2 = QPushButton(button_text_2)
        button_2.setFixedHeight(150)
        button_2.setFixedWidth(250)  # Set the width of the button
        button_2.setStyleSheet("""
            QPushButton {
                font-size: 14pt;
                background-color: #007bff;
                color: white;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """)

        # Add buttons to the layout
        button_container.addWidget(button_1, alignment=Qt.AlignLeft)
        button_container.addWidget(button_2, alignment=Qt.AlignRight)
        button_container.setAlignment(Qt.AlignTop)

        return button_container
    

    def create_choose_vendor_page(self):
        """Creates the 'Choose Vendor' page matching the provided layout."""
        vendor_layout = QVBoxLayout()
        vendor_layout.setSpacing(20)  # Add spacing between elements

        # Add stretch above the title to push it to the center vertically
        vendor_layout.addStretch()

        # Title Label (No borders, centered)
        center_text = self.create_center_text("Select Vendor")
        center_text.setStyleSheet("""
            border: none;
            font-size: 24pt;
            font-weight: bold;
            color: #343a40;  /* Dark text for better readability */
            font-family: 'Arial', sans-serif;
        """)  # Remove border and style text
        vendor_layout.addWidget(center_text, alignment=Qt.AlignCenter)

        # Button Container (For centering buttons)
        button_container = QHBoxLayout()
        button_container.setSpacing(50)  # Add spacing between buttons
        button_container.setAlignment(Qt.AlignCenter)  # Center buttons horizontally

        # Cisco Button
        cisco_button = QPushButton("Cisco")
        cisco_button.setFixedSize(250, 150)  # Match the button size
        cisco_button.setStyleSheet("""
            QPushButton {
                font-size: 16pt;
                font-family: 'Arial', sans-serif;
                padding: 20px;
                border: 2px solid #007bff;  /* Blue border for professional look */
                border-radius: 12px;
                background-color: white;
                color: #007bff;  /* Matching text color to border */
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
        cisco_button.clicked.connect(lambda: self.open_device_type_page("Cisco"))

        # Juniper Button
        juniper_button = QPushButton("Juniper")
        juniper_button.setFixedSize(250, 150)  # Match the button size
        juniper_button.setStyleSheet("""
            QPushButton {
                font-size: 16pt;
                font-family: 'Arial', sans-serif;
                padding: 20px;
                border: 2px solid #28a745;  /* Green border for professional look */
                border-radius: 12px;
                background-color: white;
                color: #28a745;  /* Matching text color to border */
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
        juniper_button.clicked.connect(lambda: self.open_device_type_page("Juniper"))

        # Add buttons to the container
        button_container.addWidget(cisco_button)
        button_container.addWidget(juniper_button)

        # Add the button container to the vendor layout
        vendor_layout.addLayout(button_container)

        # Add stretch below the button container to push everything to the center
        vendor_layout.addStretch()

        # Back Button Layout (Position it at the bottom-left)
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
        back_button.clicked.connect(self.open_main_page)  # Connect to your back navigation logic

        back_button_layout = QHBoxLayout()
        back_button_layout.addWidget(back_button, alignment=Qt.AlignLeft)
        back_button_layout.setContentsMargins(20, 20, 20, 20)

        # Add the back button layout to the vendor layout
        vendor_layout.addLayout(back_button_layout)

        # Final vendor frame
        vendor_frame = QFrame()
        vendor_frame.setLayout(vendor_layout)
        vendor_frame.setFixedSize(1680, 970)  # Set specific width and height for the frame
        vendor_frame.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;  /* Light background color */
                border-radius: 20px;  /* Rounded corners */
                border: 2px solid #dcdcdc;  /* Light border */
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);  /* Subtle shadow for depth */
            }
        """)
        return vendor_frame

      
    def create_device_type_page(self):
        """Creates a device type selection page with buttons centered both vertically and horizontally."""
        page_layout = QVBoxLayout()
        page_layout.setSpacing(30)  # Add more spacing between elements for a clean look

        # Add stretch above the title to push it to the center vertically
        page_layout.addStretch()

        # Title Label
        title_label = QLabel("Select Type of Device")
        title_label.setFont(QFont("Arial", 24, QFont.Bold))  # Set font to Arial, size 24, bold
        title_label.setAlignment(Qt.AlignCenter)  # Center-align the text
        title_label.setStyleSheet("""
            QLabel {
                border: none;
                background: transparent;
                color: #343a40;  /* Dark text color for better readability */
                font-family: 'Arial', sans-serif;
            }
        """)
        page_layout.addWidget(title_label, alignment=Qt.AlignCenter)

        # Device Buttons (Switch and Router)
        button_container = QHBoxLayout()
        button_container.setSpacing(50)  # Add spacious gaps between buttons
        button_container.setAlignment(Qt.AlignCenter)  # Center buttons horizontally

        # Switch Button
        switch_button = QPushButton("Switch")
        switch_button.setFixedSize(250, 150)  # Set a consistent size for the button
        switch_button.setStyleSheet("""
            QPushButton {
                font-size: 16pt;
                font-family: 'Arial', sans-serif;
                padding: 20px;
                border: 2px solid #007bff;  /* Blue border */
                border-radius: 12px;
                background-color: white;
                color: #007bff;  /* Blue text */
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
        switch_button.clicked.connect(self.open_device_selection_page)

        # Router Button
        router_button = QPushButton("Router")
        router_button.setFixedSize(250, 150)  # Consistent button size
        router_button.setStyleSheet("""
            QPushButton {
                font-size: 16pt;
                font-family: 'Arial', sans-serif;
                padding: 20px;
                border: 2px solid #28a745;  /* Green border */
                border-radius: 12px;
                background-color: white;
                color: #28a745;  /* Green text */
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
        router_button.clicked.connect(self.open_device_selection_page)

        # Add buttons to the container
        button_container.addWidget(switch_button)
        button_container.addWidget(router_button)

        # Add the button container to the main layout
        page_layout.addLayout(button_container)

        # Add stretch below the button container to push everything to the center
        page_layout.addStretch()

        # Back Button (Bottom-Left position)
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
        back_button.clicked.connect(self.open_choose_vendor_page)  # Connect to navigation logic

        # Back Button Layout to position it at the bottom-left
        back_button_layout = QHBoxLayout()
        back_button_layout.addWidget(back_button, alignment=Qt.AlignLeft)
        back_button_layout.addStretch()  # Push the button to the left
        back_button_layout.setContentsMargins(20, 20, 20, 20)

        # Add Back button layout to the main page layout
        page_layout.addLayout(back_button_layout)

        # Final device type frame
        device_type_frame = QFrame()
        device_type_frame.setLayout(page_layout)
        device_type_frame.setFixedSize(1680, 970)  # Set specific width and height for the frame
        device_type_frame.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;  /* Light background color */
                border-radius: 20px;  /* Rounded corners for a soft look */
                border: 2px solid #dcdcdc;  /* Light border for neatness */
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);  /* Add subtle shadow */
            }
        """)
        return device_type_frame

   
    def create_device_selection_page(self):
        """Creates a device selection page with consistent button styling like the 'Choose Vendor' page."""
        # Main layout
        page_layout = QVBoxLayout()
        page_layout.setSpacing(20)  # Add spacing between elements

        # Add stretch above the title to push it to the center vertically
        page_layout.addStretch()

        # Title Label (No borders, centered)
        title_label = QLabel("Select Device Configuration")
        title_label.setFont(QFont("Arial", 20, QFont.Bold))  # Set font, size, and weight
        title_label.setAlignment(Qt.AlignCenter)  # Center-align the text
        title_label.setStyleSheet("""
            QLabel {
                border: none;  /* Ensure no borders are applied */
                background: transparent;  /* Remove any background color */
                font-family: 'Arial', sans-serif;
                font-size: 20pt;
                font-weight: bold;
                color: #343a40;  /* Dark text for readability */
            }
        """)
        page_layout.addWidget(title_label, alignment=Qt.AlignCenter)

        # Button Container (For centering buttons)
        button_container = QHBoxLayout()
        button_container.setSpacing(50)  # Add spacing between buttons
        button_container.setAlignment(Qt.AlignCenter)  # Center buttons horizontally

        # Single Device Button
        single_device_button = QPushButton("Single Device")
        single_device_button.setFixedSize(250, 150)
        single_device_button.setStyleSheet("""
            QPushButton {
                font-size: 16pt;
                font-family: 'Arial', sans-serif;
                padding: 20px;
                border: 2px solid #007bff;  /* Blue border for professional look */
                border-radius: 12px;
                background-color: white;
                color: #007bff;  /* Matching text color to border */
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
        single_device_button.clicked.connect(self.open_single_device_page)

        # Multiple Device Button
        multiple_device_button = QPushButton("Multiple Devices")
        multiple_device_button.setFixedSize(250, 150)
        multiple_device_button.setStyleSheet("""
            QPushButton {
                font-size: 16pt;
                font-family: 'Arial', sans-serif;
                padding: 20px;
                border: 2px solid #28a745;  /* Green border for professional look */
                border-radius: 12px;
                background-color: white;
                color: #28a745;  /* Matching text color to border */
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
        multiple_device_button.clicked.connect(self.open_multiple_device_page)

        # Add buttons to the container
        button_container.addWidget(single_device_button)
        button_container.addWidget(multiple_device_button)

        # Add button container to the main layout
        page_layout.addLayout(button_container)

        # Add stretch below the button container to push everything to the center
        page_layout.addStretch()

        # Back Button Layout (Positioned at the bottom-left)
        back_button_layout = QHBoxLayout()
        back_button = QPushButton("Back")
        back_button.setFixedSize(100, 40)
        back_button.setStyleSheet("""
            QPushButton {
                font-size: 12pt;
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
        back_button.clicked.connect(self.open_device_type_page)
        back_button_layout.addWidget(back_button)
        back_button_layout.addStretch()  # Push the button to the left
        back_button_layout.setContentsMargins(10, 10, 10, 10)

        # Add the back button layout to the main page layout
        page_layout.addLayout(back_button_layout)

        # Final Device Selection Frame (Overall container for the page)
        device_selection_frame = QFrame()
        device_selection_frame.setLayout(page_layout)
        device_selection_frame.setFixedSize(1680, 970)  # Set fixed width and height for the frame
        device_selection_frame.setStyleSheet("""
            QFrame {
                background-color: #f8f9fa;  /* Light background color */
                border-radius: 20px;
                border: none;  /* No border */
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);  /* Soft shadow effect */
            }
        """)
        return device_selection_frame


    def create_single_device_page(self):
        """Creates the single device page with a table."""
        content_frame = QFrame()
        content_layout = QVBoxLayout()

        # Container Frame for Title, Table, and Back Button
        device_selection_frame = QFrame()
        container_layout = QVBoxLayout()
        device_selection_frame.setLayout(container_layout)
        device_selection_frame.setFixedSize(1680, 970)
        device_selection_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 20px;  /* Rounded corners */
                border: 2px solid #dcdcdc;  /* Light border */
            }
        """)

        # Title
        title_label = QLabel("Single Device")
        title_label.setFont(QFont("Arial", 18, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)  # Center the title
        title_label.setStyleSheet("margin: 20px 0; font-weight: bold;")
        container_layout.addWidget(title_label)

        # Table
        table = QTableWidget(13, 2)  # 13 rows, 2 columns
        table.setHorizontalHeaderLabels(["Code ID", "CODE DESCRIPTION-(SINGLE)"])
        table.setColumnWidth(0, 450)
        table.setColumnWidth(1, 1200)
        table.verticalHeader().setVisible(False)

        # Sample Data
        code_ids = ["0001"] * 13
        descriptions = ["Configure Single Switch to Extract Show Running Configuration & Save TXT"] * 13

        for row, (code_id, description) in enumerate(zip(code_ids, descriptions)):
            table.setItem(row, 0, QTableWidgetItem(code_id))
            table.setItem(row, 1, QTableWidgetItem(description))

        # Apply Styles to the Table
        table.setStyleSheet("""
            QTableWidget {
                background-color: #f9f9f9;
                border: none;  /* Removed the border completely */
                font-size: 12pt;
                gridline-color: #dcdcdc;
            }
            QTableWidget::item {
                padding: 8px;
            }
            QHeaderView::section {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                border: none;  /* Removed the border from the header section */
            }
            QTableWidget::item:hover {
                background-color: #e3f2fd;  /* Light blue background for hovered item */
            }
            QTableWidget::item:selected {
                background-color: #c5cae9;  /* Highlight selected item */
            }
        """)
        container_layout.addWidget(table)

        # Back Button
        back_button = QPushButton("Back")
        back_button.setFixedSize(100, 40)
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border-radius: 8px;
                padding: 8px;
            }
        """)
        back_button.clicked.connect(self.open_device_selection_page)

        # Back Button Layout
        back_button_layout = QHBoxLayout()
        back_button_layout.addWidget(back_button)
        back_button_layout.setAlignment(Qt.AlignLeft)  # Align the button to the left
        container_layout.addLayout(back_button_layout)

        # Centering the container in the content frame
        content_layout.addWidget(device_selection_frame, alignment=Qt.AlignCenter)

        # Set the layout for the content frame
        content_frame.setLayout(content_layout)
        return content_frame

    
    def create_single_device_page(self):
        """Creates the single device page with a table."""
        content_frame = QFrame()
        content_layout = QVBoxLayout()

        # Container Frame for Title, Table, and Back Button
        device_selection_frame = QFrame()
        container_layout = QVBoxLayout()
        device_selection_frame.setLayout(container_layout)
        device_selection_frame.setFixedSize(1680, 970)
        device_selection_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 20px;  /* Rounded corners */
                border: 2px solid #dcdcdc;  /* Light border */
            }
        """)

        # Title
        title_label = QLabel("Single Device")
        title_label.setFont(QFont("Arial", 18, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)  # Center the title
        title_label.setStyleSheet("margin: 20px 0; font-weight: bold;")
        container_layout.addWidget(title_label)

        # Table
        table = QTableWidget(13, 2)  # 13 rows, 2 columns
        table.setHorizontalHeaderLabels(["Code ID", "CODE DESCRIPTION-(SINGLE)"])
        table.setColumnWidth(0, 500)
        table.setColumnWidth(1, 1150)
        table.verticalHeader().setVisible(False)

        # Sample Data
        code_ids = ["0001"] * 13
        descriptions = ["Configure Single Switch to Extract Show Running Configuration & Save TXT"] * 13

        for row, (code_id, description) in enumerate(zip(code_ids, descriptions)):
            table.setItem(row, 0, QTableWidgetItem(code_id))
            table.setItem(row, 1, QTableWidgetItem(description))

        # Apply Styles to the Table
        table.setStyleSheet("""
            QTableWidget {
                background-color: #f9f9f9;
                border: none;  /* Removed the border completely */
                font-size: 12pt;
                gridline-color: #dcdcdc;
            }
            QTableWidget::item {
                padding: 8px;
            }
            QHeaderView::section {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                border: none;  /* Removed the border from the header section */
            }
            QTableWidget::item:hover {
                background-color: #e3f2fd;  /* Light blue background for hovered item */
            }
            QTableWidget::item:selected {
                background-color: #c5cae9;  /* Highlight selected item */
            }
        """)
        container_layout.addWidget(table)

        # Back Button
        back_button = QPushButton("Back")
        back_button.setFixedSize(100, 40)
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border-radius: 8px;
                padding: 8px;
            }
        """)
        back_button.clicked.connect(self.open_device_selection_page)

        # Back Button Layout
        back_button_layout = QHBoxLayout()
        back_button_layout.addWidget(back_button)
        back_button_layout.setAlignment(Qt.AlignLeft)  # Align the button to the left
        container_layout.addLayout(back_button_layout)

        # Centering the container in the content frame
        content_layout.addWidget(device_selection_frame, alignment=Qt.AlignCenter)

        # Set the layout for the content frame
        content_frame.setLayout(content_layout)
        return content_frame

    def create_multiple_device_page(self):
        """Creates the multiple devices page with a table."""
        content_frame = QFrame()
        content_layout = QVBoxLayout()

        # Container Frame for Title, Table, and Back Button
        device_selection_frame = QFrame()
        container_layout = QVBoxLayout()
        device_selection_frame.setLayout(container_layout)
        device_selection_frame.setFixedSize(1680, 970)
        device_selection_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 20px;  /* Rounded corners */
                border: 2px solid #dcdcdc;  /* Light border */
            }
        """)

        # Title
        title_label = QLabel("Multiple Devices")
        title_label.setFont(QFont("Arial", 18, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)  # Center the title
        title_label.setStyleSheet("margin: 20px 0; font-weight: bold;")
        container_layout.addWidget(title_label)

        # Table (for multiple devices)
        table = QTableWidget(13, 2)  # 13 rows, 2 columns (like single device)
        table.setHorizontalHeaderLabels(["Code ID", "CODE DESCRIPTION-(MULTIPLE)"])
        table.setColumnWidth(0, 500)
        table.setColumnWidth(1, 1150)
        table.verticalHeader().setVisible(False)

        # Sample Data (same as single device)
        code_ids = ["0001"] * 13
        descriptions = ["Configure Multiple Devices for Running Config & Save TXT"] * 13

        # Populate the table with code_ids and descriptions
        for row, (code_id, description) in enumerate(zip(code_ids, descriptions)):
            table.setItem(row, 0, QTableWidgetItem(code_id))
            table.setItem(row, 1, QTableWidgetItem(description))

        # Apply Styles to the Table
        table.setStyleSheet("""
            QTableWidget {
                background-color: #f9f9f9;
                border: none;  /* Removed the border completely */
                font-size: 12pt;
                gridline-color: #dcdcdc;
            }
            QTableWidget::item {
                padding: 8px;
            }
            QHeaderView::section {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                border: none;  /* Removed the border from the header section */
            }
            QTableWidget::item:hover {
                background-color: #e3f2fd;  /* Light blue background for hovered item */
            }
            QTableWidget::item:selected {
                background-color: #c5cae9;  /* Highlight selected item */
            }
        """)
        container_layout.addWidget(table)

        # Back Button
        back_button = QPushButton("Back")
        back_button.setFixedSize(100, 40)
        back_button.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border-radius: 8px;
                padding: 8px;
            }
        """)
        back_button.clicked.connect(self.open_device_selection_page)

        # Back Button Layout
        back_button_layout = QHBoxLayout()
        back_button_layout.addWidget(back_button)
        back_button_layout.setAlignment(Qt.AlignLeft)  # Align the button to the left
        container_layout.addLayout(back_button_layout)

        # Centering the container in the content frame
        content_layout.addWidget(device_selection_frame, alignment=Qt.AlignCenter)

        # Set the layout for the content frame
        content_frame.setLayout(content_layout)
        return content_frame
    
    
    def open_main_page(self):
        """Navigate back to the main page."""
        self.pages.setCurrentIndex(0)

    def open_choose_vendor_page(self):
        """Navigate to the choose vendor page."""
        self.pages.setCurrentIndex(1)

    def open_device_type_page(self, vendor_name):
        """Navigate to the device type page."""
        self.pages.setCurrentIndex(2)

    def open_device_selection_page(self):
        """Navigate to the device selection page."""
        self.pages.setCurrentIndex(3)

    def open_single_device_page(self):
        """Navigate to the single device page."""
        self.pages.setCurrentIndex(4)

    def open_multiple_device_page(self):
        """Navigate to the single device page."""
        self.pages.setCurrentIndex(5)

# Run the Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dashboard = AutoPynetDashboard()
    dashboard.show()
    sys.exit(app.exec_())
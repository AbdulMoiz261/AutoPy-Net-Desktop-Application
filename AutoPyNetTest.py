import time
import pyautogui
import subprocess
import sys

# Function to open the application
def open_application():
    app_path = r"C:\Users\Abdul Moiz Nouman\Desktop\autopynet_dashboard\main.py"
    python_executable = sys.executable  # Get the path of the Python interpreter
    subprocess.Popen([python_executable, app_path])  # Run the script with Python
    time.sleep(5)  # Wait for the application to load

# Function to choose the vendor (Cisco)
def choose_vendor():
    # You may need to adjust the coordinates based on where the 'Choose Vendor' button is located
    vendor_button_location = pyautogui.locateOnScreen('choose_vendor_button_image.png')
    if vendor_button_location:
        pyautogui.click(vendor_button_location)
        time.sleep(1)
        
        # Select Cisco from the vendor options (assuming you have coordinates for Cisco)
        cisco_option_location = pyautogui.locateOnScreen('cisco_option_image.png')
        if cisco_option_location:
            pyautogui.click(cisco_option_location)
            time.sleep(1)

# Function to select the device type (Switch)
def select_device_type():
    # Click the device type dropdown
    device_dropdown_location = pyautogui.locateOnScreen('device_dropdown_image.png')
    if device_dropdown_location:
        pyautogui.click(device_dropdown_location)
        time.sleep(1)

    # Select 'Switch' from the device options
    switch_option_location = pyautogui.locateOnScreen('switch_option_image.png')
    if switch_option_location:
        pyautogui.click(switch_option_location)
        time.sleep(1)

# Function to select the configuration (Single Device)
def select_device_configuration():
    # Click the configuration dropdown
    config_dropdown_location = pyautogui.locateOnScreen('config_dropdown_image.png')
    if config_dropdown_location:
        pyautogui.click(config_dropdown_location)
        time.sleep(1)

    # Select 'Single Device' configuration
    single_device_option_location = pyautogui.locateOnScreen('single_device_option_image.png')
    if single_device_option_location:
        pyautogui.click(single_device_option_location)
        time.sleep(1)

# Function to select the command (switch_ping)
def select_command():
    # Open the command list (assuming this is done by clicking a button)
    command_button_location = pyautogui.locateOnScreen('command_button_image.png')
    if command_button_location:
        pyautogui.click(command_button_location)
        time.sleep(1)

    # Select the command '0001 - switch_ping'
    switch_ping_command_location = pyautogui.locateOnScreen('switch_ping_command_image.png')
    if switch_ping_command_location:
        pyautogui.click(switch_ping_command_location)
        time.sleep(1)

# Main function to automate the steps
def automate_steps():
    # Step 1: Open the application
    open_application()

    # Step 2: Choose the vendor (Cisco)
    choose_vendor()

    # Step 3: Select the device type (Switch)
    select_device_type()

    # Step 4: Select the configuration (Single Device)
    select_device_configuration()

    # Step 5: Select the command (0001 - switch_ping)
    select_command()

# Run the automation
if __name__ == '__main__':
    automate_steps()

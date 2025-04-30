from netmiko import ConnectHandler

def show_running_config():
    ip = "10.10.10.17"

    device = {
        "device_type": "cisco_ios",
        "ip": ip,
        "username": "admin",
        "password": "cisco123"
    }

    try:
        connection = ConnectHandler(**device)
        print(f"\nConnected to {ip}\n")

        output = connection.send_command("show running-config")
        print("===== Running Configuration =====")
        print(output)

        connection.disconnect()

    except Exception as e:
        print(f"Error: {e}")

# Call the function
show_running_config()

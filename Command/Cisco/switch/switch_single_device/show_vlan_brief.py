from netmiko import ConnectHandler

def show_vlan_brief():
    device = {
        "device_type": "cisco_ios",
        "ip": "10.10.10.17",  # Hardcoded IP
        "username": "admin",
        "password": "admin123"
    }

    try:
        print(f"\nConnecting to {device['ip']}...")
        connection = ConnectHandler(**device)
        print(f"Successfully connected to {device['ip']}.\n")

        output = connection.send_command("show vlan brief")
        print("===== VLAN Brief =====")
        print(output)

        connection.disconnect()
        print("\nConnection closed.")

    except Exception as e:
        print(f"\nError: {e}")


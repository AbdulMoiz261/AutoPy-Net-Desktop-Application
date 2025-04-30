from netmiko import ConnectHandler

def show_arp_table():
    device = {
        "device_type": "cisco_ios",
        "ip": "10.10.10.17",  # Hardcoded IP address
        "username": "admin",
        "password": "admin123"
    }

    try:
        print(f"\nConnecting to {device['ip']}...")
        connection = ConnectHandler(**device)
        print(f"Successfully connected to {device['ip']}.\n")

        output = connection.send_command("show arp")
        print("===== ARP Table =====")
        print(output)

        connection.disconnect()
        print("\nConnection closed.")

    except Exception as e:
        print(f"\nError: {e}")


from netmiko import ConnectHandler

def configure_vlan():
    device = {
        "device_type": "cisco_ios",
        "ip": "10.10.10.17",  # Hardcoded IP
        "username": "admin",
        "password": "admin123",
    }

    commands = [
        "vlan 10",
        "name Test Vlan"
    ]

    try:
        net_connect = ConnectHandler(**device)
        print(f"\nConnected to {device['ip']}\n")

        for command in commands:
            print(f"Sending command: {command}")
            output = net_connect.send_config_set(command)
            print(output)

        net_connect.send_command("write memory")
        print("\nConfiguration saved.")

        net_connect.disconnect()

    except Exception as e:
        print(f"\nFailed to connect to {device['ip']}: {e}")

# Call the function directly
configure_vlan()
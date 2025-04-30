from netmiko import ConnectHandler

def enable_ip_routing():
    # Hardcoded device details
    device = {
        "device_type": "cisco_ios",
        "ip": "10.10.10.15",
        "username": "admin",
        "password": "cisco123",
    }

    commands = ["ip routing"]

    try:
        net_connect = ConnectHandler(**device)
        print(f"\nConnected to {device['ip']}\n")

        for command in commands:
            print(f"Sending command: {command}")
            output = net_connect.send_config_set(command)
            print(f"Output: {output}")

        net_connect.send_command("write memory")
        print("\nConfiguration saved.")

        net_connect.disconnect()

    except Exception as e:
        print(f"\nFailed to connect to {device['ip']}: {e}")

# Call the function
enable_ip_routing()
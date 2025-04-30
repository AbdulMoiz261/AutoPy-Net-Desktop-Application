from netmiko import ConnectHandler

def configure_rip():
    device = {
        "device_type": "cisco_ios",
        "ip": "10.10.10.15",
        "username": "admin",
        "password": "admin123",
    }

    commands = [
        "router rip",
        "version 2",
        "no auto-summary",
        "network 10.0.0.0"
    ]

    try:
        net_connect = ConnectHandler(**device)
        print(f"\nConnected to {device['ip']}\n")

        print("Configuring RIP routing...")
        output = net_connect.send_config_set(commands)
        print(f"RIP Configuration Output:\n{output}")

        net_connect.send_command("write memory")
        print("\nConfiguration saved.")

        net_connect.disconnect()

    except Exception as e:
        print(f"\nFailed to connect to {device['ip']}: {e}")
configure_rip()
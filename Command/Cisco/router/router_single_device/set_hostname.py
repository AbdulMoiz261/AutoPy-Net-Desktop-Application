from netmiko import ConnectHandler

def set_hostname():
    ip = "10.10.10.15"
    device = {
        "device_type": "cisco_ios",
        "ip": ip,
        "username": "admin",
        "password": "admin123",
    }

    hostname = "Router-1"
    commands = [f"hostname {hostname}"]

    try:
        net_connect = ConnectHandler(**device)
        print(f"\nConnected to {ip}\n")

        for command in commands:
            print(f"Sending command: {command}")
            output = net_connect.send_config_set(command)
            print(f"Output: {output}")

        net_connect.send_command("write memory")
        print("\nConfiguration saved.")

        net_connect.disconnect()

    except Exception as e:
        print(f"\nFailed to connect to {ip}: {e}")
set_hostname()
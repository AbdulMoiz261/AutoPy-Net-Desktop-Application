from netmiko import ConnectHandler

def show_running_config():
    ip = "10.10.10.15"
    device = {
        "device_type": "cisco_ios",
        "ip": ip,
        "username": "admin",
        "password": "admin123",
    }

    try:
        net_connect = ConnectHandler(**device)
        print(f"\nConnected to {ip}\n")

        print("Running 'show running-config' command...")
        output = net_connect.send_command("show running-config")
        print(output)

        net_connect.disconnect()

    except Exception as e:
        print(f"\nFailed to connect to {ip}: {e}")
show_running_config()
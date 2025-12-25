from netmiko import ConnectHandler
from datetime import datetime

device = {
    'device_type': 'cisco_ios',
    'host': '192.0.2.1',  # placeholder IP
    'username': 'admin',
    'password': 'password',
}

connection = ConnectHandler(**device)
config = connection.send_command('show running-config')
connection.disconnect()

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"backup_{timestamp}.txt"

with open(filename, 'w') as file:
    file.write(config)

print(f"Configuration backed up to {filename}")


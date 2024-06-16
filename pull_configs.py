from Netmiko import Netmiko

my_device = {
	'host': '10.32.1.151',
	'username': 'mark',
	'password': 'mark',
	'device_type': 'cisco_ios',
}

net_conn = Netmiko(**my_device)
output = net_conn.send_command_timing('copy running-config tftp://10.32.1.90/MarkslanR_config.txt')
if 'Address' in output:
	output += net_connect.send_command_timing("\n")

if 'Destination' in output:
	output += net_connect.send_command_timing("\n")

net_connect.disconnect()

print(output)

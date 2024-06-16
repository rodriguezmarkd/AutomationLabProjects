from netmiko import Netmiko

hosts = ['10.32.1.210', '10.32.1.211', '10.32.1.212', '10.32.1.213']


for host in hosts:
	my_device = {
		'host': host,
		'username': 'mark',
		'password': 'mark',
		'device_type': 'cisco_ios',
	}

	net_conn = Netmiko(**my_device)
	output = net_conn.send_command_timing(f'copy running-config tftp://10.32.1.90/{host}.txt')
	if 'Address' in output:
		output += net_conn.send_command_timing("\n")

	if 'Destination' in output:
		output += net_conn.send_command_timing("\n")

net_conn.disconnect()

print(output)

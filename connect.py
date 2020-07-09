from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "ip":"10.1.1.1",
    "username":"admin",
    "password":"admin",
    "secret":"admin"
}

ssh = ConnectHandler(**device)
ssh.enable()
#ssh.send_config_set("hostname duy")
#print(ssh.send_config_set("hostname duy"))
command = ["int loop 0", "ip add 172.16.1.1 255.255.255.0"]
ssh.send_config_set(command)
print(ssh.send_config_set("do sh ip int br"))
output = ssh.find_prompt()
print(output)
ssh.disconnect()
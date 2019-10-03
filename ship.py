from netmiko import ConnectHandler

r1 = {
        "device_type" : "cisco_ios",
        "ip" : "10.10.10.1",
        "username" : "dharmo",
        "password" : "dharmo"
}

conn = ConnectHandler(**r1)

print conn.send_command("show ip int br")

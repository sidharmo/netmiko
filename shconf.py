from netmiko import ConnectHandler
import getpass

ip_router = raw_input("Masukan IP Router: ")
username = raw_input("Masukan Username: ")
password = getpass.getpass()

config_list = ['int lo30','ip address 10.0.0.30 255.255.255.255', 'int lo31','ip address 10.10.10.31 255.255.255.255']

r1 = {
        "device_type" : "cisco_ios",
        "ip" : ip_router,
        "username" : username,
        "password" : password
}

conn = ConnectHandler(**r1)

print conn.send_config_set(config_list)
print conn.send_command("sh ip int br")

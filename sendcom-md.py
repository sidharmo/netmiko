from netmiko import ConnectHandler
import getpass

username = raw_input("Username: ")
password = getpass.getpass()

r1 = {
        "device_type" = "cisco_ios",
        "ip" = 10.10.10.1,
        "username" = username,
        "password" = password
}
r3 = {
        "device_type" = "cisco_ios",
        "ip" = 10.10.10.3,
        "username" = username,
        "password" = password
}

router_list = (r1,r3)
for router in router_list
 conn = ConnectHandler(**router)
 print "IP Address on {}".format(router["ip"])
 print conn.send_command("show ip int brief")
 print "\n\n"

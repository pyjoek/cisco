## make sure to install the required package
#### pip install pyautogui

#######################################
### example of how to run the file ######
## python main.py -a args // to see all available configurations
## python main.py -a ssh // or the one you want
## remember to change the ip addresses to your own choice

import pyautogui as p
from time import sleep

def write():
    p.press("enter")
    sleep(1)

def conf_t():
    p.write("en")
    write()
    p.write("conf t")

#assing ip
def asssign_ip():
    sleep(1)
    p.write("int gig0/0/0")
    write()
    p.write("ip address 192.168.1.1 255.255.255.0") 
    write() 
    p.write("do wr")
    write()
    p.write("exit")
    write()

#local
def local_cridential():
    sleep(1)
    p.write("username admin privilege 15 secret cisco")
    write()

#telnet
def telnet():
    sleep(1)
    p.write("line vty 0 4")
    write()
    p.write("login local")
    write()
    p.write("logging synchronous")
    write()
    p.write("exec-timeout 0")
    write()
    p.write("do wr")
    write()

#console
def console():
    sleep(1)
    p.write("line console 0 4")
    write()
    p.write("login local")
    write()
    p.write("logging synchronous")
    write()
    p.write("exec-timeout 0")
    write()
    p.write("do wr")
    write()

#ssh
def ssh():
    sleep(1)
    p.write("ip domain-name knowit.org")
    write()
    p.write("crypto key generate rsa")
    write()
    p.write("2048")
    write()
    p.write("ip ssh version 2")
    write()
    p.write("do wr")
    write()

#dhcp
def dhcp():
    sleep(1)
    p.write("ip dhcp exclude-address 192.168.1.11 192.168.1.240")
    write()
    p.write("ip dhcp pool first_pool")
    write()
    p.write("network 192.168.1.0 255.255.255.0")
    write()
    p.write("default-router 192.168.1.1")
    write()
    p.write("dns-server 8.8.8.8")
    write()
    p.write("exit")
    write()

##configuring rip version 2
def rip2():
    p.write("conf t")
    write()
    p.write("router rip")
    write()
    p.write("version 2")
    write()
    p.write("no auto-summary")
    write()
    p.write("network 192.168.1.0")
    write()
    p.write("exit")
    write()
    p.write("do wr")
    write()

##configuring rip version 1
def rip1():
    p.write("conf t")
    write()
    p.write("router rip")
    write()
    p.write("version 1")
    write()
    p.write("network 192.168.1.0")
    write()
    p.write("exit")
    write()
    p.write("do wr")
    write()

#configuring eigrp
def eigrp():
    p.write("router eigrp 100")
    write()
    p.write("network 192.168.1.0 0.0.0.3")
    write()
    p.write("show route eigrp")
    write()

#########verify
## rip = 
## dhcp = show ip dhcp binding [OR] show ip dhcp pool
## eigrp = show route eigrp [OR] show ip protocols [OR] show ip eigrp neighbours
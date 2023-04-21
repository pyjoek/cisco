from cisco import *
from optparse import OptionParser

parser = OptionParser()

parser.add_option('-a','--arguments',dest = "args", type = str, help = "current arguments")

(option,argument) = parser.parse_args()
args = option.args

if args == 'args':
    print('''
Current Arguments are :
1) Telnet
2) SSH
3) Assigning IP
4) Console
5) Creating LOcal username and password
6) DHCP
7) RIPv1
8) RIPv2
''')
elif args == 'telnet':
    telnet()
elif args == 'ssh':
    ssh()
elif args == 'console':
    console()
elif args == 'dhcp':
    dhcp()
elif args == 'rip1':
    rip1()
elif args == 'rip2':
    rip2()
elif args == 'dhcp':
    dhcp()
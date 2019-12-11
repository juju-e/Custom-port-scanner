import socket
import sys

ports={
    "-ftp-d":20,
    "-ftp-c":21,
    "-ssh":22,
    "-telnet":23,
    "-smtp":25,
    "-dns":53,
    "-dhcp":67,
    "-dhcp":68,
    "-http":80,
    "-pop3":110,
    "-nntp":119,
    "-ntp":123,
    "-imap":143,
    "-snmp":161,
    "-irc":194,
    "-https":443
    }
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if sys.argv[1]=="-all":
    for a in range(60000):
       if not s.connect_ex(('localhost',a)):
        print("open port is "+str(a))
    print("")    
    print("no other")    
else:        
  for arg in range(1,len(sys.argv)):
    if  s.connect_ex(('localhost',ports[sys.argv[arg]])):
        print("port "+"".join(sys.argv[arg].split("-"))+" is closed")
    else:
        print("this port is open")
              
      

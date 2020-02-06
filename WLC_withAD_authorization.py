#!/usr/bin/env python

""" this examples show how to send commands and receive the outputs for 
    those commands and also to check the current prompt of the device 
"""

from netmiko import Netmiko
from getpass import getpass
from easyad import EasyAD
from json import dumps

 #first creating devices and its login creds and dict
 
 # after the password is given check and verify it with AD
 loginas = input("Put your login credentials or just press enter to leave it empty")
 username = input("Enter username: ")
 password = getpass("Enter password:")
 cisco1 = {
     'device_type' : 'cisco_WLC',
     'ip' : 'ip addr',
     'username' : username,
     'password' : password,
     'port' : 22,
      }
#creating a dict for setting up configuration of our active directory

Config = dict(
        AD_SERVER = "xxxx", #put your active directory server
        AD_DOMAIN = "xxxx", #put your active directory domain name
        CA_CERT_FILE = ""   #mention your actice dir certificate location
)

ad = EasyAD(Config)

 user = ad.authenticate(username, password, json_safe = True)
 
 if user:
     print(dumps(user, sort_keys=True, indent=2, ensure_ascii=False))
     
 else:
     print("invalid credentials")
  
# connection with WLC or network device is done through below code
 cnet = ConnectHandler(**cisco1)
 
 print ("Connection established")
 
 prompt = cnet.find_prompt()
 print (prompt)
 
 if (prompt == 'Loginas') :
     loginas
     output = cnet.send_command('putyour WLC commands here')
     
 else:
     print(' Device not configured ')
    

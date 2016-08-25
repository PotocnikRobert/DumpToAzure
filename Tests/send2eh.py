import time
import sys
import socket
from azure.servicebus import ServiceBusService


key_name = "key_name;
key_value = "key";

sbs = ServiceBusService("flightdata",shared_access_key_name=key_name, shared_access_key_value=key_value);

#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 30003
BUFFER_SIZE = 1024

while(True):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	data = s.recv(BUFFER_SIZE)
	s.close()
	
	msg = str(data)
	msg = msg[2:]
	msg = msg[:-5]
	list = msg.split(",")
	
	print("______________________")
	for item in list:
    		print(item)
	print("______________________")
	result = ""
	result += "{"
	
	result += '"MessageType": "'
	result += list[0]
	result += '", '
	result += '"TransmissionType": "'
	result += list[1]
	result += '", '
	result += '"SessionID": "'
	result += list[2]
	result += '", '
	result += '"AircraftID": "'
	result += list[3]
	result += '", '
	result += '"HexIdent": "'
	result += list[4]
	result += '" '
	result += "}"
	print(result)


	#print "received data:", data

#while(True):
#	print('sending...')
#	sbs.send_event('radardata', '{ "DeviceId": "smokerpi", "Temperature": "37.0" }')
#	print('sent!')
#	time.sleep(10)
